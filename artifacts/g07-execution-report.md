# G-07 Execution Report: Numerical Null-Helix Stability Analysis

**Phase 1-2: DDG Framework + Discretisation**
**Date:** 2026-07-30
**Script:** `ddg/null_helix_ddg.py`

## 1. Framework

The computational framework for the discrete null-helix stability analysis has been implemented as `ddg/null_helix_ddg.py`. The framework includes:

- Null-helix parametrisation in dimensionless units (m_e = c = ħ = 1)
- Discrete differential geometry (DDG) for curvature κ and torsion τ
- Curvature-torsion energy functional E[γ] = Σ (κ_i² - τ_i²) Δs_i
- Parameter sweep over pitch angle θ ∈ [0.001, 0.1] rad

## 2. Discretisation Test Results

| Metric | Analytic | DDG (N=5000) | Relative Error |
|:-------|:---------|:-------------|:---------------|
| Curvature κ | 2.92×10⁻⁴ | **3.08×10⁻⁴** | 5.5% |
| Torsion τ | 2.00 | **1.88** | 6.2% |
| Energy per segment E/N | — | 1.05×10⁻⁴ | — |

The DDG framework recovers curvature and torsion to within 5-6% of analytic values at N=5000 segments. This is sufficient accuracy for a parameter sweep that identifies the location of the energy minimum — the exact value can be refined with higher N or higher-order discretisation.

## 3. Parameter Sweep

| θ (deg) | α = tan(θ) | E/N |
|:--------|:-----------|:----|
| 0.006° | 0.0001 | 4.4×10⁻⁹ |
| 0.06° | 0.0010 | 4.7×10⁻⁷ |
| 0.29° | 0.0051 | 1.2×10⁻⁵ |
| 0.42° | 0.0073 (physical) | 2.5×10⁻⁵ |
| 1.0° | 0.0175 | 1.4×10⁻⁴ |
| 2.0° | 0.0349 | 5.7×10⁻⁴ |
| 3.0° | 0.0524 | 1.3×10⁻³ |
| 5.0° | 0.0875 | 3.6×10⁻³ |

**Key finding:** E(θ) is monotonically increasing over the swept range — NO local minimum at the physical α ≈ 1/137 (θ ≈ 0.42°). The energy functional E[γ] = Σ (κ_i² - τ_i²) Δs_i does NOT have a stationary point at the physical pitch angle at this discretisation level (N=5000).

## 4. Interpretation

The absence of a minimum in E(θ) at the physical α has three possible interpretations:

1. **The null-helix model does not capture α.** The curvature-torsion functional may not be the correct stability condition for the electron. The physical α is determined by a different variational principle (e.g., a minimum in the electromagnetic self-energy, a fixed point of the renormalisation group, or a different energy functional).

2. **Constraints are missing.** The current sweep does not enforce the non-radiation constraint (Poynting flux = 0) or the single-valuedness constraint (wavefunction periodicity). Adding these constraints may introduce a minimum at the physical α.

3. **The sign of the functional may be wrong.** The energy functional E = κ² - τ² penalises torsion (τ² term is subtractive). If the physical electron minimises κ² + τ² (both additive) or maximises τ²/κ² (torsion-dominant), a different functional may capture the correct physics. The functional was conjectured in P2 based on a curvature-torsion balance analogy; the monotonic result suggests the conjecture needs revision.

## 5. Next Steps

- **Phase 3:** Implement constraint enforcement (non-radiation, single-valuedness)
- **Phase 3 alt:** Test alternative functionals (E = κ² + τ², E = τ²/κ², E = |κ - τ|)
- **Phase 4:** Full gradient-descent optimisation with constraints
- **Phase 5:** Convergence analysis as N → ∞

## 6. Transparent Reporting

**The physical α is NOT the minimum of E(θ) = κ² - τ² for the unconstrained null helix at N=5000.** This is a null result — the simplest formulation of the P2 conjecture does not hold. The finding does NOT falsify the broader hypothesis that α is a geometric eigenvalue; it only shows that the specific conjectured functional, in its simplest unconstrained form, does not yield α as a minimum.

This is exactly the type of result that the Bayesian cascade in the P2 Deep Research appendix anticipated: the prior probability of α = 1/137 emerging from the simplest functional was estimated at 0.05 (P2 Deep Research, Stage 4). The null result is consistent with the low prior — and the Phase 3-4 constraints are where the true hypothesis test lies.

## 7. Adelic Interpretation

The discrete null helix in DDG form is a computational instance of the adelic framework. The null curve lives in Minkowski space (the archimedean place), but its periodicity constraint — the requirement that the helix close on itself after one Compton period — is fundamentally a topological condition analogous to a p-adic valuation condition on the winding number. The relationship between the Archimedean pitch angle θ and the number of turns per Compton period may be the true determinant of α, rather than the local curvature-torsion balance.
