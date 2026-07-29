---
title: "Alpha as Bifurcation Parameter: The Helical Electron Stability Problem"
author: "Rowan Brad Quni-Gudzinas"
date: "2026-07-29"
license: "CC-BY-4.0"
doi: "10.5281/zenodo.21690631"
status: "published"
---

**Author:** Rowan Brad Quni-Gudzinas | **Date:** 2026-07-29 | **License:** CC-BY-4.0

## Abstract

The fine-structure constant α $\approx$ 1/137.035999084 has resisted derivation for a century — it appears in the Standard Model as a free parameter, inserted by hand rather than derived from deeper principles. We propose that α is a critical eigenvalue of a geometric stability condition: the electron's Zitterbewegung (ZBW), the oscillatory motion at the Compton frequency predicted by the Dirac equation, is modelled as a classical light-speed helical null-curve in Minkowski space with constant curvature κ and torsion τ. The pitch angle θ = arctan(α) separates three qualitatively distinct geometric regimes: α = 0 (a free, non-interacting straight line), α $\approx$ 1/137 (a stable, charge-bearing, perturbatively tractable helix), and α $\rightarrow$ ∞ (a confined, infinite-coupling circle). We conjecture that α $\approx$ 1/137 is the unique stationary point of a curvature-torsion energy functional — a geometric fixed point rather than a free parameter — and pose the helical stability problem in precise mathematical terms. This paper does not solve the problem; it identifies it, connects it to the existing cross-ratio reframing α = CR(r_e, λ_C; 0, ∞) [1], and provides five specific, dated falsifiability conditions. We also discuss the muon and tau mass ratios (~207, ~3477) as candidate topological winding numbers. The broader context is the QNFO Adelic Physics Program, which argues that ℚ, not ℝ, is the physically accessible base field — if true, coupling constants are not continuous free parameters but discrete geometric invariants.

**Keywords:** fine-structure constant, Zitterbewegung, helical null-curve, bifurcation theory, cross-ratio, electron structure, fundamental constants, adelic physics

---

## 1. Introduction

### 1.1 The α Problem

The fine-structure constant α $\equiv$ e²/(4πε₀$\hbar$c) $\approx$ 1/137.035999084 is one of the most precisely measured dimensionless numbers in physics [established]. It governs the strength of electromagnetic interactions at all accessible energy scales. After a century of measurement, its origin remains unexplained — it is a free parameter in the Standard Model Lagrangian, its value determined by experiment and inserted by hand [established].

The problem is not that α is imprecisely known. It is measured to 0.15 parts per billion [2]. The problem is that nothing in the Standard Model explains *why it takes this value rather than any other*. Unlike the speed of light c, which can be set to 1 by choice of units, or Planck's constant $\hbar$, which is similarly conventional, α is genuinely dimensionless — its value is a fact about the universe that our current theories accept but do not explain.

### 1.2 Prior Attempts

The history of α-derivation attempts is long and uniformly unsuccessful. Eddington proposed α$^{-1}$ = 137 based on a numerological argument involving the number of independent components in a fundamental tensor [3] — falsified by improved measurements showing α$^{-1}$ = 137.035999084, not 137. Wyler derived α$^{-1}$ = 9/(8π⁴)(π⁵/2⁴ 5!)¹/⁴ $\approx$ 137.036 from the geometry of complex bounded domains [4] — elegant but without physical mechanism. Gilson proposed a formula based on intersecting quantum waves [5] — not independently verifiable. The reference class "derivations of fundamental constants" has an empirical success rate indistinguishable from zero [6].

A common objection to any α-derivation attempt is the renormalisation group: α is not a constant but runs with energy scale. At the Z-boson mass (M_Z $\approx$ 91.2 GeV), α(M_Z) $\approx$ 1/128, significantly different from the low-energy value α(0) $\approx$ 1/137. A geometric derivation at the Compton scale (~511 keV) must reconcile with this running. We address this in §2.4.

### 1.3 The Geometric Proposal

This paper proposes a different approach. Rather than attempting to produce a magic formula that yields α $\approx$ 1/137, we pose a geometric stability problem. The claim is:

> **[SPECULATIVE]** The electron's Zitterbewegung can be modelled as a classical light-speed helical null-curve in Minkowski space. The pitch angle of this helix, θ = arctan(α), marks a critical bifurcation point separating three qualitatively distinct geometric regimes. α $\approx$ 1/137 is hypothesised to be the unique stationary point of a curvature-torsion energy functional — a geometric fixed point rather than a free parameter.

The key difference from prior attempts: we do not claim to have derived α. We claim only to have identified a well-posed variational problem whose solution, if it exists, would constitute a derivation. The paper's contribution is the *problem formulation*, not the *solution*.

### 1.4 Structure

§2 develops the helical null-curve model. §3 identifies the three regimes and the bifurcation hypothesis. §4 poses the variational problem. §5 discusses the muon and tau mass ratios as topological winding numbers. §6 connects the model to the adelic physics programme. §7 surveys computational feasibility. §8 provides falsifiability conditions. §9 discusses limitations and open problems.

---

## 2. The Helical Null-Curve Model

### 2.1 Zitterbewegung as Helical Motion

The Dirac equation for a free electron predicts that the velocity operator has eigenvalues ±c, yet the expectation value of the velocity is always less than c [7, 8, established]. This paradox is resolved by the Zitterbewegung — a rapid oscillatory motion at the Compton frequency ω_C = 2m_ec²/$\hbar$ $\approx$ 1.55 × 10²¹ Hz, arising from quantum interference between positive- and negative-energy Fourier components of a localised wave packet [established].

Schrödinger [8] first noted that ZBW can be visualised as the electron tracing a helical path at the speed of light, with the observed subluminal velocity being the time-averaged axial component. Huang [9] provided the definitive treatment. Barut and Zanghi [10] developed a classical model of the Dirac electron in which ZBW emerges naturally from a spinning particle Lagrangian. Hestenes [11] reinterpreted quantum mechanics entirely in terms of ZBW, with the electron as a point charge executing a helical light-speed trajectory whose time average yields the Schrödinger and Dirac equations.

The essential geometry: the electron moves on a helix of radius r_ZBW and pitch λ_C (the Compton wavelength). The instantaneous velocity is c (light-speed along the helical path). The observed velocity is v = c cos θ, where θ is the pitch angle — the angle between the helical path and the forward direction.

### 2.2 The Cross-Ratio Reframing

In a companion paper [1], we established that α can be reframed geometrically as the cross-ratio of two measurable electron length scales:

α = CR(r_e, λ_C; 0, ∞) = r_e / λ_C

where r_e = e²/(4πε₀ m_e c²) $\approx$ 2.818 × 10$^{-1}$⁵ m is the classical electron radius, and λ_C = h/(m_e c) $\approx$ 2.426 × 10$^{-1}$² m is the Compton wavelength. The cross-ratio is the fundamental invariant of projective geometry — preserved under all projective transformations.

This reframing is not circular. The ratio r_e/λ_C is definitionally α, but expressing it as a cross-ratio CR(r_e, λ_C; 0, ∞) reveals a projective invariance that the standard formula e²/(4πε₀$\hbar$c) conceals. The specific value of α is then the specific cross-ratio realised by the actual electron — a geometric parameter, not a free-parameter placeholder.

### 2.3 The Null Helix

A curve γ(s) in Minkowski space parametrised by proper time s is null if its tangent vector is lightlike: g(γ′, γ′) = 0. A null helix has constant curvature κ and torsion τ. In suitable coordinates, the general null helix can be written:

γ(s) = (s, R cos(ωs), R sin(ωs), s cos θ)

where R is the helical radius, ω is the angular frequency, and θ is the pitch angle. The curvature is κ = Rω² and the torsion is τ = ω cos θ. The key dimensionless ratio is:

κ/τ = Rω / cos θ

For the electron, ω = ω_C = 2m_e c²/$\hbar$, R = r_e = α λ_C, and cos θ $\approx$ 1 - α²/2 for small α. The curvature-torsion ratio is directly related to α.

**The crucial observation:** For a null helix, the ratio κ/τ cannot be arbitrary. The condition that the helix be a *persistent, non-radiating, self-consistent* solution imposes constraints on κ/τ — constraints that may determine α.

### 2.4 The RG Running: Addressed

α is not strictly constant — it runs with energy scale. At the Z-boson mass, α(M_Z) $\approx$ 1/128, significantly different from the low-energy value. This does not invalidate a geometric derivation at the Compton scale, for the same reason that the proton mass is determined by QCD at the confinement scale (~200 MeV) even though the strong coupling α_s runs with energy. The claim is:

> **[SPECULATIVE]** The *infrared fixed point* of QED — the value α $\rightarrow$ α(0) $\approx$ 1/137 as the energy scale goes to zero — is determined by the geometric stability condition at the Compton scale. The running of α away from this fixed point is a quantum field-theoretic effect that does not alter the geometric origin of the fixed-point value.

This is analogous to the way the critical temperature of a phase transition is determined by microscopic interactions, even though thermodynamic quantities vary with temperature near the critical point.

---

## 3. The Three Regimes: A Bifurcation Diagram

### 3.1 Regime I: α = 0 — The Free Straight Line

In the limit α $\rightarrow$ 0, the classical electron radius r_e $\rightarrow$ 0. The helix's transverse radius vanishes. The curve becomes a straight null line — a free, non-interacting particle with no electromagnetic coupling. There is no charge, no photon emission, no QED. This is the limit of a massless Weyl fermion or a sterile neutrino. [SPECULATIVE]

Physically, α = 0 is a *qualitatively different universe* — one without electromagnetism as we know it. The transition from α = 0 to α > 0 is not a smooth parameter change; it is a phase transition that creates charge.

### 3.2 Regime II: α $\approx$ 1/137 — The Stable Helix

At the observed value α $\approx$ 1/137, the electron is a tightly wound helix with pitch angle θ $\approx$ arctan(1/137) $\approx$ 0.0073 radians $\approx$ 0.42°. The transverse circumference is 2πr_e $\approx$ 1.77 × 10$^{-1}$⁴ m; the axial advance per Compton period is λ_C $\approx$ 2.426 × 10$^{-1}$² m.

This is the regime of **perturbative QED**. The smallness of α makes perturbation theory work — each additional photon exchange is suppressed by α/π $\approx$ 0.0023. The electron is almost (but crucially not quite) a straight line. This "almost free" property is what makes our universe computationally tractable: Feynman diagrams converge, precision tests are possible, and the Standard Model works.

The conjecture: **[SPECULATIVE]** This specific pitch angle is the unique value at which the helical null-curve is stable against both radiative decay (energy leakage into photon modes) and electromagnetic collapse (the classical self-energy problem). The electron sits at a geometric fixed point.

### 3.3 Regime III: α $\rightarrow$ ∞ — The Confined Circle

In the limit α $\rightarrow$ ∞, the pitch goes to zero. The helix collapses into a pure circle in the transverse plane with no net forward motion. This is the limit of infinitely strong coupling — the electromagnetic self-interaction is so intense that the particle cannot propagate. This regime is inaccessible to perturbative QED and may be physically unrealisable, analogous to the Landau pole of QED. [SPECULATIVE]

### 3.4 The Double Pendulum Analogy

The three regimes are structurally identical to the double pendulum's behaviour [12]:

| Double pendulum | Helical electron |
|:----------------|:-----------------|
| Energy < 1: regular swinging | α = 0: free line |
| Energy > 1: chaotic flipping | α $\approx$ 1/137: stable helix |
| — | α $\rightarrow$ ∞: confined circle |

The integer 1 in the double pendulum is a bifurcation point — a qualitative cliff where the topology of the phase space changes abruptly. The number α $\approx$ 1/137 is hypothesised to be the same kind of critical value — a bifurcation point in the space of possible helical geometries, separating the "free line" phase from the "confined circle" phase. [SPECULATIVE]

The decimal expansion 1/137.035999084... is the flat, Archimedean shadow of a geometric invariant. The invariant itself — the unique self-consistent pitch angle — is the thing of interest. Its decimal name is not.

---

## 4. The Variational Problem

### 4.1 Problem Statement

We pose the following problem in global differential geometry:

> **Problem (Helical Electron Stability).** Let γ: ℝ $\rightarrow$ M⁴ be a smooth null curve in (3+1)-dimensional Minkowski space, parametrised by proper time s, with constant curvature κ > 0 and constant torsion τ > 0. Define the curvature-torsion energy functional:
>
> E[γ] = ∫ [κ(s)² - τ(s)²] ds
>
> Find the stationary points of E[γ] subject to:
> 1. The curve is null: g(γ′, γ′) = 0
> 2. The curve is periodic: γ(s + P) = γ(s) for some period P
> 3. The curve is non-radiating: the electromagnetic field produced by the charged curve has zero net energy flux at infinity
> 4. The curve is single-valued: the wavefunction Ψ(γ(s)) satisfies periodic boundary conditions
>
> **Conjecture:** The unique stationary point satisfying all constraints occurs at κ/τ = α$^{-1}$ $\approx$ 137.036.

### 4.2 Related Variational Problems

This problem generalises several well-studied variational formulations:

- **Euler elastica (Bernoulli, 1744):** Stationary points of ∫ κ² ds for curves in Euclidean space. The solutions are elliptic functions — the bent elastic rod problem.
- **Kirchhoff rod theory (1859):** Adds torsion to the elastica. Stationary points of ∫ (Aκ² + Bτ²) ds for elastic rods with bending and twisting stiffness.
- **Nambu-Goto string (1974):** Stationary points of the area functional for relativistic strings. The null limit (tensionless string) is a special case.
- **Willmore energy (1965):** Stationary points of ∫ (κ² - τ²) dA for surfaces. The analogous curve functional is ∫ (κ² - τ²) ds — precisely the suggested functional.

The helical electron problem can be seen as a **null-curve generalisation of the Kirchhoff rod**, with the additional constraint of periodicity and non-radiation.

### 4.3 Why This Might Work

The choice of functional E[γ] = ∫ (κ² - τ²) ds is not arbitrary. For a null curve:

- κ² ds is the bending energy (analogous to the electromagnetic self-energy of curvature)
- -τ² ds is the torsional energy with opposite sign (torsion reduces the effective energy — a tightly wound helix with large τ has lower effective energy)
- The stationary condition δE = 0 balances curvature against torsion

For constant κ and τ (the helical solution), δE = 0 gives 2κ δκ - 2τ δτ = 0, i.e., κ/τ = constant. The value of this constant is determined by the constraints (periodicity, non-radiation, single-valuedness). The conjecture is that the constraints force κ/τ = α$^{-1}$ $\approx$ 137.

**[UNTESTED]** This variational problem has not been solved. The mathematical tools exist (global differential geometry of null curves, symplectic geometry of the Kirchhoff rod, Noether's theorem for the conservation laws) but have not been applied to this specific formulation.

### 4.4 Computational Approach

Even without an analytic solution, the problem admits numerical investigation:

1. **Discretise the null helix** on a spacetime lattice with spacing ℓ (perhaps the Planck length ℓ_P)
2. **Compute the curvature-torsion functional** E(θ) as a function of pitch angle θ
3. **Sweep θ from 0 to π/2** and identify stationary points
4. **Check stability:** ensure the stationary point is a minimum (second variation positive), not a saddle or maximum
5. **Compare the stationary pitch angle** with arctan(α_obs) $\approx$ 0.0073 rad

A computational experiment of this form would take minutes on a modern workstation. The primary obstacle is formalising the discretisation in a Lorentz-invariant manner — null curves on a Minkowski lattice are subtle because null separation introduces causal structure that Euclidean lattices do not have.

---

## 5. The Muon and Tau: Topological Winding Numbers

### 5.1 The Mass Ratios

The mass ratios of the charged leptons are:

m_μ / m_e $\approx$ 206.7682830
m_τ / m_e $\approx$ 3477.23

These are not random — 207 is close to a prime; 3477 is close to 57 × 61. If the electron's helical structure is characterised by a single winding number (perhaps the number of turns per Compton period), then the muon and tau may correspond to distinct winding numbers.

**[SPECULATIVE]** Conjecture: The electron is the ground state (winding number n = 1) of the helical null-curve. The muon is the n = 207 state. The tau is the n = 3477 state. The mass ratios arise from the energy of curvature — loosely, E(n) ∝ n · E_0, so m_n/m_e = n.

This is reminiscent of the Bohr model of hydrogen, where the energy levels scale as 1/n². The difference is that here the winding is *along the helical path in spacetime*, not around a nucleus.

### 5.2 Falsifiability

If this conjecture is correct, there should be no stable lepton with winding number n between 1 and 207 — the spectrum is discrete. A fourth charged lepton, if discovered, should have a mass ratio close to an integer and no decay channel to a lower-mass lepton of the same type.

**[UNTESTED]** No fourth charged lepton has been observed. The LEP collider excluded charged leptons up to ~100 GeV (m/m_e ~ 200,000). The conjecture is falsifiable: if a fourth lepton is discovered with a mass ratio that is NOT close to an integer, the winding-number conjecture is wrong.

---

## 6. Connection to the Adelic Physics Programme

### 6.1 ℚ as Physical Base Field

The QNFO Adelic Physics Programme [13] argues that the physically accessible base field is ℚ (the rational numbers), not ℝ (the real numbers). Ostrowski's theorem then demands that all p-adic completions ℚ_p be physically meaningful alongside the Archimedean completion ℝ [established — Ostrowski, 1916].

If ℚ is the base field, then coupling constants are not continuous real parameters but rational invariants of a discrete geometric structure. α, as a cross-ratio of rational length scales, is fundamentally a rational number — its apparent irrationality is an artifact of decimal expansion, which is a base-10 Archimedean projection.

### 6.2 α as Rational Invariant

The cross-ratio α = CR(r_e, λ_C; 0, ∞) is a projective invariant. If r_e and λ_C are both rational multiples of the Planck length ℓ_P (the natural fundamental length in quantum gravity), then α is a rational number — specifically, it would be a fraction with denominator approximately 137.

This has a concrete implication: high-precision measurements of α can search for a "rational fingerprint." If α is a rational number with a modest denominator (~10²–10⁴), measurements at sufficient precision would reveal periodicity in its decimal expansion. Current precision (~0.15 ppb) corresponds to ~10 digits — insufficient to detect rational structure unless the denominator is very small. Future improvement to ~1 ppt (parts per trillion) would probe ~12 digits.

**[UNTESTED]** No rational structure has been detected in α at current precision.

### 6.3 Bruhat-Tits Interpretation

In the p-adic strand of the adelic programme, physical geometry at the Compton scale is modelled on a Bruhat-Tits building — a tree-like ultrametric space where each vertex corresponds to a p-adic valuation [14]. The helical null-curve, in this picture, is a path on the Bruhat-Tits tree whose length (in the tree metric) determines α.

This interpretation makes the discreteness of the lepton spectrum (electron, muon, tau) natural: winding numbers are tree-path lengths, which are integers. The masses are proportional to the number of edges traversed in one Compton period. The "fine-structure constant" is then the ratio of the Archimedean projection length (the Compton wavelength) to the ultrametric tree distance (the p-adic valuation).

---

## 7. Computational Feasibility

### 7.1 Numerical Stability Analysis

A computational investigation of the helical stability problem is feasible with current tools:

1. **Discretisation:** Approximate the null helix as a polygonal chain of N segments, each lightlike. The larger N, the better the approximation.
2. **Curvature and torsion estimators:** Use discrete differential geometry (DDG) — the curvature at vertex i is estimated from the angle between adjacent segments; the torsion from the dihedral angle between consecutive osculating planes.
3. **Constraint enforcement:** The periodicity and non-radiation constraints are applied as boundary conditions. The non-radiation constraint is the hardest — it requires computing the Liénard-Wiechert potentials for each segment and checking the Poynting flux at a distant sphere.
4. **Optimisation:** Minimise E(θ) using gradient descent in the space of control points. The gradient is computable analytically from the DDG expressions.

Estimated computational cost: O(N³) for a full optimisation with N ~ 10⁴, requiring ~10¹² floating-point operations — a few hours on a single GPU.

### 7.2 Existing QNFO Infrastructure

The QNFO programme has deployed a 20-principle ultrametric discovery engine [15] with 27+ API endpoints including Bruhat-Tits tree construction and spectral analysis. This infrastructure can be extended to include a helical stability analysis endpoint.

---

## 8. Falsifiability Conditions

The helical stability hypothesis is falsifiable. The following predictions are dated, strength-tagged, and registered in the calibration register of the QNFO Adelic Physics Programme [13].

| # | Prediction | Check Date | Strength | Falsification Condition |
|:--|:-----------|:-----------|:---------|:------------------------|
| F1 | A null-curve variational principle with the functional E[γ] = ∫ (κ² - τ²) ds has stationary points | 2028 | [WEAK] | If no physicist publishes a solution by 2028, the problem is harder than conjectured but the claim is not falsified (it's a proposal, not a prediction of success) |
| F2 | Numerical stability analysis of the discrete null helix identifies a unique stable pitch angle θ* | 2028 | [WEAK] | If numerical optimisation finds NO stationary point, or finds one at a pitch angle inconsistent with arctan(α_obs) to within numerical error, the conjecture is falsified |
| F3 | No stable charged lepton exists with a mass ratio that is not an integer multiple of the electron mass, within experimental precision | Open-ended | [STRONG] | A charged lepton discovered with a non-integer mass ratio (in units of m_e, after accounting for QED radiative corrections) would falsify the winding-number conjecture |
| F4 | α is a rational number — improved precision measurements reveal a terminating or repeating decimal expansion | 2040 | [STRONG] | If α is measured to 1 part in 10¹⁴ with NO rational fingerprint, the ℚ-as-base-field prediction is strongly constrained |
| F5 | The cross-ratio α = CR(r_e, λ_C; 0, ∞) is preserved under all projective transformations — specifically, α is invariant under the duality transformation r_e ↔ ℓ_P²/λ_C (the T-duality of string theory) | 2035 | [WEAK] | If a projective transformation of the electron length scales is found to yield a different cross-ratio, projective invariance is falsified |

---

## 9. Limitations and Open Problems

### 9.1 Quantisation

The helical null-curve model is **classical**. The electron is a quantum object described by the Dirac equation. Quantising the model — promoting the null-curve to a quantum path integral — is an open problem.

The relationship may be analogous to the Bohr model of hydrogen: the classical circular orbits are not literally the quantum states, but the quantisation condition (angular momentum = n$\hbar$) yields the correct energy levels. The helical model may similarly yield α as a *semiclassical* eigenvalue — the quantum corrections may shift it but not destroy the qualitative structure.

### 9.2 The Absolute Scale

The Compton wavelength λ_C = h/(m_e c) sets the absolute scale of the helix. In natural units ($\hbar$ = c = 1), the question is: why m_e $\approx$ 4.2 × 10⁻²³ m_P, where m_P is the Planck mass? The helical model does not address this — it explains the *ratio* r_e/λ_C = α, not the absolute value of λ_C.

The absolute scale may be determined by the Planck-scale discretisation — the Compton wavelength is the smallest length at which a helical structure can form on the Planck lattice without collapsing into a black hole. This is the territory of quantum gravity and is beyond the scope of the present proposal.

### 9.3 Radiative Corrections

The measured value of α includes contributions from virtual electron-positron pairs, muons, taus, and hadrons. A geometric derivation at the Compton scale would yield a "bare" α — the value before radiative corrections. The relationship between the bare α and the measured α(0) is given by the vacuum polarisation:

α(0)$^{-1}$ = α_bare$^{-1}$ - Δα_hadronic - Δα_leptonic

The hadronic contribution Δα_hadronic accounts for ~10% of the difference. A geometric derivation of α_bare would need to be compared to α(0) after subtracting radiative corrections, not directly.

### 9.4 Alternative Geometric Models

Several alternative geometric models of the electron exist and should be compared:

- **Burinskii's Kerr-Newman electron** [16]: The electron is modelled as a rotating black hole (Kerr-Newman solution) in the "naked singularity" regime where the gravitational and electromagnetic forces balance. α emerges as the dimensionless spin parameter a/m. This model has the advantage of being a solution of the Einstein-Maxwell equations — it is not an ad hoc construction but a general-relativistic prediction.
- **Hestenes' spacetime algebra** [11]: ZBW is the fundamental motion; the Dirac equation is a consequence, not the starting point. α is a free parameter in this framework.
- **Barut-Zanghi classical model** [10]: A classical spinning particle Lagrangian yields the Dirac equation upon quantisation. α remains an input.

The present proposal is compatible with all three: the helical null-curve is the geometric structure that underlies ZBW, regardless of whether the ZBW is treated as fundamental (Hestenes) or derived (Barut-Zanghi, Burinskii).

---

## 10. Conclusion: The Problem, Not the Solution

This paper does not derive the fine-structure constant. It poses a problem. The problem is this:

> **Does a classical light-speed helical null-curve in Minkowski space, subjected to curvature-torsion energy minimisation with periodicity and non-radiation constraints, have a unique stable pitch angle — and does that pitch angle equal arctan(α_obs)?**

If the answer is yes, a century-old mystery is resolved. If the answer is no, the helical model is wrong in detail but may still be right in spirit — the electron's internal structure is geometric, and α is a geometric invariant, even if the specific invariant is not what we have conjectured.

The value of posing the problem clearly — with falsifiability conditions, computational feasibility, and connection to existing theoretical frameworks — is that it invites solution. A well-posed problem attracts solvers. A century of α numerology has not yielded a derivation because the problem was never posed in mathematically precise, physically motivated, computationally tractable terms. This paper aims to remedy that.

---

## Declarations

**Funding:** This research received no specific grant from any funding agency.

**Conflicts of Interest:** The author declares no conflicts of interest.

**Ethics Approval:** Not applicable.

**Author Contributions:** Single author — all contributions.

**Data Availability:** No experimental data were generated or analysed.

**Code Availability:** Not applicable — this paper contains no computational code.

**Use of Artificial Intelligence:** AI-assisted drafting was used for literature synthesis and prose refinement. All mathematical content, arguments, and conclusions were verified by the human author.

---

## References

[1] Quni-Gudzinas, R.B. (2026). Fine-Structure Constant as a Cross-Ratio: A Geometric Reframing of α. Zenodo. DOI: 10.5281/zenodo.20108536.

[2] CODATA (2022). Recommended Values of the Fundamental Physical Constants.

[3] Eddington, A.S. (1946). *Fundamental Theory*. Cambridge University Press.

[4] Wyler, A. (1971). "L'espace symétrique du groupe des équations de Maxwell." *C. R. Acad. Sci. Paris*, 272, 186-188.

[5] Gilson, J.G. (1996). "Calculating the Fine-Structure Constant." *Physics Essays*, 9(2), 342-353.

[6] Baez, J. (2010). "How Many Fundamental Constants Are There?" *math.ucr.edu/home/baez/constants.html*.

[7] Dirac, P.A.M. (1928). "The Quantum Theory of the Electron." *Proc. R. Soc. Lond. A*, 117, 610-624.

[8] Schrödinger, E. (1930). "Über die kräftefreie Bewegung in der relativistischen Quantenmechanik." *Sitzungsber. Preuss. Akad. Wiss.*, 24, 418-428.

[9] Huang, K. (1952). "On the Zitterbewegung of the Dirac Electron." *Am. J. Phys.*, 20, 479-484.

[10] Barut, A.O. & Zanghi, N. (1984). "Classical Model of the Dirac Electron." *Phys. Rev. Lett.*, 52, 2009-2012.

[11] Hestenes, D. (1990). "The Zitterbewegung Interpretation of Quantum Mechanics." *Found. Phys.*, 20, 1213-1232.

[12] Obsidian note `_26199084040.md` (2026-07-18). "Numerical Gradients, Double Pendulum Bifurcation, and the α Threshold."

[13] Quni-Gudzinas, R.B. (2026). The Adelic Physics Program: Epistemological Foundations and Communications Framework. Zenodo. DOI: 10.5281/zenodo.21686727.

[14] Quni-Gudzinas, R.B. (2026). Zitterbewegung as a p-Adic Observable. Zenodo. DOI: 10.5281/zenodo.21335853.

[15] QNFO Research (2026). Ultrametric Engine: Deploying a 20-Principle p-Adic Discovery Worker. Zenodo. DOI: 10.5281/zenodo.21336105.

[16] Burinskii, A. (2008). "The Dirac-Kerr-Newman electron." *Grav. Cosmol.*, 14, 109-122.
