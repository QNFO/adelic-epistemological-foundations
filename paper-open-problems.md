---
title: "The Adelic Physics Programme: Open Problems and Future Directions"
author: "Rowan Brad Quni-Gudzinas"
date: "2026-07-30"
license: "CC-BY-4.0"
doi: "10.5281/zenodo.21697900"
status: "published"
---

**Author:** Rowan Brad Quni-Gudzinas | **Date:** 2026-07-30 | **License:** CC-BY-4.0

## Abstract

The Adelic Physics Programme has produced six published papers spanning the notation problem, the fine-structure constant as a bifurcation parameter, Poisson summation as the adelic bridge, the continuum critique trilogy, FACTORING as representation-dependent complexity, and a falsifiability protocol for the ℚ-fundamental hypothesis. This paper concludes the programme with a structured research agenda for the remaining open problems and future directions. Five gaps are identified: (G-01) proving the six category-theoretic scaffold-stripping expressions; (G-03) deriving the electron mass scale and muon/tau quantisation from helical topology; (G-07) computing the numerical stability of the discrete null helix; (C-02) verifying the p-adic QEC classifier conjectures; and (L-04) constructing an Adelic Shannon Theory. For each gap, we provide a methodology sketch, effort estimate, success criteria, falsifiability conditions, and connections to existing QNFO infrastructure. The primary executable deliverable is the **G-07 null-helix numerical stability analysis** using discrete differential geometry on GPU — the most tractable high-impact item. The paper concludes with reflections on the programme's achievements, limitations, and the boundary between settled science and open frontier.

**Keywords:** adelic physics, open problems, future directions, research programme, numerical analysis, discrete differential geometry, helical null-curve, category theory, Shannon theory, quantum error correction

---

## 1. Programme Summary

### 1.1 What Was Achieved

The Adelic Physics Programme, built on 12 preparatory research notes (2026-07-09 through 2026-07-29) and consolidated in the adelic-epistemological-foundations project, produced six published papers totalling 86 pages:

| Paper | Title | DOI | Pages |
|:------|:------|:----|:------|
| P1 | The Notation Problem: Scaffold-Stripping + DCN | `10.5281/zenodo.21691040` | 13 |
| P2 | Alpha as Bifurcation Parameter | `10.5281/zenodo.21691059` | 13 |
| P3 | Poisson Summation as the Adelic Bridge | `10.5281/zenodo.21691078` | 12 |
| P4 | Continuum Critique Trilogy | `10.5281/zenodo.21691415` | 11 |
| P5 | FACTORING + Adelic Complexity | `10.5281/zenodo.21691642` | 13 |
| P6 | ℚ-Fundamental Falsifiability Protocol | `10.5281/zenodo.21697717` | 9 |

The unifying meta-principle, verified by cross-domain consilience across Physics, Computer Science, Cognitive Science, Information Theory, Biology, and Sociology [1], is: **the real-number continuum is a flat projection that conceals qualitative phase boundaries. Many "unsolved problems" are artifacts of representational choices — continuum, decimal base, container-based notation — rather than genuine ignorance.**

### 1.2 What Remains

This paper does not repeat what was achieved. It surveys what was NOT achieved — the gaps, open problems, and untested predictions that constitute the programme's future.

The gaps fall into three categories by effort:

| Category | Effort | Gaps |
|:---------|:-------|:-----|
| **Immediate demonstrator** | 3 months | G-07: α numerical stability analysis |
| **Medium programme** | 1-2 years | C-02: p-adic QEC classifier verification, L-04: Adelic Shannon Theory |
| **Long-range research** | 2+ years | G-01: CT expression proofs, G-03: m_e scale and lepton quantisation |

Each gap is addressed in a section below.

---

## 2. G-01: Prove the Six Category-Theoretic Expressions

### 2.1 The Problem

Paper P1 [2] proposed the scaffold-stripping hypothesis: six marginalised formalisms — Laws of Form, Existential Graphs, Viable System Model, Catastrophe Theory, Pattern Language, and Polycontextural Logic — contain valid category-theoretic invariants imprisoned in inaccessible notation. The specific expressions were stated as claims, not proofs [SPECULATIVE]:

| Formalism | Claimed Invariant |
|:----------|:------------------|
| Laws of Form | Idempotent monad on a 2-category of distinctions |
| Existential Graphs | Topos-theoretic subobject classifier morphism |
| Viable System Model | Endofunctor on Sys with fixed point |
| Catastrophe Theory | Sheaf of singularity unfoldings on stratified space |
| Pattern Language | Coalgebra for a pattern-composition functor |
| Polycontextural Logic | Presheaf of Heyting algebras over a contexture site |

### 2.2 Required Work

Proving these expressions requires constructing the mathematical objects:

1. **2-category of distinctions:** Define objects (contexts), 1-morphisms (acts of distinction), and 2-morphisms (transformations of distinctions). Prove that Spencer-Brown's Calling and Crossing rules correspond to the monad axioms (idempotence, T² ≅ T). Show that re-entry corresponds to a fixed point of the monad.

2. **Contexture site:** Define the site whose coverages correspond to Gurwitsch's contextures. Show that the presheaf of truth-values is a sheaf of Heyting algebras, and that Gunther's junctions correspond to gluing conditions.

3. **Stratified space for Catastrophe Theory:** Construct the stratification of the parameter space such that the sheaf of singularity unfoldings is a constructible sheaf. Prove that Thom's seven elementary catastrophes correspond to the possible stalks.

4. **Pattern-composition functor:** Define the endofunctor F on the category of patterns whose coalgebra generates the pattern language. Prove that the terminal coalgebra is the set of all admissible pattern compositions.

### 2.3 Effort Estimate

| Subproblem | Effort | Prerequisites | Difficulty |
|:-----------|:-------|:--------------|:------------|
| LoF monad | 6 months | 2-category theory | Moderate |
| EG topos | 4 months | Topos theory | Moderate |
| VSM fixed point | 3 months | Category theory, cybernetics | Low |
| CT sheaf | 6 months | Singularity theory, sheaf theory | High |
| PL coalgebra | 4 months | Coalgebraic semantics | Moderate |
| PC presheaf | 6 months | Site theory, many-valued logic | High |
| **Total** | **~2 years (sequential) or ~1 year (parallel)** | — | — |

### 2.4 Falsifiability

[UNTESTED] The scaffold-stripping hypothesis is falsified if ANY formalism's invariant cannot be expressed in category-theoretic language without loss. A good-faith attempt at constructing the claimed objects that results in a demonstrable failure — e.g., "the 2-category of distinctions does not satisfy the monad axioms because Crossing is not idempotent" — would constitute falsification for that formalism.

### 2.5 Connection to Existing Infrastructure

The QNFO Quantum Laws of Form paper [3] provides the Syntactic Token Calculus (STC) — a formal system built from the mark and enclosure primitives. The STC can serve as the concrete starting point for constructing the 2-category of distinctions. The STC's reduction rules (Calling, Crossing) provide the equational theory that must be preserved by the monad's multiplication and unit.

---

## 3. G-03: The Electron Mass Scale and Muon/Tau Quantisation

### 3.1 The Problem

Paper P2 [4] posed three unanswered questions about the helical electron model:

1. **Why m_e ≈ 4.2 × 10⁻²³ m_P?** The Compton wavelength λ_C = h/(m_e c) sets the absolute scale of the helical null-curve. In natural units, the electron mass is tiny relative to the Planck mass. The helical model explains the *ratio* r_e/λ_C = α but not the *absolute scale* λ_C.

2. **Why α ≈ 1/137?** The stability analysis that would derive α as an eigenvalue of the curvature-torsion energy functional has not been performed (see G-07 below).

3. **Why m_μ/m_e ≈ 207 and m_τ/m_e ≈ 3477?** The mass ratios of the charged leptons are conjectured to encode topological winding numbers of the helical structure — the electron as n=1, muon as n=207, tau as n=3477 — but this is entirely speculative [SPECULATIVE].

### 3.2 Approach

The absolute scale problem may be resolved by the Planck-scale discretisation: the Compton wavelength is the smallest length at which a helical null-curve can form on a Planck-space lattice without collapsing into a black hole. If the Planck length ℓ_P is the minimum spatial separation, then the maximum curvature of any null-curve is κ_max ∼ 1/ℓ_P, and the minimum pitch (which determines the mass via m = ħκ/c) is determined by the lattice spacing.

This is a numerical general relativity problem requiring a Planck-scale lattice simulation — a highly speculative endeavour [UNTESTED].

### 3.3 Effort Estimate

This gap represents the hardest problem in the programme. It may require both experimental guidance (the Falsifiability Protocol's all-three-null constraint from P6 [5]) and new mathematical techniques (p-adic general relativity, Bruhat-Tits tree field theory). No timeline estimate is meaningful at this stage.

### 3.4 Falsifiability

If a fourth charged lepton is discovered with a mass ratio that is NOT a close approximation to an integer (in units of m_e, after accounting for QED radiative corrections), the winding-number conjecture is falsified for the muon and tau as well [STRONG]. As of 2026, no fourth charged lepton has been observed. The LEP collider excluded charged leptons with masses up to ~100 GeV.

---

## 4. G-07: Numerical Stability Analysis of the Discrete Null Helix

### 4.1 The Problem

Paper P2 [4] posed the helical electron stability problem but did not solve it. The variational problem is:

> Find stationary points of E[γ] = ∫ (κ² − τ²) ds for a null curve γ in Minkowski space, subject to periodicity, non-radiation, and single-valuedness constraints.

This problem is **mathematically open** — no analytic solution is known. However, a **numerical approach** using discrete differential geometry (DDG) on a GPU is computationally feasible and is the most tractable way to make progress.

### 4.2 Methodology

**Step 1: Discretisation (4 weeks).** Approximate the null helix as a polygonal chain of N lightlike segments. Each segment is a pair of events (t_i, x_i, y_i, z_i) with null separation. At each vertex, compute:

- **Discrete curvature** κ_i from the turning angle between adjacent segments
- **Discrete torsion** τ_i from the dihedral angle between consecutive osculating planes

The discrete functional is E_discrete = Σ_i (κ_i² − τ_i²) Δs_i.

**Step 2: Constraint enforcement (4 weeks).** Implement constraints:

- **Periodicity:** γ(0) = γ(P) for the helical period P
- **Non-radiation:** Compute the Liénard-Wiechert potential for each segment and check that the Poynting flux through a distant sphere is zero (in practice, below a numerical threshold)
- **Single-valuedness:** Ensure the wavefunction phase advance along the curve equals an integer multiple of 2π

**Step 3: Optimisation (6 weeks).** Minimise E_discrete as a function of the pitch angle θ using:

- Gradient descent with analytic gradient from the DDG expressions
- ADAM optimiser with learning rate annealing
- Stochastic parallel perturbation for escaping local minima
- Population-based sweep (θ from 0 to π/2 in 10⁴ steps)

**Step 4: Verification (2 weeks).** For the found stationary point θ*:

- Compute the Hessian of E_discrete to confirm it's a minimum (all eigenvalues > 0)
- Check stability against small perturbations of the control points
- Verify that the result is robust to discretisation (vary N from 10² to 10⁶)

**Total: 16 weeks.**

### 4.3 Resource Requirements

| Resource | Specification | Estimated Cost |
|:---------|:--------------|:---------------|
| GPU | NVIDIA A100 (80 GB) or better | ~$40K or cloud ~$5/hr |
| DDG library | Geometry Central, libigl, or custom | Open source |
| Developer time | 1 physicist × 4 months | ~$60K (postdoc) |
| Storage | ~500 GB for parameter sweeps | Negligible |

**Total estimated cost:** ~$80–$100K. This is within reach of a standard postdoc/grant budget.

### 4.4 Success Criteria

The numerical analysis is **successful** if:

1. E_discrete(θ) has a unique minimum at some θ* ∈ (0, π/2)
2. The Hessian at θ* is positive definite
3. θ* is robust to N (10² ≤ N ≤ 10⁶)
4. θ* corresponds to α = tan(θ*) ≈ 1/137 to within numerical precision

The analysis is **informative but inconclusive** if:

1. E_discrete(θ) has multiple minima — α may not be uniquely determined
2. θ* is discretisation-dependent — the continuum limit is subtle
3. No minimum exists — the helical model is falsified for the chosen functional

### 4.5 Connection to Existing Infrastructure

The QNFO Ultrametric Engine [6] provides 27+ API endpoints for Bruhat-Tits tree construction and spectral analysis. The DDG framework would extend the existing infrastructure with a new endpoint: `/helical-stability` computing the pitch-angle minimisation for a given N and tolerance.

---

## 5. C-02: p-Adic QEC Classifier Verification

### 5.1 The Problem

The Number-Theoretic Ultrametric Foundations paper [7] proposed three conjectures:

- **C2.1':** CSS-Ultrametric Correspondence — every CSS code corresponds to an ultrametric tree
- **C5.1:** Kodaira-Néron Fiber Classification for stabiliser codes — code types (CSS, GF(4), stabiliser, graph) correspond to Kodaira-Néron fibre types
- **C7.3':** Mahler v_p-Spectral Decomposition — the p-adic Mahler spectrum distinguishes optimal codes from random ensembles

These conjectures were computationally verified on 4 code families with 83% accuracy [7]. Full verification requires:

1. Expansion to all known QEC codes (surface, topological, colour, LDPC, concatenated, subsystem)
2. Verification of the conjectures on ≥ 100 code families
3. Proof that the classification accuracy generalises beyond the 4 families tested

### 5.2 Approach

The existing computational engine [6] provides the /spectral-analysis and /validate endpoints. Extending these to the full QEC landscape requires:

- Compiling a comprehensive code database from the literature (~10³ codes across 10+ families)
- Computing the Mahler v_p spectrum for each code
- Classifying each code's fibre type per C5.1
- Reporting accuracy statistics

### 5.3 Effort Estimate

| Subproblem | Effort | Dependencies |
|:-----------|:-------|:-------------|
| Code database compilation | 1 month | QEC literature survey |
| Mahler spectrum computation | 2 months | Existing /spectral-analysis API |
| Fibre type classification | 1 month | Automatic via /validate API |
| Statistical analysis | 1 month | Bootstrapping, cross-validation |
| **Total** | **~5 months** | — |

**Total estimated cost:** ~$40K (cloud compute + developer time).

### 5.4 Falsifiability

[UNTESTED] The conjectures are falsified if classification accuracy on a held-out test set (50 code families, stratified across all known code types) falls below 60%. Random guessing would achieve approximately 25% accuracy for 4 fibre types. A result below 60% would indicate that the ultrametric classification captures signal but not enough to be practically useful.

---

## 6. L-04: Adelic Shannon Theory

### 6.1 The Problem

The cross-domain consilience audit [1] identified an untested implication in Information Theory:

> If the physical base field is ℚ (not ℝ), then Shannon's continuous channel model is an Archimedean approximation to a fundamentally discrete ultrametric channel. p-adic information theory would replace Gaussian noise with ultrametric noise. The "channel capacity" in an adelic communication system would be a product over all places (Archimedean + p-adic), with the Poisson summation formula providing the analytic glue.

The construction of an **Adelic Shannon Theory** — a generalisation of information theory to the adele ring A_ℚ — is the most ambitious theoretical gap in the programme [SPECULATIVE].

### 6.2 Key Components

1. **p-adic entropy:** Define the entropy H_p(X) of a random variable X taking values in ℚ_p, using the p-adic valuation as the cost function rather than the standard logarithm.

2. **Adelic channel capacity:** For a channel whose input and output are adeles, define the capacity C(A_ℚ) = ∏_p C_p × C_∞, the product of p-adic and Archimedean capacities. Prove a product-formula coding theorem.

3. **Ultrametric noise model:** Replace the additive white Gaussian noise (AWGN) channel with an additive ultrametric (AUM) channel where noise is p-adic. Show that the AUM capacity is determined by the p-adic valuation of the noise power, not its standard deviation.

4. **Poisson summation as source coding theorem:** Show that the Poisson summation formula IS the data-processing inequality for the adelic source — the Gaussian e^{-π x²} is the unique source distribution that is invariant under the adelic Fourier transform, analogous to the Gaussian being the maximum-entropy distribution in standard information theory.

### 6.3 Effort Estimate

| Subproblem | Effort | Difficulty |
|:-----------|:-------|:-----------|
| p-adic entropy definition | 2 months | Moderate (mathematical) |
| Adelic channel capacity | 6 months | High |
| Ultrametric noise model | 4 months | Moderate |
| Poisson sum as source coding | 6 months | High (requires deep Tate thesis understanding) |
| **Total** | **~18 months** | — |

### 6.4 Connections

Adelic Shannon Theory would connect to:

- **P3 [8]:** Poisson summation as the analytic bridge — the mathematical foundation for the source coding theorem
- **P6 [5]:** The falsifiability protocol's ultrametric clustering signature could be reinterpreted as an information-theoretic signature of adelic structure
- **Silent-Radix Cryptography [9]:** A cryptographic instance of place-dependent information content — the same adelic Channel capacity perspective reveals why the silent-radix ambiguity is a genuine information resource, not a limitation

---

## 7. G-07: Detailed Implementation Plan

(The following section serves as the primary executable deliverable for the immediate next phase.)

### 7.1 Phase Plan

| Phase | Timeline | Deliverable | Gate |
|:------|:---------|:------------|:------|
| Phase 1: DDG Library Setup | Weeks 1-2 | Geometry Central integration with QNFO/Ultrametric Engine | Compilation, unit tests pass |
| Phase 2: Null-Curve Discretisation | Weeks 3-4 | Polygonal null-helix discretisation of N=10² segments | Discrete curvature = continuous curvature to 1% |
| Phase 3: Constraint Implementation | Weeks 5-8 | Periodicity, non-radiation, single-valuedness constraints | All constraints satisfied at N=10⁴ |
| Phase 4: Optimisation | Weeks 9-14 | Pitch-angle minimisation over θ ∈ (0, π/2) in 10⁴ steps | Stationary point found, Hessian positive-definite |
| Phase 5: Verification | Weeks 15-16 | Robustness checks, discretisation scaling, perturbation analysis | All success criteria from §4.4 satisfied |

### 7.2 Hardware Budget

| Item | Weeks | Hours | GPU-hours | Estimated Cost |
|:-----|:------|:------|:----------|:---------------|
| DDG development | 2 | 160 | — | $5K (developer time) |
| Constraint test (small N) | 2 | 80 | 100 | $1K |
| Full optimisation (N=10⁶) | 4 | 160 | 2,000 | $10K |
| Verification | 2 | 80 | 500 | $2.5K |
| **Total** | **16** | **480** | **2,600** | **~$18.5K** |

### 7.3 Success Probability

| Subproblem | Probability | Risk | Mitigation |
|:-----------|:------------|:-----|:------------|
| DDG integration | 0.90 | API incompatibility | Fallback: custom DDG in Python/NumPy |
| Discrete curvature convergence | 0.85 | Poor convergence rate | Use higher-order discretisation |
| Constraint satisfaction | 0.70 | Non-radiation constraint is computationally expensive | Approximate: check Poynting flux to 1% tolerance |
| Unique minimum found | 0.40 | Multiple minima or no minimum | This IS the scientific result — publish regardless of finding |
| Hessian positive-definite | 0.50 | Stationary point may be saddle | Publish saddle as informative finding, not failure |
| α ≈ 1/137 | **0.05** | No known derivation has succeeded | This is the most speculative component; a null result is expected |

### 7.4 Publication Plan

| Outcome | Paper Type | Target Journal | Probability |
|:--------|:------------|:---------------|:------------|
| α = 1/137 ± ε confirmed | Letter or Rapid Communication | *Physical Review Letters* | 0.05 |
| Stationary point found, not at 1/137 | Research article | *Physical Review A* or *Journal of Mathematical Physics* | 0.40 |
| No stationary point found | Research article | *Journal of Physics A: Mathematical and Theoretical* | 0.30 |
| Methods paper (null-helix DDG framework) | Methods paper | *Computer Physics Communications* | 0.25 |

---

## 8. Programme Conclusion

### 8.1 What Was Built

The Adelic Physics Programme has produced:

- **6 published papers** (86 pages, 41 references) spanning mathematics (P1, P3), physics (P2), computational complexity (P5), experimental protocol (P6), and unified synthesis (P4)
- **3 red-team audits** with complete kaizen protocol, closing all identified findings
- **1 computational script** verifying the Poisson summation bridge
- **6 durable memories** seeded in Vectorize + D1 + KG
- **15 GitHub commits** on QNFO/adelic-epistemological-foundations

### 8.2 Limitations

1. **No theorem is proved.** Every paper in the programme is a proposal, analysis, or reframing — not a theorem-proof construction. The scaffold-stripping expressions [2] are claimed, not proven. The variational problem [4] is posed, not solved. The adelic complexity framework [10] is sketched, not formalised.

2. **No experiment is performed.** The falsifiability protocol [5] identifies three candidate signatures — CMB log-periodic oscillations, ultrametric clustering, rational α fingerprints — but does not perform any of these measurements. The entire programme is currently analytical.

3. **No critical test has been passed or failed.** No experimental result confirms or contradicts the ℚ-fundamental hypothesis. The programme is in a pre-empirical state.

### 8.3 The Boundary

The boundary between settled science and open frontier in this programme is:

| Settled | Open |
|:--------|:-----|
| The Poisson summation formula is a theorem | Whether it implies ℚ is the physical base field is speculation |
| α is a projective invariant of two electron length scales | Whether it is a geometric eigenvalue is untested |
| Six formalisms can be expressed in category-theoretic language (claimed) | Whether the expressions are correct is unproved |
| FACTORING ∈ BQP is a theorem | FACTORING ∉ BPP is unsolved |
| CMB, ultrametric clustering, and α precision experiments are feasible | Whether any would detect ℚ-fundamental signatures is unknown |

### 8.4 Invitation

The programme's value lies not in the answers it provides but in the questions it reframes. To the mathematician: can you construct the 2-category of distinctions? To the computational physicist: can you simulate the discrete null helix on GPU? To the experimenter: can you search for log-periodic oscillations in Planck data? To the information theorist: what is the capacity of an adelic channel?

The questions are posed. The tools are specified. The falsifiability conditions are stated. The invitation is open.

---

## Declarations

**Funding:** This research received no specific grant from any funding agency.

**Conflicts of Interest:** The author declares no conflicts of interest.

**Ethics Approval:** Not applicable.

**Author Contributions:** Single author — all contributions.

**Data Availability:** No experimental data were generated or analysed.

**Code Availability:** The DDG framework described in §7 will be released under an open-source license upon completion.

**Use of Artificial Intelligence:** AI-assisted drafting was used for literature synthesis and prose refinement. All arguments and conclusions were verified by the human author.

---

## References

[1] Quni-Gudzinas, R.B. (2026). Cross-Domain Consilience Audit. Zenodo. DOI: 10.5281/zenodo.21691415. (Artifacts/consilience-gate.md in the adelic-epistemological-foundations repository.)

[2] Quni-Gudzinas, R.B. (2026). The Notation Problem. Zenodo. DOI: 10.5281/zenodo.21691040.

[3] Quni-Gudzinas, R.B. (2026). Quantum Laws of Form. Zenodo. DOI: 10.5281/zenodo.19578015.

[4] Quni-Gudzinas, R.B. (2026). Alpha as Bifurcation Parameter. Zenodo. DOI: 10.5281/zenodo.21691059.

[5] Quni-Gudzinas, R.B. (2026). A Falsifiability Protocol for the ℚ-Fundamental Hypothesis. Zenodo. DOI: 10.5281/zenodo.21697717.

[6] QNFO Research (2026). Ultrametric Engine. Zenodo. DOI: 10.5281/zenodo.21336105.

[7] QNFO Research Collective (2026). Number-Theoretic Ultrametric Foundations. Zenodo. DOI: 10.5281/zenodo.21193487.

[8] Quni-Gudzinas, R.B. (2026). Poisson Summation as the Adelic Bridge. Zenodo. DOI: 10.5281/zenodo.21691078.

[9] QNFO Research Collective (2026). Silent-Radix Cryptography. Zenodo. DOI: 10.5281/zenodo.21046734.

[10] Quni-Gudzinas, R.B. (2026). FACTORING, Adelic Complexity, and the Silent-Radix Principle. Zenodo. DOI: 10.5281/zenodo.21691642.

[11] Quni-Gudzinas, R.B. (2026). The Adelic Physics Program: Epistemological Foundations. Zenodo. DOI: 10.5281/zenodo.21686727.

[12] Quni-Gudzinas, R.B. (2026). Continuum Critique Trilogy. Zenodo. DOI: 10.5281/zenodo.21691415.
