#!/usr/bin/env python3
"""G-07: Numerical Stability Analysis of the Discrete Null Helix.

Phase 1-2: DDG Library Setup + Null-Curve Discretisation.
Phase 3-4: Constraint Implementation + Energy Minimisation.
Phase 5: Verification.

The null helix is parametrised as:
    γ(s) = (s, R cos(ωs), R sin(ωs), s cos θ)
where ω = 2 (Compton frequency in m_e = c = ħ = 1 units),
R = α (classical electron radius), θ = arctan(α).

The energy functional: E[γ] = Σ (κ_i² - τ_i²) Δs_i
where κ_i is discrete curvature, τ_i is discrete torsion, Δs_i is segment length.

Reference: P7 §4 (DOI 10.5281/zenodo.21697900)
"""

import numpy as np
import argparse
from typing import Tuple


# ─── Physical constants (dimensionless: m_e = c = ħ = 1) ───

ALPHA = 1.0 / 137.035999084  # Fine-structure constant
THETA_ALPHA = np.arctan(ALPHA)  # ~0.0073 rad ≈ 0.42°
OMEGA = 2.0  # Compton frequency: 2m_e c²/ħ → 2 in natural units
LAMBDA_C = 1.0  # Compton wavelength: ħ/(m_e c) → 1
R_E = ALPHA  # Classical electron radius: α·λ_C → α


# ─── Null helix parametrisation ───

def null_helix(s: np.ndarray, theta: float = THETA_ALPHA) -> np.ndarray:
    """Parametrise the null helix γ(s) in (3+1)D Minkowski space.
    
    Args:
        s: Proper time array along the curve.
        theta: Pitch angle (radians). Default: arctan(α) ≈ 0.0073 rad.
    
    Returns:
        γ: Array of shape (len(s), 4) with columns (t, x, y, z).
    """
    R = np.tan(theta)  # r_e = α = tan(θ)
    omega = OMEGA
    gamma = np.zeros((len(s), 4))
    gamma[:, 0] = s                          # t = s
    gamma[:, 1] = R * np.cos(omega * s)      # x = R cos(ωs)
    gamma[:, 2] = R * np.sin(omega * s)      # y = R sin(ωs)
    gamma[:, 3] = s * np.cos(theta)          # z = s cos(θ)
    return gamma


# ─── Discrete Differential Geometry ───

def compute_segments(gamma: np.ndarray) -> Tuple[np.ndarray, np.ndarray]:
    """Compute segment vectors and lengths from the discretised curve.
    
    Args:
        gamma: Array of shape (N+1, 4) — N+1 vertices.
    
    Returns:
        segments: Array of shape (N, 4) — N segment vectors Δγ_i = γ_{i+1} - γ_i.
        lengths: Array of shape (N,) — N segment lengths ||Δγ_i||.
    """
    segments = np.diff(gamma, axis=0)  # (N, 4)
    lengths = np.linalg.norm(segments, axis=1)  # (N,)
    return segments, lengths


def compute_tangents(segments: np.ndarray, lengths: np.ndarray) -> np.ndarray:
    """Compute unit tangent vectors T_i = Δγ_i / ||Δγ_i||.
    
    Args:
        segments: Array of shape (N, 4).
        lengths: Array of shape (N,).
    
    Returns:
        tangents: Array of shape (N, 4).
    """
    with np.errstate(divide='ignore', invalid='ignore'):
        tangents = segments / lengths[:, np.newaxis]
    tangents[np.isnan(tangents)] = 0.0
    return tangents


def compute_curvature(tangents: np.ndarray, lengths: np.ndarray) -> np.ndarray:
    """Compute discrete curvature κ_i at each vertex.
    
    κ_i = ||T_i - T_{i-1}|| / (||Δγ_i|| + ||Δγ_{i-1}||)
    for interior vertices i = 1, ..., N-1.
    
    Args:
        tangents: Array of shape (N, 4) — unit tangent vectors for N segments.
        lengths: Array of shape (N,) — segment lengths.
    
    Returns:
        curvature: Array of shape (N,) — curvature at each vertex.
    """
    N = tangents.shape[0]
    curvature = np.zeros(N + 1)  # N+1 vertices
    for i in range(1, N):
        dT = tangents[i] - tangents[i - 1]
        denom = lengths[i] + lengths[i - 1]
        if denom > 1e-15:
            curvature[i] = np.linalg.norm(dT) / denom
    return curvature


def compute_torsion(gamma: np.ndarray, tangents: np.ndarray,
                    lengths: np.ndarray) -> np.ndarray:
    """Compute discrete torsion τ_i at each vertex.
    
    τ_i = angle between osculating planes / midpoint segment length.
    
    For 3+1D Minkowski space: torsion is computed from the binormal
    rotation between consecutive osculating planes.
    
    Args:
        gamma: Array of shape (N+1, 4) — N+1 vertices.
        tangents: Array of shape (N, 4) — unit tangent vectors.
        lengths: Array of shape (N,) — segment lengths.
    
    Returns:
        torsion: Array of shape (N+1,) — torsion at each vertex.
    """
    N = tangents.shape[0]
    torsion = np.zeros(N + 1)
    
    # Compute binormals from cross product of consecutive tangents
    for i in range(1, N):
        T_prev = tangents[i - 1]
        T_curr = tangents[i]
        T_next = tangents[min(i + 1, N - 1)]
        
        # Normal direction (simplified for null curves)
        N_i = T_curr - T_prev
        N_i_norm = np.linalg.norm(N_i)
        if N_i_norm < 1e-15:
            continue
        
        N_i = N_i / N_i_norm
        
        N_next = T_next - T_curr
        N_next_norm = np.linalg.norm(N_next)
        if N_next_norm < 1e-15:
            continue
        
        N_next = N_next / N_next_norm
        
        # Binormal = T × N
        B_i = np.cross(T_curr[:3], N_i[:3]) if np.linalg.norm(N_i) > 1e-15 else np.zeros(3)
        B_inext = np.cross(T_curr[:3], N_next[:3]) if np.linalg.norm(N_next) > 1e-15 else np.zeros(3)
        
        # Torsion ~ angular rotation of binormal
        B_dot = np.dot(B_i, B_inext) / (np.linalg.norm(B_i) * np.linalg.norm(B_inext) + 1e-15)
        B_dot = np.clip(B_dot, -1.0, 1.0)
        delta_phi = np.arccos(B_dot)
        
        denom = lengths[i] + lengths[i - 1]
        if denom > 1e-15:
            torsion[i] = delta_phi / denom
    
    return torsion


# ─── Energy functional ───

def compute_energy(gamma: np.ndarray) -> Tuple[float, np.ndarray, np.ndarray, np.ndarray]:
    """Compute the curvature-torsion energy functional E[γ] = Σ (κ_i² - τ_i²) Δs_i.
    
    Args:
        gamma: Array of shape (N+1, 4) — N+1 vertices.
    
    Returns:
        E: Total energy.
        curvature: Array of shape (N+1,).
        torsion: Array of shape (N+1,).
        ds: Array of shape (N,) — segment lengths for energy weighting.
    """
    segments, ds = compute_segments(gamma)
    tangents = compute_tangents(segments, ds)
    kappa = compute_curvature(tangents, ds)
    tau = compute_torsion(gamma, tangents, ds)
    
    # Energy: sum over interior vertices (where both κ and τ are defined)
    E = 0.0
    for i in range(1, len(kappa) - 1):
        dsi = 0.5 * (ds[i - 1] + ds[i])  # average segment length around vertex i
        E += (kappa[i]**2 - tau[i]**2) * dsi
    
    return E, kappa, tau, ds


# ─── Parameter sweep ───

def sweep_pitch_angle(N: int = 10000, theta_range: Tuple[float, float] = (0.001, 0.1),
                      n_steps: int = 50) -> Tuple[np.ndarray, np.ndarray]:
    """Sweep the pitch angle θ and compute E(θ) for each value.
    
    Args:
        N: Number of discretisation segments.
        theta_range: (min, max) in radians.
        n_steps: Number of θ values to sweep.
    
    Returns:
        thetas: Array of pitch angles (radians).
        energies: Array of E(θ) / N (energy per segment).
    """
    thetas = np.linspace(theta_range[0], theta_range[1], n_steps)
    alphas = np.tan(thetas)
    energies = np.zeros(n_steps)
    
    for i, (theta, alpha_i) in enumerate(zip(thetas, alphas)):
        # Build helix with specific pitch angle
        s = np.linspace(0, 2 * np.pi, N + 1)  # One Compton period
        gamma = null_helix(s, theta=theta)
        
        # Override R for different α values
        R = alpha_i
        omega = OMEGA
        gamma[:, 0] = s
        gamma[:, 1] = R * np.cos(omega * s)
        gamma[:, 2] = R * np.sin(omega * s)
        gamma[:, 3] = s * np.cos(theta)
        
        E, _, _, _ = compute_energy(gamma)
        energies[i] = E / N  # Energy per segment
    
    return thetas, alphas, energies


# ─── Main ───

def main():
    ap = argparse.ArgumentParser(description='G-07: Null-Helix DDG Stability Analysis')
    ap.add_argument('--N', type=int, default=1000,
                    help='Number of discretisation segments (default: 1000)')
    ap.add_argument('--sweep', action='store_true', default=True,
                    help='Run parameter sweep (default: True)')
    ap.add_argument('--steps', type=int, default=50,
                    help='Number of theta steps in sweep')
    ap.add_argument('--theta-min', type=float, default=0.001,
                    help='Min theta in radians (default: 0.001 ~ 0.057 deg)')
    ap.add_argument('--theta-max', type=float, default=0.1,
                    help='Max theta in radians (default: 0.1 ~ 5.73 deg)')
    args = ap.parse_args()
    
    print('=' * 72)
    print('G-07: NUMERICAL STABILITY ANALYSIS OF THE DISCRETE NULL HELIX')
    print('  E[γ] = Σ (κ_i² - τ_i²) Δs_i')
    print('=' * 72)
    
    # 1. Baseline: compute at the physical α pitch angle
    print(f'\n[1] BASELINE: θ = arctan(α) ≈ {THETA_ALPHA:.6f} rad ({np.degrees(THETA_ALPHA):.4f} deg), N = {args.N}')
    s = np.linspace(0, 2 * np.pi, args.N + 1)
    gamma = null_helix(s, THETA_ALPHA)
    E, kappa, tau, ds = compute_energy(gamma)
    
    print(f'    Total energy E = {E:.6e}')
    print(f'    Energy per segment E/N = {E/args.N:.6e}')
    print(f'    Mean curvature: κ̄ = {np.mean(kappa[1:-1]):.6e}')
    print(f'    Mean torsion:   τ̄ = {np.mean(tau[1:-1]):.6e}')
    
    # Compare to analytic values
    kappa_analytic = ALPHA * OMEGA**2  # κ = α·ω² = α·4 ≈ 0.00029
    tau_analytic = OMEGA * np.cos(THETA_ALPHA)  # τ = ω·cos(θ) ≈ 2.0
    print(f'\n    Analytic: κ = {kappa_analytic:.6e}, τ = {tau_analytic:.6e}')
    print(f'    DDG:      κ̄ = {np.mean(kappa[1:-1]):.6e}, τ̄ = {np.mean(tau[1:-1]):.6e}')
    
    kappa_err = abs(np.mean(kappa[1:-1]) - kappa_analytic) / (kappa_analytic + 1e-15)
    tau_err = abs(np.mean(tau[1:-1]) - tau_analytic) / (tau_analytic + 1e-15)
    print(f'    Relative error: κ_err = {kappa_err:.4%}, τ_err = {tau_err:.4%}')
    
    # 2. Parameter sweep
    if args.sweep:
        print(f'\n[2] PARAMETER SWEEP: θ ∈ [{args.theta_min}, {args.theta_max}] rad, {args.steps} steps')
        thetas, alphas, energies = sweep_pitch_angle(
            args.N, (args.theta_min, args.theta_max), args.steps
        )
        
        print(f'{"θ (rad)":>10s}  {"θ (deg)":>10s}  {"α = tan(θ)":>12s}  {"E/N":>14s}')
        print('-' * 54)
        for i in range(0, len(thetas), max(1, args.steps // 10)):
            print(f'{thetas[i]:10.6f}  {np.degrees(thetas[i]):10.4f}  '
                  f'{alphas[i]:12.6f}  {energies[i]:14.6e}')
        
        # Find minimum
        imin = np.argmin(energies)
        print(f'\n    Minimum energy at θ = {thetas[imin]:.6f} rad '
              f'({np.degrees(thetas[imin]):.4f} deg)')
        print(f'    Corresponding α = {alphas[imin]:.6f}')
        print(f'    Physical α     = {ALPHA:.6f}')
        print(f'    Difference: {(alphas[imin] - ALPHA) / ALPHA:.4%}')
    
    # 3. Gate
    if kappa_err < 0.01:
        print(f'\n[3] GATE: DDG curvature accuracy < 1%   [PASS] ({kappa_err:.4%})')
    else:
        print(f'\n[3] GATE: DDG curvature accuracy < 1%   [FAIL] ({kappa_err:.4%})')
    
    print(f'\n[4] ADELIC INTERPRETATION')
    print(f'    The discrete null helix is the computational instance of')
    print(f'    the helical electron model (P2, DOI 10.5281/zenodo.21691059).')
    print(f'    The curvature-torsion functional tests the hypothesis that')
    print(f'    α ≈ 1/137 is a geometric eigenvalue — a minimum of E(θ).')
    print(f'    Next phase: full optimisation with gradient descent (Phase 3-4),')
    print(f'    verification against N scaling (Phase 5).')
    
    return 0


if __name__ == '__main__':
    main()
