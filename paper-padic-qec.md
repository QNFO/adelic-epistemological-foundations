---
title: "p-Adic Quantum Error Correction Classifier Verification: A Computational Methodology"
author: "Rowan Brad Quni-Gudzinas"
date: "2026-07-30"
license: "CC-BY-4.0"
doi: "10.5281/zenodo.21698279"
status: "published"
---

**Author:** Rowan Brad Quni-Gudzinas | **Date:** 2026-07-30 | **License:** CC-BY-4.0

## Abstract

The Number-Theoretic Ultrametric Foundations paper proposed three conjectures connecting p-adic valuation theory to quantum error-correcting (QEC) code classification: the CSS-Ultrametric Correspondence (C2.1'), Kodaira-Néron Fiber Classification for stabiliser codes (C5.1), and the Mahler v_p-Spectral Decomposition (C7.3'). Initial computational verification on 4 code families (83% accuracy) established these as theorem targets. This paper provides the computational methodology for full verification across the complete QEC landscape — an estimated 10³ codes spanning 10+ families (surface, topological, colour, LDPC, concatenated, subsystem, CSS, stabiliser, GF(4), graph). The methodology specifies: (1) a code database compilation protocol from the QEC literature; (2) automated Mahler v_p spectrum computation using the existing QNFO Ultrametric Engine; (3) Kodaira-Néron fibre type classification via the /validate API; (4) statistical validation with bootstrapping and cross-validation. Success criteria: classification accuracy ≥ 60% on a held-out test set of 50 code families (random baseline: ~25%). The methodology requires ~5 months of computational work and ~$40K in cloud resources. All tools are deployed on Cloudflare Workers with D1, R2, and Vectorize bindings. This paper is a computational methodology design — it does not perform the verification; it provides the roadmap. [SPECULATIVE]

**Keywords:** p-adic valuation, quantum error correction, stabilizer codes, Mahler spectrum, Kodaira-Néron classification, computational verification, ultrametric, Cloudflare Workers

---

## 1. Background

### 1.1 The Conjectures

The Number-Theoretic Ultrametric Foundations paper [1, established — QNFO 2026] advanced three major conjectures connecting p-adic number theory to quantum error-correcting codes:

**C2.1' (CSS-Ultrametric Correspondence).** Every CSS code corresponds to an ultrametric tree. Specifically: the CSS construction from classical codes C_1, C_2 yields a metric on the logical subspace that is ultrametric if and only if C_1 and C_2 satisfy a mutual orthogonality condition in the p-adic valuation.

**C5.1 (Kodaira-Néron Fiber Classification).** The classification of stabiliser code types — CSS, GF(4), stabiliser, graph — corresponds to Kodaira-Néron fibre types (I_n, II, III, IV, I₀*, I_n*, IV*, III*, II*) from the theory of elliptic surfaces. Each code type maps to a specific fibre type based on its p-adic Mahler spectral signature.

**C7.3' (Mahler v_p-Spectral Decomposition).** The Mahler spectral analysis of a stabiliser code — computing the v_p-Mahler spectrum of the code's weight enumerator — distinguishes optimal codes (with v_p^max ≥ 28) from random ensembles (v_p^max ≤ 4). Optimal and random codes satisfy all three conjectures.

### 1.2 Initial Verification

The initial verification [1] covered 4 code families with 83% classification accuracy and 100% lemma-level agreement. The Mahler spectral analysis yielded v_p^max = 28 for optimal codes versus v_p^max = 4 for random ensembles. All three conjectures were satisfied (3/3) for both optimal and random codes.

However, 4 code families out of the estimated 10+ families in the QEC landscape is a small sample. Full verification requires expanding to all known code families and testing generalisation.

### 1.3 This Paper

This paper provides the computational methodology for full verification. It does NOT perform the verification — it is a design document, analogous to the G-07 DDG design in the Open Problems paper [2]. The methodology is specified at the level of API calls, data structures, and statistical tests, such that an implementation team could execute it without further design decisions.

---

## 2. Methodology

### 2.1 Code Database Compilation

**Source:** The QEC literature since Calderbank-Shor-Steane (1996) contains > 10³ distinct stabiliser codes across > 10 families.

**Protocol:**
1. Compile a comprehensive list of code families: surface codes, toric codes, colour codes, low-density parity-check (LDPC) codes, concatenated codes, subsystem codes, CSS codes, GF(4)-additive codes, stabiliser codes, graph codes, hypergraph product codes, quantum expander codes, homological codes, and anyonic codes.
2. For each family, select 10 representative codes with varying parameters ([[n, k, d]] with n from 5 to 1000, k from 1 to 100, d from 3 to 50).
3. Record metadata: code family, parameters [[n, k, d]], construction method, stabiliser generator matrix, logical operators, and weight enumerator.
4. Store in the QNFO D1 database with schema: `qec_codes (id, family, n, k, d, stabilizer_json, weight_enumerator, classification, verification_status)`.

**Estimated effort:** 1 month (literature survey + database population).

### 2.2 Mahler v_p Spectrum Computation

**Tool:** QNFO Ultrametric Engine [3, established — QNFO 2026], endpoint `/spectral-analysis`.

**Protocol:**
1. For each code in the database, extract the weight enumerator polynomial A(z).
2. Compute the p-adic Mahler coefficients c_k via the Mahler expansion: A(z) = Σ c_k · binomial(z, k).
3. Compute the v_p-Mahler spectrum: for each prime p dividing the code parameters n, compute the p-adic valuations v_p(c_k) of the Mahler coefficients.
4. Extract the maximum valuation v_p^max = max_k v_p(c_k) as the spectral signature.
5. Store results with schema: `qec_spectra (code_id, prime_p, vp_max, mahler_coeffs_json, computation_timestamp)`.

**API call:**
```
POST /spectral-analysis
Body: {"code_id": "...", "prime_p": 2, "method": "mahler"}
Response: {"vp_max": 28, "coefficients": [...], "status": "ok"}
```

**Estimated effort:** 2 months (API integration + batch computation for 10³ codes). Parallelisation: the Ultrametric Engine is deployed on Cloudflare Workers at the edge, scaling to 10³ concurrent requests.

### 2.3 Kodaira-Néron Fibre Type Classification

**Tool:** QNFO Ultrametric Engine [3], endpoint `/validate`.

**Protocol:**
1. For each code, submit the Mahler spectrum (computed in §2.2) to the `/validate` endpoint.
2. The endpoint classifies the code's Kodaira-Néron fibre type based on the v_p-Mahler spectral signature.
3. Compare the classified fibre type to the known code family: CSS → I_n, GF(4) → II, stabiliser → III, graph → IV, etc. (per C5.1).
4. Compute per-family and overall classification accuracy.

**API call:**
```
POST /validate
Body: {"spectrum": {...}, "method": "kodaira-neron"}
Response: {"fibre_type": "I_5", "confidence": 0.89, "classified_family": "CSS"}
```

**Estimated effort:** 1 month (API integration, classification for 10³ codes).

### 2.4 Statistical Validation

**Protocol:**
1. **Stratified train/test split:** Hold out 50 code families (stratified across all known code types — CSS, GF(4), stabiliser, graph, LDPC, surface, etc.) for testing. Train the classifier on the remaining ~10³ codes.
2. **Bootstrapping:** Resample the training data with replacement 10³ times and compute the mean and 95% confidence interval of the classification accuracy.
3. **Cross-validation:** 10-fold cross-validation on the training set; report mean accuracy and standard deviation.
4. **Permutation test:** Shuffle the code-to-family mapping and re-run classification 10³ times to establish the null distribution. A p-value < 0.01 indicates the classification is significantly better than random.
5. **Confusion matrix:** Report which code families are confused with which other families, providing insight into the structure of the ultrametric classification.

**Estimated effort:** 1 month (statistical analysis + visualisation).

### 2.5 Total Timeline

| Phase | Timeline | Deliverable | Gate |
|:------|:---------|:------------|:------|
| Code database compilation | Month 1 | D1 database with 10³ codes | ≥ 100 codes in ≥ 10 families |
| Mahler spectrum computation | Months 2-3 | v_p-Mahler spectra for all codes | ≤ 1% API failure rate |
| Fibre type classification | Month 4 | Classification results | ≥ 80% accuracy on training |
| Statistical validation | Month 5 | Validation report | Bootstrapped CI, p < 0.01 |

**Total: 5 months. Estimated cost: ~$40K.**

---

## 3. Infrastructure

### 3.1 Cloudflare Integration

All components run on Cloudflare's edge network:

| Component | Technology | Binding |
|:----------|:-----------|:--------|
| Code database | Cloudflare D1 (SQLite) | `PAPERS_DB` → `living-paper` |
| Spectral analysis | Ultrametric Engine Worker | `/spectral-analysis` |
| Classification | Ultrametric Engine Worker | `/validate` |
| Results storage | Cloudflare R2 | `qnfo/qec-verification/` |
| Semantic search | Cloudflare Vectorize | `qwav-research-v2` |

### 3.2 Reproducibility

All computations are deterministic given the same input. The Docker container for the Ultrametric Engine is pinned to a specific commit hash in the QNFO/qnfo-skills repository. Results are stored in R2 with timestamped keys for auditability.

---

## 4. Success Criteria

### 4.1 Primary Gate

[UNTESTED] Classification accuracy ≥ 60% on a held-out test set of 50 code families. Random guessing achieves ~25% accuracy (1 in 4 fibre types). A result below 60% indicates the ultrametric classification captures signal but not enough to be practically useful.

### 4.2 Secondary Gates

- **C2.1':** The CSS-Ultrametric Correspondence is verified if ≥ 90% of CSS codes are correctly classified as type I_n fibre.
- **C5.1:** The Kodaira-Néron map is verified if per-family accuracy exceeds 80% for all families.
- **C7.3':** The v_p-Mahler spectral gap (v_p^max difference between optimal and random codes) exceeds 20 for all primes p ≥ 2.

### 4.3 Falsifiability

The conjectures are falsified if:
1. Classification accuracy falls below 60% on held-out test data (all three conjectures)
2. The Mahler spectrum of random codes shows v_p^max ≥ 20 (C7.3')
3. Per-family accuracy for any single family falls below 50% (C5.1 constrained for that family)

---

## 5. Connection to the Adelic Programme

This computational verification is the QEC-theoretic component of the broader Adelic Physics Programme [4]. The key structural connection:

- The p-adic valuations v_p distinguish optimal from random codes because optimal codes have structure that random ensembles lack — exactly analogous to the way α ≈ 1/137 (a specific geometric eigenvalue) differs from a random dimensionless coupling constant.
- The Kodaira-Néron fibre classification maps code families to algebraic-geometric types because stabiliser codes, like elliptic surfaces, are classified by their singular fibres — and the classification is ultrametric.
- The Mahler spectrum connects number theory (p-adic valuations) to quantum information (code performance) via a spectral expansion — the same bridge that Poisson summation provides between discrete sums and continuous integrals [5].

If the conjectures are verified on the full QEC landscape, the adelic programme gains a concrete computational success — the p-adic framework provides a classifier that outperforms random guessing by a factor of 2.4×, with specific structural predictions (fibre types, Mahler spectra) that are falsifiable and computationally verifiable.

---

## 6. Conclusion: The Invitation

This paper provides the computational methodology for verifying the three ultrametric QEC conjectures across the complete quantum error-correcting code landscape. The tools exist: the QNFO Ultrametric Engine [3] with its 27+ API endpoints. The data exists: the QEC literature contains > 10³ stabiliser codes. The question is clear: does p-adic valuation theory classify quantum error-correcting codes with accuracy ≥ 60%, significantly above the random baseline?

The answer awaits execution. This paper is the invitation.

---

## Declarations

**Funding:** This research received no specific grant from any funding agency.

**Conflicts of Interest:** The author declares no conflicts of interest.

**Ethics Approval:** Not applicable.

**Author Contributions:** Single author — all contributions.

**Data Availability:** No experimental data were generated or analysed.

**Code Availability:** The Ultrametric Engine is deployed on Cloudflare Workers: `https://ultrametric-engine.qnfo.workers.dev/`. The methodology described here extends the existing /spectral-analysis and /validate endpoints.

**Use of Artificial Intelligence:** AI-assisted drafting was used for literature synthesis and prose refinement.

---

## References

[1] QNFO Research Collective (2026). Number-Theoretic Ultrametric Foundations: A Unified p-adic Framework for Error-Correcting Code Classification. Zenodo. DOI: 10.5281/zenodo.21193487.

[2] Quni-Gudzinas, R.B. (2026). The Adelic Physics Programme: Open Problems and Future Directions. Zenodo. DOI: 10.5281/zenodo.21697900.

[3] QNFO Research (2026). Ultrametric Engine: Deploying a 20-Principle p-Adic Discovery Worker. Zenodo. DOI: 10.5281/zenodo.21336105.

[4] Quni-Gudzinas, R.B. (2026). The Adelic Physics Program: Epistemological Foundations. Zenodo. DOI: 10.5281/zenodo.21686727.

[5] Quni-Gudzinas, R.B. (2026). Poisson Summation as the Adelic Bridge. Zenodo. DOI: 10.5281/zenodo.21691078.
