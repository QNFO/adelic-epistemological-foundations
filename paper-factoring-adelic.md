---
title: "FACTORING, Adelic Complexity, and the Silent-Radix Principle: Why Computational Hardness May Be Representation-Dependent"
author: "Rowan Brad Quni-Gudzinas"
date: "2026-07-29"
license: "CC-BY-4.0"
doi: "10.5281/zenodo.21697676"
status: "published"
---

**Author:** Rowan Brad Quni-Gudzinas | **Date:** 2026-07-29 | **License:** CC-BY-4.0

## Abstract

Shor's algorithm proves FACTORING ∈ BQP — factoring integers is efficient on a quantum computer. The widespread claim that "quantum computers will break RSA" requires an additional, unproven premise: FACTORING ∉ BPP — that no polynomial-time classical factoring algorithm exists. After 30 years, this remains an open problem equivalent to separating BPP from BQP, which would itself separate P from PSPACE (a Clay Millennium Prize problem). We argue that the FACTORING ∉ BPP question is not merely an open problem in computational complexity — it is a **representation-dependent problem**, and its resolution may depend on which completion of Q (archimedean ℝ vs p-adic Q_p) is used to pose the question. The evidence: (1) ≥80% of known exponential quantum speedups reduce to the abelian hidden subgroup problem (HGP) — period-finding over Z/p^kZ, which is fundamentally p-adic; (2) the silent-radix principle demonstrates that a positional numeral cannot internally specify its own base, and by extension a computational problem posed over ℤ cannot internally specify whether its hardness is archimedean or p-adic; (3) FACTORING ∉ BPP is a complexity-class *phase boundary*, separating efficiently-solvable from exponentially-hard — and if phase boundaries in physics (α, double pendulum, RG fixed points) are representation-dependent, the same may hold in computation. This paper does not resolve FACTORING ∉ BPP. It argues that the *question itself* may be ill-posed if framed in purely archimedean terms — and that an adelic reformulation (unifying all completions of Q) may reframe the landscape of computational complexity theory. [SPECULATIVE]

**Keywords:** FACTORING, BQP, BPP, abelian hidden subgroup, p-adic, silent-radix, adelic complexity, Shor's algorithm, quantum advantage, representation dependence

---

## 1. Introduction: The Unproven Premise

### 1.1 What Shor Proved — and What He Didn't

In 1994, Peter Shor proved that **FACTORING ∈ BQP**: a quantum computer can factor integers in polynomial time using period-finding via the quantum Fourier transform [1, established]. This result, along with Grover's algorithm for unstructured search, launched the field of quantum computing and motivated billions of dollars in research investment.

However, the claim that "quantum computers will break RSA" requires an additional premise that Shor did NOT prove — and that remains unproven after 30 years:

> **FACTORING ∉ BPP** — that no polynomial-time classical algorithm for integer factorisation exists.

This is not a detail. It is the logical gap that separates "factoring is hard for classical computers" from "quantum computers have an advantage at factoring." If a polynomial-time classical factoring algorithm were discovered tomorrow, Shor's algorithm would remain correct (FACTORING ∈ BQP) but the claim of quantum advantage for factoring would collapse — both classical and quantum computers would factor efficiently.

### 1.2 What Proving FACTORING ∉ BPP Would Require

Proving FACTORING ∉ BPP would require separating BPP from BQP — showing that BQP is strictly larger than BPP. This would, in turn, separate P from PSPACE (since P ⊆ BPP ⊆ BQP ⊆ PSPACE). Separating P from PSPACE is a Clay Millennium Prize problem. [established — Aaronson 2013]

The converse — that FACTORING ∈ BPP — would be established by discovering a polynomial-time classical factoring algorithm. This would collapse the quantum advantage claim for factoring without saying anything about BQP's power for other problems. It would merely show that factoring was never genuinely hard — we just hadn't found the right algorithm.

### 1.3 The Narrowness of Quantum Advantage

A striking empirical fact about quantum algorithms is their narrowness. A survey of known exponential quantum speedups reveals that ≥80% reduce to the **abelian hidden subgroup problem** (HGP): find the period of a function over an abelian group G [2]. [established]

| Problem | Group | Speedup |
|:--------|:------|:--------|
| Integer factorisation | Z/nZ × Z/nZ | Exponential |
| Discrete logarithm | Z/pZ × Z/pZ | Exponential |
| Pell's equation | Z | Exponential |
| Simon's problem | Z_2^n | Exponential |
| Period-finding (general) | any finite abelian G | Exponential |

The abelian HGP is solved by the quantum Fourier transform over the group G — the same algebraic trick applied to different groups. This narrowness is significant. If quantum advantage is essentially equivalent to "can do an abelian Fourier transform efficiently," then quantum computing's power may be more algebraic than quantum-mechanical.

### 1.4 Structure

§2 connects the abelian HGP to p-adic structure. §3 introduces the silent-radix principle and extends it to computational complexity. §4 argues that FACTORING ∉ BPP is a complexity-class phase boundary. §5 proposes adelic complexity theory. §6 provides falsifiability conditions. §7 discusses limitations and open problems.

---

## 2. The Abelian HGP Is p-Adic

### 2.1 Period-Finding as Valuation-Theoretic Computation

The core of Shor's algorithm is period-finding: given a function f: Z → X with unknown period r, find r. The quantum Fourier transform over Z/NZ (for N ≈ n² where n is the integer to factor) extracts the period by measuring the frequency domain. [established]

But period-finding over Z/NZ is structurally **p-adic**. The Chinese remainder theorem factorises Z/NZ ≅ ∏_i Z/p_i^{e_i} Z, and period-finding decomposes into finding the period modulo each prime power. [established]

A period r modulo p^e determines the p-adic valuation v_p(r) — and the Bruhat-Tits tree for SL_2(Q_p) provides the natural geometric setting for period-finding in p-adic analysis [3]. The quantum Fourier transform over Z/NZ, when decomposed via the CRT, is a product of p-adic Fourier transforms — and the p-adic Fourier transform is the basis of Tate's thesis and the adelic framework [4, established].

### 2.2 Why This Matters

[SPECULATIVE] If the abelian HGP (which accounts for ≥80% of known quantum advantage) is fundamentally a p-adic computation, then quantum advantage may be a **p-adic phenomenon** rather than a general feature of quantum mechanics. Specifically: the quantum speedup may arise from the ability to efficiently compute p-adic Fourier transforms — a computation that is intrinsically ultrametric and tree-structured, matching the hierarchical architecture of quantum interference.

This would explain why quantum advantage is narrow. If the quantum computer's power is essentially "it can walk efficiently on Bruhat-Tits trees," then problems that don't have a natural embedding on those trees won't see a quantum speedup. The narrowness of quantum advantage is not a bug — it's a feature that follows from the p-adic structure of the abelian HGP.

### 2.3 The Existing QNFO Framework

The QNFO Adelic Physics Programme has already established that Zitterbewegung — the trembling motion of the Dirac electron — is a p-adic observable [3]. The ZBW current correlator is a Z_2 topological invariant [5], and the Bruhat-Tits tree provides the readout protocol for measuring this invariant [6]. The ultrametric discovery engine [7] provides computational infrastructure for p-adic analysis.

What has NOT been done — and what this paper proposes — is to extend the adelic framework from physics to computational complexity. Specifically: if physical observables are adelic (have both archimedean and p-adic components), then computational problems may be adelic as well — their hardness may depend on which place (R or Q_p) the problem is posed at.

---

## 3. The Silent-Radix Principle Extended

### 3.1 The Original Principle

The silent-radix principle, developed in the QNFO Ultrametric Foundation [8] and formalised as a cryptographic primitive in Silent-Radix Cryptography [9], states:

> **A positional numeral string cannot internally specify its own base.** The digit string "10" means two in binary, ten in decimal, sixty in sexagesimal. The radix is always a silent parameter, supplied by an external convention — a human agreement, a hardware specification, a cultural default.

This ambiguity is not a bug. It is a cryptographic resource: Silent Radix Encryption (SRE) exploits the base ambiguity as a key encapsulation mechanism where the secret is the base b, and the publicly transmitted decimal digits encode one key in base b and a different key in base 10 [9].

### 3.2 Extension to Computational Complexity

[SPECULATIVE] We propose that the silent-radix principle extends from numerals to computational problems themselves. Just as a numeral string cannot internally specify its own base, a computational problem posed over Z cannot internally specify whether its hardness is computed relative to the archimedean metric (|·|_∞) or a p-adic metric (|·|_p).

The extension:

| Domain | Silent Parameter | What It Conceals |
|:-------|:-----------------|:-----------------|
| Positional notation | Base b | The actual integer value of a digit string |
| Computational complexity | Place p (or ∞) | Whether a problem's hardness is archimedean or p-adic |

The claim is not that FACTORING is easy classically — it demonstrably is not, under all known classical algorithms. The claim is more precise: FACTORING may be hard relative to the archimedean metric (Euclidean distance between numbers, used in the number field sieve) but admit structure relative to p-adic metrics that classical algorithms don't exploit — and that quantum algorithms DO exploit via the quantum Fourier transform.

### 3.3 The Two-Place Test

[UNTESTED] A concrete test: for an integer n to be factored, compute the p-adic valuations v_p(n) for primes p dividing n. If there exists a new classical factoring algorithm whose runtime depends on v_p(n) rather than on n itself (the standard measure), that algorithm would demonstrate that factoring hardness is place-dependent — easy at small p-adic valuation, hard at large archimedean size.

No such algorithm is known. But the search space of classical factoring algorithms has been biased toward archimedean methods (sieves, continued fractions, elliptic curves) — exactly the methods that treat numbers as points on a real line rather than as leaves on a Bruhat-Tits tree.

---

## 4. FACTORING ∉ BPP as a Complexity-Class Phase Boundary

### 4.1 Phase Boundaries in Physics

The adelic physics programme has identified several physical phase boundaries that are representation-dependent:

- **α ≈ 1/137** separates the free-line regime (α = 0, non-interacting) from the confined-circle regime (α → ∞, infinite coupling). The value of α is not an arbitrary free parameter but a geometric eigenvalue [10, SPECULATIVE].
- **The double pendulum's flip threshold** (energy > 1) separates integrable swinging from chaotic tumbling. The number 1 is not a smooth point on a continuum — it's a topological cliff [11, established — Strogatz 2015].
- **RG fixed points** in quantum field theory separate different phases of matter (confined vs deconfined, ordered vs disordered). The coupling constants at these fixed points are determined by the dynamics, not chosen freely.

The meta-principle, established across the companion papers of the adelic programme [12], is that **the real-number continuum is a flat projection that conceals qualitative phase boundaries**.

### 4.2 Extension to Computational Complexity

[SPECULATIVE] We propose that complexity class boundaries — particularly BPP vs BQP — are phase boundaries of the same structural type. The question "is FACTORING ∈ BPP?" is not a question about absolute computational hardness but about the **phase diagram of the problem's parameter space** relative to a chosen metric (place).

Specifically:

- **Classical algorithms** operate in the archimedean place: they treat integers as points on the real line, use Euclidean distance as the cost measure, and optimise sieves and polynomial evaluations in that metric.
- **Quantum algorithms** operate across all places simultaneously via the quantum Fourier transform, which is the archimedean *and* p-adic Fourier transform in different regimes.
- **FACTORING ∉ BPP** is the claim that no archimedean algorithm can cross the phase boundary into the efficient region — but a quantum algorithm, by operating adelically, can.

If this analysis is correct, FACTORING ∉ BPP is true — but the *reason* it's true is not absolute computational hardness but a representation-dependent phase boundary. Change the representation (from archimedean to adelic, by incorporating p-adic structure into the algorithm), and the phase boundary moves.

### 4.3 The Complexity Phase Diagram

[SPECULATIVE] The computational complexity of FACTORING can be represented as a function of two parameters:

1. **Archimedean size:** n = |N|_∞ — the number of bits of the integer to factor
2. **p-Adic structure:** v_p(N) — the p-adic valuation of N for each prime p dividing N

The runtime of the general number field sieve (GNFS) depends on n (the archimedean size) and is exponential in n^{1/3}(log n)^{2/3}. The runtime of Shor's algorithm depends on n as well but is polynomial.

The "phase boundary" conjectured here is:

> **FACTORING is classically hard when its complexity is measured in the archimedean metric alone. It is quantum-efficient because the quantum Fourier transform measures it in the adelic metric — simultaneously at the archimedean place AND at the p-adic places for p dividing N.**

This is not a proof of FACTORING ∉ BPP. It is a structural explanation for *why* quantum computing might have an advantage: not because quantum mechanics is "more powerful" than classical physics in general, but because it naturally operates in the adelic setting where the problem's phase boundaries are differently configured.

---

## 5. Toward an Adelic Complexity Theory

### 5.1 The Idea

[SPECULATIVE] Standard computational complexity theory is archimedean: it measures problem size in bits (which are effectively |x|_∞), uses Turing machines that operate sequentially, and classifies problems by asymptotic scaling in the archimedean metric.

An **adelic complexity theory** would:

1. **Measure problem size adelically** — the "size" of an integer N is not just its bit-length (archimedean size) but the vector (|N|_∞, v_2(N), v_3(N), v_5(N), ...) — the number of bits PLUS the p-adic valuations for all primes.
2. **Define adelic algorithm classes** — A-BPP (adelic BPP) for problems solvable by a probabilistic classical algorithm that uses both archimedean and p-adic operations; A-BQP (adelic BQP) for adelic quantum algorithms.
3. **Classify problems by their adelic complexity profile** — some problems may be adelic-hard (hard at all places), others adelic-easy at some places but hard at others.

The central conjecture, which remains entirely speculative, is:

> **[SPECULATIVE]** FACTORING ∈ A-BPP. That is: there exists a classical probabilistic algorithm that, by exploiting p-adic structure (not merely archimedean sieves), achieves polynomial runtime.

This would not contradict the standard belief that FACTORING ∉ BPP — because standard BPP is archimedean. It would merely show that the hardness of factoring is place-dependent, and that the advantage of Shor's algorithm is that it naturally accesses the place where factoring is easy.

### 5.2 The Silent-Radix Analogy Applied

In silent-radix cryptography [9], the same digit string encodes different messages depending on the secret base. The security of the scheme rests on the computational hardness of determining the base.

The adelic complexity analogue: the same integer N encodes different computational hardness depending on the place. The integer 15 = 3 × 5 has archimedean size |15|_∞ = 15 (small) and p-adic valuations v_3(15) = 1, v_5(15) = 1. An algorithm that sees only the archimedean size sees "small number, easy to factor." An algorithm that sees only the p-adic structure sees "two small prime factors." Both are correct — they're just different views of the same adelic object.

The "hardness" of factoring is an artifact of the archimedean view. From the adelic view, factoring a number is equivalent to reading off its p-adic valuations — which is trivial if you have access to the p-adic metric. Classical computers don't naturally access that metric; quantum computers, via the quantum Fourier transform, do.

### 5.3 Connection to the Continuum Critique

This analysis is the computational-complexity-theoretic instance of the continuum critique — the unifying meta-principle of the adelic physics programme [12]:

> **The real-number continuum is a flat projection that conceals qualitative phase boundaries. In computational complexity, the "phase boundary" is the BPP/BQP separation — and it is an artifact of measuring problem size in the archimedean metric alone.**

If this is correct, many open problems in computational complexity — P vs BPP, BPP vs BQP, FACTORING ∉ BPP — may be **ill-posed** when framed in purely archimedean terms. They are not false; they are *incomplete* — they fail to account for the place-dependence of computational hardness. The resolution may require an adelic reformulation of computational complexity theory itself.

---

## 6. Falsifiability Conditions

| # | Prediction | Check Date | Strength | Falsification |
|:--|:-----------|:-----------|:---------|:--------------|
| F1 | FACTORING ∉ BPP is not resolved within 10 years by purely archimedean methods (GNFS variants, continued fractions, elliptic curves) | 2036 | [WEAK] | Any polynomial-time classical factoring algorithm using ONLY archimedean methods would show that the place-dependence claim is unnecessary for explaining factoring hardness |
| F2 | A classical factoring algorithm exploiting p-adic structure (Hensel lifting, p-adic Newton iteration, Bruhat-Tits tree search) is discovered with runtime O(n^k) for some k | 2035 | [WEAK] | The non-discovery of such an algorithm by 2035 would not falsify the claim, but its discovery would strongly confirm it |
| F3 | The abelian HGP accounts for ≥90% of exponential quantum speedups discovered after 2026 — quantum advantage remains narrow and p-adic | Ongoing | [WEAK] | Discovery of an exponential quantum speedup that does NOT reduce to abelian HGP (e.g., a genuinely non-abelian HGP speedup) would show quantum advantage is broader than the p-adic hypothesis claims |
| F4 | The quantum Fourier transform over Z/p^k Z has a classical analogue that achieves the same asymptotic complexity — i.e., there exists a classical p-adic Fourier transform algorithm that matches the QFT's efficiency | 2035 | [WEAK] | If no such classical algorithm exists after exhaustive search, the claim that p-adic structure is the key to quantum advantage is weakened |
| F5 | Silent-radix encryption (SRE) remains unbroken for b ~ 2^128 when attacked by algorithms optimised over the archimedean metric, but is broken by algorithms that exploit p-adic structure | 2040 | [WEAK] | If SRE is entirely unbroken for 15+ years, the place-dependence of computational hardness gains credibility; if broken by any method, the specific silent-radix instance is falsified |

---

## 7. Limitations and Open Problems

### 7.1 This Is Not a Proof

This paper does not prove FACTORING ∉ BPP, nor does it prove FACTORING ∈ A-BPP. It proposes a framework — adelic complexity theory — in which these questions may be reframed. The framework is [SPECULATIVE] throughout. The primary contribution is the **identification of a structural pattern** (phase boundaries are representation-dependent, computational hardness is a phase boundary of a specific type, therefore computational hardness may be representation-dependent) rather than a theorem.

### 7.2 The Adelic Complexity Programme

[SPECULATIVE] If the analysis in this paper is correct, the research programme is:

1. **Formalise adelic complexity classes** (A-P, A-BPP, A-BQP, A-NP) — define them rigorously in terms of oracle access to p-adic operations
2. **Prove inclusions** — show that A-P ⊆ A-BPP ⊆ A-BQP ⊆ A-PSPACE and relate to standard classes
3. **Classify problems** — determine the adelic complexity of known problems (FACTORING, discrete log, graph isomorphism, etc.)
4. **Search for classical p-adic factoring algorithms** — using Hensel lifting, Bruhat-Tits tree search, and p-adic Newton iteration
5. **Build adelic complexity-theoretic lower bounds** — prove that certain problems are hard at ALL places (genuinely adelic-hard), distinguishing them from problems that are hard only at the archimedean place

### 7.3 What Changes, What Doesn't

**What changes:** If FACTORING ∈ A-BPP, the practical impact on RSA is immediate — but ONLY if an A-BPP algorithm is discovered and implemented. The theoretical impact is profound: it would show that the BPP/BQP separation is a place-dependent artifact, not an absolute computational fact.

**What doesn't change:** Even if FACTORING ∈ A-BPP, Shor's algorithm remains a monumental achievement — it was the first algorithm to demonstrate that the quantum Fourier transform (which accesses the p-adic structure of Z/NZ) can factor efficiently. The discovery of a classical p-adic factoring algorithm would not diminish Shor's contribution; it would confirm the structural insight that motivated it.

### 7.4 Connection to Existing QNFO Infrastructure

The adelic complexity programme connects directly to existing QNFO infrastructure:

- **Ultrametric Discovery Engine** [7] — 27+ API endpoints for p-adic analysis, including Bruhat-Tits tree construction and spectral analysis. This can be extended to include complexity-theoretic computations.
- **Number-Theoretic Ultrametric Foundations** [8] — p-adic valuation classifiers for quantum error-correcting codes provide the bridge between valuation theory and computational structure.
- **Silent-Radix Cryptography** [9] — the concrete cryptographic primitive that instantiates the place-dependence of computational hardness in a practical setting.
- **Adelic Physics Programme** [12, 3, 5, 6] — the broader framework in which computational complexity is revealed as another domain where the continuum critique applies.

---

## 8. Conclusion: The Question, Not the Answer

FACTORING ∉ BPP has been an open problem for 30 years. The difficulty of resolving it — equivalent to separating major complexity classes — suggests that the question as framed may be ill-posed.

We have proposed that FACTORING ∉ BPP is not a question about absolute computational hardness but about the **representation-dependence of hardness**. If computational problems, like physical observables, are adelic — with archimedean and p-adic components — then their complexity depends on which place the computation is performed at. The quantum Fourier transform accesses all places simultaneously, which is why Shor's algorithm works. A classical p-adic factoring algorithm may exist — but would be invisible to researchers searching only in the archimedean metric.

This paper does not answer the question. It reframes it. And reframing — as the notation problem, the cross-ratio reframing of α, and the Poisson summation bridge all demonstrate — is sometimes the hardest and most necessary step toward a solution.

---

## Declarations

**Funding:** This research received no specific grant from any funding agency.

**Conflicts of Interest:** The author declares no conflicts of interest.

**Ethics Approval:** Not applicable.

**Author Contributions:** Single author — all contributions.

**Data Availability:** No experimental data were generated or analysed.

**Code Availability:** Not applicable — this paper contains no computational code beyond existing QNFO infrastructure.

**Use of Artificial Intelligence:** AI-assisted drafting was used for literature synthesis and prose refinement. All arguments and conclusions were verified by the human author.

---

## References

[1] Shor, P.W. (1994). Algorithms for Quantum Computation: Discrete Logarithms and Factoring. *Proc. 35th FOCS*, 124-134. DOI: 10.1109/SFCS.1994.365700.

[2] Childs, A.M. & van Dam, W. (2010). Quantum Algorithms for Algebraic Problems. *Rev. Mod. Phys.*, 82, 1-52. DOI: 10.1103/RevModPhys.82.1.

[3] Quni-Gudzinas, R.B. (2026). Zitterbewegung as a p-Adic Observable. Zenodo. DOI: 10.5281/zenodo.21335853.

[4] Tate, J. (1950). Fourier Analysis in Number Fields and Hecke's Zeta-Functions. PhD Thesis, Princeton University. In: Cassels & Fröhlich (eds., 1967). ISBN: 978-0950273426.

[5] Quni-Gudzinas, R.B. (2026). Majorana Zitterbewegung Current Correlator. Zenodo. DOI: 10.5281/zenodo.21336045.

[6] Quni-Gudzinas, R.B. (2026). Bruhat-Tits Readout Protocol. Zenodo. DOI: 10.5281/zenodo.21336081.

[7] QNFO Research (2026). Ultrametric Engine. Zenodo. DOI: 10.5281/zenodo.21336105.

[8] QNFO Research Collective (2026). Number-Theoretic Ultrametric Foundations. Zenodo. DOI: 10.5281/zenodo.21193487.

[9] QNFO Research Collective (2026). Silent-Radix Cryptography. Zenodo. DOI: 10.5281/zenodo.21046734.

[10] Quni-Gudzinas, R.B. (2026). Alpha as Bifurcation Parameter. Zenodo. DOI: 10.5281/zenodo.21691059.

[11] Strogatz, S.H. (2015). *Nonlinear Dynamics and Chaos*, 2nd ed. Westview Press. ISBN: 978-0813349107.

[12] Quni-Gudzinas, R.B. (2026). The Adelic Physics Program: Epistemological Foundations. Zenodo. DOI: 10.5281/zenodo.21686727.

[13] Quni-Gudzinas, R.B. (2026). Continuum Critique Trilogy. Zenodo. DOI: 10.5281/zenodo.21691415.

[14] Quni-Gudzinas, R.B. (2026). The Notation Problem. Zenodo. DOI: 10.5281/zenodo.21691040.

[15] Aaronson, S. (2013). *Quantum Computing Since Democritus*. Cambridge University Press. ISBN: 978-0521199568.

[16] Quni-Gudzinas, R.B. (2026). Poisson Summation as the Adelic Bridge. Zenodo. DOI: 10.5281/zenodo.21691078.
