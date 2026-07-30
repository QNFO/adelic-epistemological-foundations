---
title: "A Falsifiability Protocol for the Q-Fundamental Hypothesis: Experimental Signatures of the Discrete Continuum"
author: "Rowan Brad Quni-Gudzinas"
date: "2026-07-29"
license: "CC-BY-4.0"
doi: "10.5281/zenodo.21697717"
status: "published"
---

**Author:** Rowan Brad Quni-Gudzinas | **Date:** 2026-07-29 | **License:** CC-BY-4.0

## Abstract

The QNFO Adelic Physics Programme argues that the physically accessible base field is ℚ (the rational numbers), not ℝ (the real numbers). This claim — the *ℚ-fundamental hypothesis* — requires a falsifiability protocol. What measurement would distinguish a universe where ℝ is fundamental from one where ℚ is fundamental with ℝ as the Archimedean completion? We propose three experimental signatures: (1) log-periodic oscillations in the cosmic microwave background, a direct prediction of discrete-combinatorial structure at cosmological scales; (2) ultrametric clustering in quantum measurement statistics, where outcomes cluster hierarchically (tree-like, $\delta = 0$) rather than spreading continuously; and (3) rational fingerprints in $\alpha$ at extreme precision, detectable at $\sim 1$ ppt measurement resolution. For each signature, we specify the measurement, the predicted signal, the null hypothesis, the detection threshold, and the epistemic status. We also address the symmetry caveat: if ℝ-formalism does not imply ℝ-reality, then p-adic formalism does not imply p-adic reality — the falsifiability protocol must treat both completions symmetrically. This paper does not perform the measurements; it provides the roadmap. [SPECULATIVE]

**Keywords:** falsifiability, ℚ-fundamental, adelic physics, Ostrowski's theorem, CMB, log-periodic, ultrametric clustering, fine-structure constant, rational fingerprints, continuum critique

---

## 1. Introduction: The Frontier Question

### 1.1 What the Adelic Programme Claims

The QNFO Adelic Physics Programme [1] makes one central claim: the physically accessible base field of physics is ℚ (the rational numbers), not ℝ (the real numbers). Ostrowski's theorem [2, established] then demands that all p-adic completions $\mathbb{Q}_p$ be physically meaningful alongside the Archimedean completion ℝ.

This is not a reinterpretation of existing physics. It is a new physical claim with specific, falsifiable predictions [1, 3, 4]. But these predictions have been scattered across multiple companion papers — the ZBW as p-adic observable [3], the Bruhat-Tits readout protocol [4], the $\alpha$ reframing [5], the Falsifiability Register of the Bayesian cascade [6]. No single document has provided a **unified falsifiability protocol** — a systematic map from the theoretical claim to specific experimental signatures with detection thresholds and null hypotheses.

This paper provides that protocol.

### 1.2 The Frontier Question

The cross-domain consilience audit of the adelic programme [7] identified a single Frontier Question that applies to all six domains simultaneously:

> **What measurement would falsify the continuum? In other words: what is the single testable prediction that distinguishes a universe where ℝ is fundamental from one where ℚ is fundamental with ℝ as the Archimedean completion?**

This paper proposes three candidate measurements, each targeting a different physical scale, each with a different falsification condition.

### 1.3 The Epistemic Symmetry Caveat

Before presenting the protocol, we restate the epistemic symmetry caveat from prior work [8]:

> **If ℝ-formalism does not imply ℝ-reality, then by identical logic, p-adic formalism does not imply p-adic reality.** [established — logical necessity]

The falsifiability protocol treats both completions symmetrically. A failure to detect p-adic signatures does NOT prove ℝ is fundamental — it only shows that this particular p-adic model is not empirically confirmed at current precision. Conversely, detection of p-adic signatures would NOT prove ℚ is fundamental in an ontological sense — it would only show that p-adic structure encodes physical information invisible to the Archimedean framework.

The protocol is designed for the modest claim: ℚ is the physically accessible base field, and all Ostrowski completions — ℝ and $\mathbb{Q}_p$ — are legitimate completions that may encode physical information. It does NOT test the stronger claim that specific p-adic models (Bruhat-Tits walks, ZBW as $\mathbb{Q}_2$ observable) are literally happening in Hilbert space.

### 1.4 Structure

§2 presents Signature 1: log-periodic oscillations in the CMB. §3 presents Signature 2: ultrametric clustering in quantum measurement statistics. §4 presents Signature 3: rational fingerprints in $\alpha$ at extreme precision. §5 discusses the detection thresholds and timeline. §6 addresses epistemic risks and post-hoc rationalisation. §7 provides the Falsifiability Register.

---

## 2. Signature 1: Log-Periodic Oscillations in the CMB

### 2.1 The Prediction

The QNFO Quantum Laws of Form programme [9] makes a specific, falsifiable prediction: **the cosmic microwave background (CMB) temperature angular power spectrum should exhibit log-periodic oscillations** — discrete Fourier modes in $\log(\ell)$ rather than $\ell$, where $\ell$ is the multipole moment.

The physical origin: if spacetime at the Planck scale has a discrete-combinatorial structure (a Bruhat-Tits tree rather than a smooth manifold), then primordial density perturbations are not continuous functions on a smooth background but discrete functions on a tree graph. The Fourier transform of a discrete tree function produces log-periodic modulation — exactly as the Poisson summation formula produces periodic modulation from discrete lattice sums [8].

Formally: let $\delta\rho(x)$ be the primordial density perturbation. In standard cosmology, $\delta\rho(x)$ is a continuous random field on $\mathbb{R}^3$ with a nearly scale-invariant power spectrum $P(k) \propto k^{n_s-1}$ where $n_s \approx 0.965$. In the discrete-combinatorial model, $\delta\rho$ is defined on the vertices of a Bruhat-Tits tree $\mathcal{T}_p$ at the Planck scale, and its power spectrum acquires a multiplicative log-periodic factor:

$P(k) = P_0(k) \cdot \left[1 + A \cos(\omega \log(k/k_0) + \phi)\right]$

where $A$ is the oscillation amplitude, $\omega$ is the log-frequency, $k_0$ is a reference scale, and $\phi$ is a phase. [SPECULATIVE]

### 2.2 The Measurement

The CMB angular power spectrum $C_\ell$ has been measured by Planck [10, established] to cosmic-variance-limited precision for $\ell \lesssim 2000$. The log-periodic oscillation signature would appear as a periodic modulation in $\log(\ell)$ across the acoustic peaks.

The detection threshold: $A \gtrsim 10^{-3}$ (0.1% modulation) at Planck sensitivity. Below this, the signal is below the cosmic variance limit. Future CMB experiments (Simons Observatory, CMB-S4) will reduce the detection threshold to $A \gtrsim 10^{-4}$ [11].

### 2.3 Null Hypothesis

The null hypothesis is the standard $\Lambda$CDM model: no log-periodic oscillations, $A = 0$, and the power spectrum is purely scale-invariant with small deviations from the spectral index $n_s \neq 1$.

### 2.4 Status: Untested, Low Signal, High Stakes

[UNTESTED] A search for log-periodic oscillations in the Planck 2018 data [10] has been proposed (QNFO Quantum Laws of Form [9]) but not yet performed. The expected signal amplitude ($A \lesssim 10^{-3}$) is at the edge of Planck sensitivity — a null result at Planck resolution would NOT falsify the ℚ-fundamental hypothesis; it would only constrain the amplitude to $A \lesssim 10^{-3}$.

A positive detection (log-periodic oscillations at $>3\sigma$ significance in Planck or CMB-S4 data) would be a direct signature of discrete-combinatorial structure at cosmological scales — inconsistent with a smooth, continuous spacetime manifold and therefore inconsistent with a fundamental continuum. This would strongly corroborate the ℚ-fundamental hypothesis.

### 2.5 Falsification Window

| Parameter | Planck (2018) | Simons Observatory (~2028) | CMB-S4 (~2035) |
|:----------|:-------------|:--------------------------|:---------------|
| Sensitivity (A) | $\sim 10^{-3}$ | $\sim 3 \times 10^{-4}$ | $\sim 10^{-4}$ |
| $\ell$ range | 2–2500 | 30–5000 | 30–5000 |
| Detection | Marginal | Possible | Strong |

---

## 3. Signature 2: Ultrametric Clustering in Quantum Measurement Statistics

### 3.1 The Prediction

If quantum measurement outcomes are fundamentally rational numbers — as required by the ℚ-fundamental hypothesis — then the p-adic completions of those outcomes should exhibit ultrametric structure. Specifically: **the pairwise distances between measurement outcomes, when measured in a p-adic metric, should exhibit hierarchical clustering** rather than the continuous spread expected from an Archimedean measurement model.

The Gromov hyperbolicity $\delta$ of the resulting metric space is the diagnostic. For a tree-like ultrametric space, $\delta = 0$ (all triangles are $0$-thin). For an Archimedean metric space (e.g., points sampled from a Gaussian distribution on $\mathbb{R}^n$), $\delta > 0$ and grows with the dimension of the space. [3, established — QNFO P1 §4]

The prediction: for any quantum system with $\ge 10^3$ repeated measurements of the same observable, the Gromov $\delta$ of the measurement-outcome metric space, computed in the 2-adic metric, should satisfy $\delta \lesssim 0.1$ — consistent with tree-like ultrametric structure. [SPECULATIVE]

### 3.2 The Measurement

Protocol A from the Bruhat-Tits Readout Protocol [4] specifies the experimental procedure:

1. **Select a quantum system** with a discrete measurement spectrum (e.g., a superconducting qubit, trapped ion, or Majorana nanowire)
2. **Perform $\ge 10^4$ repeated projective measurements** of the same observable (e.g., $\sigma_z$ on a qubit)
3. **Record the raw measurement outcomes** as rational numbers (binary 0/1 for qubits; integer photon counts for optical systems)
4. **Compute the p-adic distance matrix** — for outcomes $x_i, x_j$, the 2-adic distance is $d_2(x_i, x_j) = 2^{-v_2(x_i - x_j)}$ where $v_2$ is the 2-adic valuation
5. **Compute the Gromov $\delta$** of the resulting metric space using the standard thin-triangles algorithm [12]
6. **Compare $\delta$ to the Archimedean control** — the same outcomes measured in Euclidean distance should have $\delta \gg 0$

### 3.3 Null Hypothesis

The null hypothesis is that measurement outcomes are independent, identically distributed random variables on $\mathbb{R}$ (standard quantum mechanics). In this case, the p-adic distances should NOT exhibit ultrametric clustering — the Gromov $\delta$ should be indistinguishable from the Euclidean $\delta$, up to statistical noise.

### 3.4 Detection Threshold

The detection requires $\delta_{\text{p-adic}} \lesssim 0.1$ AND $\delta_{\text{Archimedean}} \gg 0.1$ in the same dataset. This is a differential measurement — the same outcomes, two different metrics, different structural signatures.

The statistical threshold: the difference $\Delta\delta = \delta_{\text{Archimedean}} - \delta_{\text{p-adic}}$ must exceed $3\sigma$ of the bootstrapped null distribution. For $\ge 10^4$ measurements, this requires $\Delta\delta \gtrsim 0.05$.

### 3.5 Status: Experimentally Feasible, Not Yet Performed

[UNTESTED] The measurement protocol is feasible with current technology:
- Superconducting qubits (IBM, Google, Rigetti): $\ge 10^4$ projective measurements in minutes
- Trapped ions (IonQ, Quantinuum): similar rates
- Majorana nanowires (Microsoft, Delft): lower fidelity but the ZBW connection [3, 4] makes them the theoretically preferred platform

No experimental group has performed this specific measurement — the concept of computing p-adic distances on quantum measurement outcomes is novel to the QNFO programme.

---

## 4. Signature 3: Rational Fingerprints in α at Extreme Precision

### 4.1 The Prediction

If $\alpha$ is a projective invariant — a cross-ratio of rational length scales $\alpha = \text{CR}(r_e, \lambda_C; 0, \infty)$ [5] — and if those length scales are rational multiples of the Planck length $\ell_P$, then $\alpha$ itself is a rational number. [SPECULATIVE]

A rational number has a terminating or repeating decimal (or p-adic) expansion. At current measurement precision ($\sim 0.15$ ppb, or $\sim 10$ significant digits), no rational fingerprint is detectable unless the denominator is very small ($\lesssim 10^2$). At improved precision ($\sim 1$ ppt, or $\sim 12$ significant digits), a rational fingerprint with denominator up to $\sim 10^4$ would become detectable.

### 4.2 The Measurement

The most precise measurement of $\alpha$ comes from the electron magnetic moment anomaly $a_e = (g-2)/2$ [13, established]:

$a_e^{\text{exp}} = 0.00115965218059(13)$

This measurement determines $\alpha$ to 0.15 ppb. The next-generation experiment (Northwestern g-2) aims for $\sim 0.01$ ppb precision — approximately 12 significant digits.

At 12-digit precision, a rational number with denominator up to $10^4$ would reveal its rational structure. Specifically: if $\alpha^{-1} = p/q$ with $q \lesssim 10^4$, then $\alpha^{-1}$ expressed in decimal would show a periodic pattern of length at most $q$.

### 4.3 Null Hypothesis

The null hypothesis is standard QED: $\alpha$ is a running coupling constant, determined by the renormalisation group flow from the UV, with NO rational structure. In this case, improved measurements would reveal an increasingly long, apparently random decimal expansion — consistent with an irrational (or even transcendental) number.

### 4.4 Detection Threshold

The detection of rational structure requires a pattern at $>5\sigma$ significance in the decimal expansion of $\alpha^{-1}$. For a denominator $q$, the expected signal-to-noise ratio after $N$ digits of measurement is SNR $\approx \sqrt{N/q}$. For $N = 12$ digits and $q \lesssim 10^3$, SNR $\gtrsim 3$, which is marginal. For $N = 15$ digits and $q \lesssim 10^3$, SNR $\gtrsim 10$, which is strong.

**Realistic timeline:** 15-digit measurement of $\alpha$ requires approximately 1 order of magnitude improvement over current precision (0.01 ppb). This is projected for the 2030s [13].

### 4.5 Status: Precision Inadequate, Future Measurement May Resolve

[UNTESTED] Current precision ($< 12$ digits) is insufficient to detect rational structure. A null result at current precision is expected and does not falsify the hypothesis. The hypothesis becomes testable at $\sim 15$ digit precision, projected for the 2030s.

---

## 5. Detection Thresholds and Timeline

| Signature | Current Status | Detection Threshold | Projected Window | Null-Result Meaning |
|:----------|:---------------|:--------------------|:------------------|:-------------------|
| S1: CMB log-periodic | Planck 2018 data available, analysis not yet performed | $A \gtrsim 10^{-3}$ at $3\sigma$ | 2026–2028 (Simons Obs.) | $A \lesssim 10^{-3}$ — constrains amplitude, does NOT falsify ℚ-fundamental |
| S2: Ultrametric clustering | Protocol designed [4], no implementation | $\Delta\delta \gtrsim 0.05$ at $3\sigma$ | 2026–2030 (existing hardware) | $\Delta\delta \approx 0$ — constrains ultrametric signal, does NOT falsify |
| S3: Rational α fingerprints | $\sim 10$ digits (0.15 ppb) | $\sim 15$ digits (0.01 ppb) | 2030–2040 (g-2 experiments) | $\alpha$ appears irrational at $\sim 15$ digits — strongly constrains |

**Conservation of null results:** If ALL three signatures return null results at their detection thresholds — no log-periodic CMB oscillations, no ultrametric clustering, no rational $\alpha$ fingerprint at 15-digit precision — the ℚ-fundamental hypothesis is strongly constrained. It is NOT logically falsified (absence of evidence is not evidence of absence), but its empirical motivation would be severely weakened. The programme would survive only as a mathematical framework without confirmed physical predictions.

---

## 6. Epistemic Risks and Post-Hoc Rationalisation

### 6.1 The Post-Hoc Risk

A measurable risk for any programme with multiple falsifiability conditions is **post-hoc rationalisation**: when a prediction fails, the programme adjusts its parameters rather than accepting falsification.

To mitigate this risk, we register the following calibration commitments:

1. **S1 (CMB log-periodic):** If no oscillation is detected at Simons Observatory sensitivity ($A \lesssim 3 \times 10^{-4}$), the predicted amplitude $A \gtrsim 10^{-3}$ is **falsified**. Claiming "the amplitude must be smaller than $10^{-4}$" is NOT a legitimate post-hoc adjustment unless accompanied by a revised model that independently predicts the smaller amplitude.

2. **S2 (Ultrametric clustering):** If $\Delta\delta < 0.05$ at $3\sigma$ with $\ge 10^4$ measurements on 3 independent platforms (superconducting, trapped-ion, Majorana), the claim that p-adic structure is detectable in quantum measurement statistics at current precision is **falsified**.

3. **S3 (Rational $\alpha$):** If $\alpha$ shows NO rational fingerprint at 15-digit precision (SNR $\gtrsim 10$), the claim that $\alpha$ is a rational number with denominator $\lesssim 10^4$ is **falsified**. Claiming "the denominator must be larger" is acceptable only if accompanied by an independent prediction of the denominator.

### 6.2 The Symmetry Caveat in Practice

Per the symmetry caveat [8], a null result does NOT prove ℝ is fundamental. It only shows that the specific p-adic models proposed by QNFO (Bruhat-Tits tree at Planck scale, ZBW as $\mathbb{Q}_2$ observable, $\alpha$ as rational cross-ratio) are not confirmed at current precision. The logical possibility remains open that:
- The true base field is still ℚ, but the specific p-adic signatures are different from those predicted
- Detection requires higher precision than projected
- The signatures are qualitatively different from those proposed

These are legitimate possibilities but cannot be invoked to indefinitely evade falsification. A programme that accumulates null results across all three signatures for two decades (2026–2046) without a positive detection is empirically indistinguishable from a programme that is empirically vacuous.

---

## 7. Falsifiability Register

The following predictions are dated, strength-tagged, and committed to the QNFO Falsifiability Register [6]:

| # | Signature | Prediction | Check Date | Strength | Falsification |
|:--|:----------|:-----------|:-----------|:---------|:--------------|
| F1 | S1: CMB log-periodic | Log-periodic oscillations detected in CMB angular power spectrum with amplitude $A \gtrsim 10^{-3}$ at $\ge 3\sigma$ | 2028 (Simons Obs.) | [WEAK — model-dependent amplitude prediction] | $A \lesssim 3 \times 10^{-4}$ with no oscillation detected — refutes predicted amplitude |
| F2 | S2: Ultrametric clustering | Gromov $\delta_{\text{p-adic}} \lesssim 0.1$ AND $\delta_{\text{Archimedean}} \gg 0.1$ at $\ge 3\sigma$ | 2030 (3 platforms) | [WEAK — first-of-its-kind measurement] | $\Delta\delta < 0.05$ on all 3 platforms — refutes detectable ultrametric signal claim |
| F3 | S3: Rational $\alpha$ | Periodic structure detected in $\alpha^{-1}$ decimal expansion with SNR $\gtrsim 10$ | 2040 (15-digit g-2) | [STRONG — a rational number either repeats or doesn't] | No periodic structure at 15-digit SNR $\gtrsim 10$ — refutes rational-α-with-q-less-than-10000 claim |
| F4 | Conservation | If F1, F2, AND F3 all return null | 2046 | [STRONG] | ℚ-fundamental hypothesis has no confirmed experimental signature after 20 years — severely constrained, programme reduced to mathematical framework |

---

## 8. Conclusion: The Measurement, Not the Theory

The QNFO Adelic Physics Programme has produced a body of theoretical work: 16 preparatory notes, 6 consolidated publications, a taxonomy of marginalised formalisms, a reframing of $\alpha$ as a cross-ratio, a Poisson summation bridge between discrete and continuous, and an analysis of computational complexity as representation-dependent.

What has not been produced — until this paper — is a **falsifiability protocol**: a systematic map from theoretical claims to experimental signatures with detection thresholds, null hypotheses, and post-hoc rationalisation safeguards.

This paper provides that protocol. It does not perform the measurements — it provides the roadmap. The next step is clear: identify an experimental collaboration willing to perform S2 (ultrametric clustering), the most immediately feasible of the three signatures. The protocol is designed, the hardware exists, the measurement takes minutes.

The fate of the ℚ-fundamental hypothesis will be decided not by theoretical argument but by experimental result. This paper is the invitation to make the measurement.

---

## Declarations

**Funding:** This research received no specific grant from any funding agency.

**Conflicts of Interest:** The author declares no conflicts of interest.

**Ethics Approval:** Not applicable.

**Author Contributions:** Single author — all contributions.

**Data Availability:** No experimental data were generated or analysed. Planck 2018 CMB data are publicly available at pla.esac.esa.int.

**Code Availability:** The Gromov $\delta$ computation algorithm is specified in [4] and available via the QNFO Ultrametric Engine [14]. The log-periodic CMB analysis code is pending.

**Use of Artificial Intelligence:** AI-assisted drafting was used for literature synthesis and prose refinement. All arguments and conclusions were verified by the human author.

---

## References

[1] Quni-Gudzinas, R.B. (2026). The Adelic Physics Program: Epistemological Foundations and Communications Framework. Zenodo. DOI: 10.5281/zenodo.21686727.

[2] Ostrowski, A. (1916). Über einige Lösungen der Funktionalgleichung $\varphi(x)\cdot\varphi(y)=\varphi(xy)$. *Acta Mathematica*, 41, 271-284.

[3] Quni-Gudzinas, R.B. (2026). Zitterbewegung as a p-Adic Observable. Zenodo. DOI: 10.5281/zenodo.21335853.

[4] Quni-Gudzinas, R.B. (2026). Bruhat-Tits Readout Protocol. Zenodo. DOI: 10.5281/zenodo.21336081.

[5] Quni-Gudzinas, R.B. (2026). Fine-Structure Constant as a Cross-Ratio. Zenodo. DOI: 10.5281/zenodo.20108536.

[6] Quni-Gudzinas, R.B. (2026). Alpha as Bifurcation Parameter — Appendix: Deep Research Bayesian Cascade. Zenodo. DOI: 10.5281/zenodo.21691059.

[7] Quni-Gudzinas, R.B. (2026). Cross-Domain Consilience Audit (artifacts/consilience-gate.md). adelic-epistemological-foundations repository.

[8] Quni-Gudzinas, R.B. (2026). Poisson Summation as the Adelic Bridge. Zenodo. DOI: 10.5281/zenodo.21691078.

[9] Quni-Gudzinas, R.B. (2026). Quantum Laws of Form: A Syntactic Foundation for Physics. Zenodo. DOI: 10.5281/zenodo.19578015.

[10] Planck Collaboration (2020). Planck 2018 results. I. Overview and the cosmological legacy of Planck. *Astron. Astrophys.*, 641, A1. DOI: 10.1051/0004-6361/201833880.

[11] Abazajian, K. et al. (2016). CMB-S4 Science Book, First Edition. arXiv:1610.02743.

[12] Gromov, M. (1987). Hyperbolic Groups. In *Essays in Group Theory* (ed. S.M. Gersten), 75-263. Springer. ISBN: 978-0387966182.

[13] Hanneke, D., Fogwell, S., & Gabrielse, G. (2008). New Measurement of the Electron Magnetic Moment and the Fine Structure Constant. *Phys. Rev. Lett.*, 100, 120801. DOI: 10.1103/PhysRevLett.100.120801.

[14] QNFO Research (2026). Ultrametric Engine. Zenodo. DOI: 10.5281/zenodo.21336105.

[15] Quni-Gudzinas, R.B. (2026). FACTORING, Adelic Complexity, and the Silent-Radix Principle. Zenodo. DOI: 10.5281/zenodo.21691642.
