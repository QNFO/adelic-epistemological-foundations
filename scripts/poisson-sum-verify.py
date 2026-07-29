#!/usr/bin/env python3
"""Poisson Summation Verification Script — P3 §8.2 deliverable.

Verifies the analytic bridge between discrete (Q) and continuous (R)
by computing both sides of the Poisson summation identity for the
Gaussian theta function:

    Σ_{n∈Z} e^{-π n² t} = (1/√t) · Σ_{n∈Z} e^{-π n² / t}

This identity is the mathematical heartbeat of the adelic framework:
the LHS is a discrete sum (archimedean place), the RHS is a continuous
Fourier transform, and the Gaussian e^{-πx²} is the unique invariant
kernel that bridges them at every place.

Exit code 0 if max error < 1e-10 (PUBLICATION-GRADE).
"""

import math
import sys
import argparse


def theta(t: float, N: int = 100) -> float:
    """Compute Theta(t) = sum_{n=-N}^{N} e^{-pi n^2 t}."""
    return sum(math.exp(-math.pi * n**2 * t) for n in range(-N, N + 1))


def verify_poisson(N: int = 100, t: float = 1.0) -> tuple[float, float, float]:
    """Verify Poisson summation: Theta(t) = (1/sqrt(t)) * Theta(1/t)."""
    lhs = theta(t, N)
    rhs = theta(1.0 / t, N) / math.sqrt(t)
    error = abs(lhs - rhs)
    return lhs, rhs, error


def main():
    ap = argparse.ArgumentParser(description='Poisson Summation Verification')
    ap.add_argument('--N', type=int, default=100)
    ap.add_argument('--t', type=float, default=1.0)
    ap.add_argument('--range', type=str, default='0.1,10.0,20')
    args = ap.parse_args()

    print('=' * 72)
    print('POISSON SUMMATION VERIFICATION')
    print('  sum_{n} e^{-pi n^2 t} = (1/sqrt(t)) * sum_{n} e^{-pi n^2 / t}')
    print('=' * 72)

    # 1. Convergence test
    print(f'\n[1] CONVERGENCE: t = {args.t}')
    print(f'{"N":>6s}  {"LHS":>22s}  {"RHS":>22s}  {"Error":>12s}')
    print('-' * 72)
    for N in [5, 10, 25, 50, 100, args.N]:
        lhs, rhs, err = verify_poisson(N, args.t)
        print(f'{N:6d}  {lhs:22.16f}  {rhs:22.16f}  {err:12.2e}')

    # 2. Sweep over t range
    start, end, steps = map(float, args.range.split(','))
    steps = int(steps)
    max_err = 0.0
    print(f'\n[2] SWEEP: t in [{start}, {end}], {steps} steps, N = {args.N}')
    print(f'{"t":>8s}  {"LHS":>22s}  {"RHS":>22s}  {"Error":>12s}')
    print('-' * 72)
    for i in range(steps + 1):
        t_val = start + (end - start) * i / steps
        lhs, rhs, err = verify_poisson(args.N, t_val)
        max_err = max(max_err, err)
        if i % max(1, steps // 5) == 0:
            print(f'{t_val:8.4f}  {lhs:22.16f}  {rhs:22.16f}  {err:12.2e}')

    # 3. Physical significance
    print(f'\n[3] PHYSICAL SIGNIFICANCE')
    print(f'    Max error across sweep: {max_err:.2e}')
    print(f'    Planck-scale precision:  ~1e-34 (l_P / R_Hubble)')
    print(f'    QED precision (alpha):   ~1e-9  (CODATA 2022)')
    print(f'    Cosmological precision:  ~1e-5  (CMB temperature)')

    # 4. Adelic interpretation
    print(f'\n[4] ADELIC INTERPRETATION')
    print(f'    Poisson summation is the analytic expression of Q self-duality')
    print(f'    in the adele ring A_Q. The Gaussian bridges ALL places —')
    print(f'    archimedean (R) and non-archimedean (Q_p). This verification')
    print(f'    confirms the bridge holds to {max_err:.0e} — far below any')
    print(f'    physically measurable precision.')

    # 5. Gate
    gate = 1e-10
    print(f'\n[5] GATE: max_error < {gate}')
    if max_err < gate:
        print(f'    PASS — Poisson summation verified. Error {max_err:.0e} < {gate}')
    else:
        print(f'    FAIL — max error {max_err:.0e} exceeds gate {gate}')
        return 1
    return 0


if __name__ == '__main__':
    sys.exit(main())
