# Deep Research: Bayesian Cascade — α as Critical Eigenvalue of the Helical Null-Curve

**Project:** adelic-epistemological-foundations
**Paper:** P2 — α as Bifurcation Parameter
**Date:** 2026-07-29
**Status:** Phase 4 Complete

---

## Stage 0: Domain Assessment

The research question sits at the intersection of **three domains**:

1. **Physics (QED / classical electron theory):** α is the fine-structure constant, measured as ~1/137.036. In the Standard Model it is a free parameter. The claim that α is derivable rather than input is a direct challenge to a century-old assumption.

2. **Differential Geometry (space curves):** The helical null-curve in Minkowski space has constant curvature κ and torsion τ. The claim is that the ratio κ/τ (or its inverse) is constrained by a self-consistency condition (closure, stability against radiation, single-valuedness of the wavefunction in the rest frame).

3. **Bifurcation Theory (dynamical systems):** The electron's internal motion is treated as a light-speed helix parametrized by proper time. The pitch angle θ = arctan(α) marks a critical point separating three regimes: α = 0 (free non-interacting line), α finite (stable interacting helix), α → ∞ (confined circle, strong coupling). The claim is that α is the *unique* value at which the helix is stable against both radiative decay and gravitational/electromagnetic collapse.

**Key paradigms in play:**
- **Standard Model (free-parameter paradigm):** α is an input, determined by experiment, not derivable. Dominant.
- **Classical electron models (Lorentz-Abraham-Dirac, Poincaré stresses, Born-Infeld):** Attempted to derive α from self-consistency but failed due to runaways and pre-accelerations. Dormant.
- **Soliton / vortex models (Burinskii Kerr-Newman, Skyrme, Faddeev-Niemi):** Treat the electron as a topological defect in a field. α emerges as a topological invariant. Active but minority.
- **Projective geometry / cross-ratio (QNFO α-as-cross-ratio paper):** α is a projective invariant of two length scales — does not yet derive the value, only reframes it.

**Domain topology:** The field is dominated by the free-parameter paradigm (effective field theory, RG flow). Derivable-constant claims are treated as "numerology" unless they produce a testable prediction beyond the Standard Model.

---

## Stage 1: Paradigm-Shift Candidate Identification

### Candidate P1: α is a critical eigenvalue of a helical null-curve stability condition

- **Probability (prior):** 0.15 — low base rate for "derive fundamental constant" claims
- **Impact if true:** 9/10 — would be the first derivation of α, resolving a century-old open problem; would validate the adelic physics program's geometric foundation
- **Timeline:** 1-3 years for a computational stability analysis; 5-10 years for experimental confirmation
- **Testability:** 8/10 — the claim makes falsifiable predictions (see Stage 5 Calibration Register)
- **Dependency chain:** Requires formalising the helical null-curve as a variational problem; requires solving for stationary points of curvature-torsion energy functional; requires showing the stationary point at α ≈ 1/137 is a global minimum

### Candidate P2: α is a topological invariant (winding number) of the ZBW helix

- **Probability:** 0.10 — even lower base rate
- **Impact if true:** 8/10 — would connect α to topology but likely produce a rational number, not 1/137
- **Testability:** 6/10 — harder to measure topological invariants directly
- **Dependency chain:** Requires identifying the topological charge (Chern number, winding number, linking number) that equals α⁻¹

### Candidate P3: α is NOT derivable — it is a genuine free parameter

- **Probability (prior):** 0.75 — dominant paradigm
- **Impact if false (for the program):** 2/10 — the adelic program does not depend on α being derivable; the cross-ratio reframing is sufficient
- **Testability:** 0/10 — unfalsifiable null hypothesis

### EV Ranking

| Candidate | P(H) | Impact | EV_raw | Calibrated P(H) | Calibrated EV |
|:----------|:-----|:-------|:-------|:----------------|:-------------|
| P1 (α is eigenvalue) | 0.15 | 9 | 1.35 | 0.12 (adjusted) | 1.08 |
| P2 (α is topological) | 0.10 | 8 | 0.80 | 0.08 | 0.64 |
| P3 (α is free parameter) | 0.75 | — | — | 0.80 | — |

**P1 is the highest-EV candidate.** Even at calibrated probability 0.12, the impact of deriving α (9/10) justifies investigation.

---

## Stage 2: Assumption Audit

### Enabling Assumptions Table for P1

| # | Assumption | Raw P(E\|H) | Calibration Anchor | Calibrated P | Confidence |
|:--|:-----------|:------------|:-------------------|:-------------|:-----------|
| A1 | The electron's internal motion can be modelled as a classical light-speed helical null-curve in Minkowski space | 0.80 | Empirical Base Rate: ZBW is a well-established consequence of the Dirac equation; the velocity operator eigenvalues are ±c. Reference: Dirac (1928), Schrödinger (1930), Huang (1952). The helical interpretation is standard in the ZBW literature. | 0.75 | High |
| A2 | A variational principle exists for the curvature-torsion balance of a null curve | 0.65 | Reference Class: Euler elastica (curvature energy functional), Kirchhoff rod theory, and relativistic string/Nambu-Goto action all have well-established variational formulations. Extending to null curves with torsion is mathematically novel but not forbidden. [CALIBRATION-CAP: no direct empirical pillar for null-curve variational principle] | 0.65 | Medium |
| A3 | The stationary point of the curvature-torsion functional corresponds to α ≈ 1/137 | 0.30 | Reference Class: Historical attempts to derive α (Eddington's 1/137 numerology, Wyler's formula, Gilson's model, etc.) have a ~0% success rate. The reference class is "derivations of fundamental constants" and the base rate is near zero. Adjusted: P(E\|H) capped at 0.30. | 0.25 | Low |
| A4 | The stationary point is a stable minimum (not a saddle or maximum) | 0.70 | Empirical Base Rate: In physical systems, self-consistent equilibria are typically minima of the relevant free energy (second law of thermodynamics). A saddle point would be unstable under perturbation. [CALIBRATION-CAP: no empirical pillar for this specific system] | 0.65 | Medium |
| A5 | The muon and tau lepton mass ratios (~207, ~3477) are distinct topological winding numbers of the same helical structure | 0.40 | Reference Class: The lepton mass hierarchy has resisted explanation for decades. Models that explain one mass but not the spectrum have a ~100% failure rate. Capped at 0.40. | 0.35 | Low |
| A6 | The derivation of α produces a testable prediction beyond the Standard Model | 0.55 | Empirical Base Rate: Derivations of fundamental constants that ALSO produce novel predictions have a moderate track record (e.g., the BCS theory's prediction of the energy gap from a microscopic model). But most "derivations" are post-hoc. | 0.50 | Medium |

### Blocking Assumptions
- **B1:** The null-curve variational principle may not exist — there may be no well-defined energy functional for a light-speed helical curve that is both Lorentz-invariant and yields a finite result.
- **B2:** α is known to run with energy scale (RG flow). The low-energy value α(0) ≈ 1/137 is an infrared fixed point, not a fundamental constant. A geometric derivation at the Compton scale must reconcile with running.
- **B3:** Quantum corrections may destabilise the classical helical solution — the classical stability may not survive quantisation.

### Dependency Chain
```
A1 (helix model exists) 
  → A2 (variational principle exists) 
    → A3 (stationary point matches α) 
      → A4 (stable minimum) 
        → A6 (produces testable prediction)
A5 (lepton spectrum) is independent but synergistic
```

If A1 fails, the entire cascade collapses. If A1 passes but A2 fails, the program is blocked at the formalism stage. If A1-A2 pass but A3 fails, P1 is falsified but P2 may survive.

---

## Stage 3: Red-Team Adversarial Challenge

### Challenger 1: Null-Hypothesis Defender
"α is a free parameter in the Standard Model. The RG flow shows it runs with energy. No derivation of α has ever succeeded. The cross-ratio reframing (α = CR(r_e, λ_C; 0, ∞)) is elegant but merely restates the definition — r_e and λ_C are both proportional to α, so the reframing is circular. Eddington, Dirac, Wyler, and dozens of others have claimed to derive α. All failed. The base rate is zero."

**Response:** The cross-ratio reframing is not circular — it reveals projective invariance that the standard definition conceals. The difference from prior failed attempts is that this derivation is *geometric*, not numerological — it proposes a specific dynamical mechanism (curvature-torsion balance) with falsifiable predictions, rather than a magic formula.

### Challenger 2: Methodology Skeptic
"The helical null-curve is a classical model. The electron is a quantum object. Quantising the model may destroy the stability. The Dirac equation already contains ZBW — why does a classical geometric model add anything beyond what the Dirac equation already says? The Dirac equation gives α as an input; the helix model claims to output it. That is a qualitative leap, not a refinement."

**Response:** The classical geometric model and the Dirac equation address different questions. The Dirac equation tells us *that* ZBW happens; the helical model asks *why* the coupling constant takes the value it does. Classical geometric models often yield insights that survive quantisation (e.g., the Bohr model → quantum hydrogen). The claim is that α is a *semiclassical* eigenvalue — the quantisation may shift it but not destroy the qualitative structure.

### Challenger 3: Better-Alternative Proposer
"The renormalisation group already explains α: it's an infrared fixed point of QED. The value 1/137 is not fundamental — it's the low-energy limit of a running coupling. At the Planck scale, α may be completely different. A geometric derivation at the Compton scale is solving the wrong problem."

**Response:** The RG explains *how* α changes with scale, not *why* it has the specific infrared value it does. A fixed point still needs its value explained. The helical model proposes that the infrared fixed point is a geometric consequence of the electron's structure at the Compton scale — the RG flow *converges* to α ≈ 1/137 because that's the unique stable pitch.

### Challenger 4: Scaling Pessimist
"Even if the helical model is correct, deriving α requires solving a nonlinear variational problem for a null curve in Minkowski space. This is mathematically formidable — it may require new techniques in global differential geometry. No one has solved it in 50 years (the ZBW has been known since 1930). What's different now?"

**Response:** What's different is: (a) the adelic framework provides new mathematical tools (Bruhat-Tits buildings, p-adic parametrisations); (b) computational power enables numerical stability analysis that was impossible in 1930; (c) the cross-ratio reframing reduces the problem from "derive a number" to "find the stationary point of a geometric functional" — a well-posed variational problem.

### Challenger 5: Resource Realist
"To properly investigate this, you'd need: a postdoc in differential geometry, a computational physicist for numerical stability analysis, and access to a cluster for parameter sweeps. This is a 3-5 year project requiring ~$500K in funding. The QNFO program has no institutional funding. This is a paper, not a research programme."

**Response:** The paper's contribution is to *pose the variational problem precisely* and *identify the falsifiability conditions*. Whether anyone solves it is a separate question. A well-posed problem with clear falsifiability conditions is itself a contribution — it invites others to solve it. The paper is a *proposal*, not a *solution*.

---

## Stage 4: Likelihood-Span Sensitivity Analysis

### Span Definitions

| Assumption | Calibrated Value | Lower Bound | Upper Bound | Span Source |
|:-----------|:-----------------|:------------|:------------|:------------|
| A1 | 0.75 | 0.50 | 0.90 | Reference class: ZBW literature consensus |
| A2 | 0.65 | 0.40 | 0.80 | [CALIBRATION-CAP]: broad span |
| A3 | 0.25 | 0.10 | 0.40 | Reference class: historical α derivations |
| A4 | 0.65 | 0.40 | 0.80 | [CALIBRATION-CAP] |
| A5 | 0.35 | 0.15 | 0.55 | [CALIBRATION-CAP] |
| A6 | 0.50 | 0.30 | 0.70 | [CALIBRATION-CAP] |

### EV Sensitivity

For P1 (α is eigenvalue), the overall P(H) = joint probability of A1-A4 (the cascade). Under independent assumptions:

| Scenario | A1 | A2 | A3 | A4 | P(H) | EV (impact=9) |
|:---------|:---|:---|:---|:---|:-----|:-------------|
| Calibrated (baseline) | 0.75 | 0.65 | 0.25 | 0.65 | 0.079 | 0.71 |
| Optimistic (all upper) | 0.90 | 0.80 | 0.40 | 0.80 | 0.230 | 2.07 |
| Pessimistic (all lower) | 0.50 | 0.40 | 0.10 | 0.40 | 0.008 | 0.07 |

**Key finding:** The EV range is [0.07, 2.07]. The pessimistic scenario (0.07) is below the threshold for resource allocation under a strict Kelly criterion. The optimistic scenario (2.07) justifies investigation. The baseline (0.71) is marginal — it justifies a *paper* (low cost) but not a *research programme* (high cost).

### Halve-Priors Stress Test

Cutting all optimistic priors by 50%: A1=0.38, A2=0.33, A3=0.13, A4=0.33 → P(H) = 0.0054 → EV = 0.05. **This is below any reasonable investigation threshold.** The cascading effect of multiple low-probability assumptions means P1 is extremely fragile to prior reduction.

### Correlation Stress Test

If A1 and A2 are correlated (both depend on the existence of a well-defined classical model), the pessimistic scenario is more likely than independence assumes. If A1 fails (helix model is invalid), A2-A6 are moot. This suggests a **two-gate strategy**: test A1 first (low cost: literature review), then decide whether to proceed.

---

## Stage 5: Calibration Register

| Prediction | Likelihood Anchor | Strength | Post-hoc Risk |
|:-----------|:------------------|:---------|:--------------|
| [CHECK: 2035] α ≈ 1/137 is derived from a geometric stability condition by a published peer-reviewed paper | Reference Class: 0% historical success rate for α derivations | [STRONG] | "We never claimed the derivation would happen by 2035 — we only said it was *possible*." |
| [CHECK: 2028] A null-curve variational principle yielding a finite stationary point is published | Calibrated Subjective (A2: 0.65) | [WEAK] | "We only claimed the problem was *well-posed*, not that someone would solve it." |
| [CHECK: 2030] The muon mass ratio (207) is derived as a topological winding number distinct from the electron's | Calibrated Subjective (A5: 0.35) | [WEAK] | "The topological model is speculative — we never claimed high confidence." |
| [CHECK: 2028] Numerical stability analysis of the classical helical null-curve identifies a unique stable pitch angle | Calibrated Subjective (A4: 0.65) | [WEAK] | "Numerical analysis is preliminary — analytic proof is still needed." |
| [CHECK: 2040] α is experimentally shown NOT to be a free parameter — it is invariant under any consistent UV completion | Empirical Base Rate: no such claim has ever been verified | [STRONG] | "The experimental programme was never funded — the null result proves nothing." |

---

## Stage 6: Optimal Portfolio Allocation

Given the marginal EV (0.71 baseline) and the fragility to prior reduction (EV → 0.05 under halve-priors), the optimal allocation is:

1. **P1 (α as eigenvalue): 30% allocation** — write the paper *posing the variational problem*, not claiming to have solved it. Low-cost, high-upside if the problem attracts attention.
2. **P2 (α as topological invariant): 15% allocation** — fold into P1 as a "topological interpretation" section.
3. **P3 (null hypothesis): 55% allocation** — the paper must be honest that the null hypothesis (α is a free parameter) is the dominant position and the presented framework is a *proposal*, not a result.

### Justification
The paper's contribution is not to *prove* that α is derivable, but to:
1. Pose the helical stability problem in precise mathematical terms
2. Provide falsifiability conditions
3. Connect the problem to the adelic physics program and continuum critique
4. Survey prior attempts and explain why the helical approach differs

This is a **theory proposal paper**, not a **derivation paper**. The distinction is crucial for plagiarism/fabrication avoidance: we are not claiming to have solved the problem, only to have identified it.

---

## Stage 7: Strategic Memo

**Title:** "α as Bifurcation Parameter: The Helical Electron Stability Problem"

**Executive Summary:** The fine-structure constant α ≈ 1/137.036 has resisted derivation for a century. We propose that α is a critical eigenvalue of a helical null-curve stability condition in Minkowski space. The electron's Zitterbewegung — the oscillatory motion at the Compton frequency predicted by the Dirac equation — is reinterpreted as a classical light-speed helical null-curve with curvature κ and torsion τ. The pitch angle θ = arctan(α) separates three qualitative regimes: α = 0 (free, non-interacting line), α finite (stable, charge-bearing helix), α → ∞ (confined, infinite-coupling circle). The actual value α ≈ 1/137 is hypothesised to be the unique stationary point of a curvature-torsion energy functional — a geometric fixed point rather than a free parameter. This paper does not solve the stability problem; it poses it in precise mathematical terms and provides specific falsifiability conditions. The cross-ratio reframing α = CR(r_e, λ_C; 0, ∞) (Quni-Gudzinas, 2026) provides the projective-geometric foundation. The adelic physics program provides the number-theoretic context: if ℚ is the physical base field, then coupling constants are not continuous parameters but discrete geometric invariants.

**Recommendations:**
1. Publish as a "problem proposal" paper — transparent about its speculative nature
2. Include the full Bayesian cascade in an appendix or supplementary material
3. Provide falsifiability conditions with dated calibration register entries
4. Target audience: physicists interested in fundamental constants, geometers interested in null-curve variational problems, and philosophers of physics interested in the free-parameter vs. derived-constant debate

---

## Stage 8: Adversarial Review (REVIEWER subagent deployment skipped — single-agent session)

**Self-review against red-team challenges:**

1. The paper must NOT claim to have derived α — it must claim only to have posed the problem.
2. The Bayesian cascade in Appendix A provides the necessary epistemic humility.
3. The cross-ratio reframing from the existing QNFO paper is the foundation — no circularity.
4. The falsifiability conditions (§8) are specific, dated, and strength-tagged.
5. The RG running of α must be addressed explicitly — the claim is that the infrared fixed point is geometric in origin, not that α is scale-independent.

**Verdict:** The paper is publishable as a **theory proposal** with clear [SPECULATIVE] and [UNTESTED] labels throughout. It must not be presented as a solved problem.

---

## Bibliography (Deep Research)

- Dirac, P.A.M. (1928). The Quantum Theory of the Electron. *Proc. R. Soc. Lond. A*, 117, 610-624.
- Schrödinger, E. (1930). Über die kräftefreie Bewegung in der relativistischen Quantenmechanik. *Sitzungsber. Preuss. Akad. Wiss.*, 24, 418-428.
- Huang, K. (1952). On the Zitterbewegung of the Dirac Electron. *Am. J. Phys.*, 20, 479-484.
- Barut, A.O. & Zanghi, N. (1984). Classical Model of the Dirac Electron. *Phys. Rev. Lett.*, 52, 2009-2012.
- Burinskii, A. (2008). The Dirac-Kerr-Newman electron. *Grav. Cosmol.*, 14, 109-122.
- Hestenes, D. (1990). The Zitterbewegung Interpretation of Quantum Mechanics. *Found. Phys.*, 20, 1213-1232.
- Eddington, A.S. (1946). *Fundamental Theory*. Cambridge University Press. [HISTORICAL: failed attempt at deriving α]
- Quni-Gudzinas, R.B. (2026). Fine-Structure Constant as a Cross-Ratio. Zenodo. DOI: 10.5281/zenodo.20108536.
- Quni-Gudzinas, R.B. (2026). Zitterbewegung as a p-Adic Observable. Zenodo. DOI: 10.5281/zenodo.21335853.
