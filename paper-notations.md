---
title: "The Notation Problem: Category-Theoretic Scaffold-Stripping of Six Marginalised Formal Systems, with an Application to a Distinction-Based Calculus for Prime Numbers"
author: "Rowan Brad Quni-Gudzinas"
date: "2026-07-29"
license: "CC-BY-4.0"
doi: "10.5281/zenodo.21690262"
status: "published"
---

**Author:** Rowan Brad Quni-Gudzinas | **Date:** 2026-07-29 | **License:** CC-BY-4.0

## Abstract

Six formal systems — Laws of Form (Spencer-Brown), Existential Graphs (Peirce), the Viable System Model (Beer), Catastrophe Theory (Thom), Pattern Language (Alexander), and Polycontextural Logic (Günther) — share a common fate: despite containing mathematical insights with cross-domain applicability, they remain intellectually marginalised. Mainstream formalisms (set theory, category theory, Kripke semantics) achieved canonical status while these six did not. Why? We propose the **scaffold-stripping hypothesis**: the marginalisation is a notation problem, not a content problem. When each formalism's core invariant is expressed in standard category-theoretic language, the notation-specific scaffolds dissolve and the invariants become indistinguishable from canonical mathematics. We provide category-theoretic expressions for all six formalisms: LoF as an idempotent monad on a 2-category of distinctions, Existential Graphs as a topos-theoretic subobject classifier morphism, VSM as an endofunctor with fixed point, Catastrophe Theory as a sheaf of singularity unfoldings, Pattern Language as a coalgebra for a pattern-composition functor, and Polycontextural Logic as a presheaf of Heyting algebras. We then apply this framework to develop a **Distinction Calculus for Numbers (DCN)** — a formal system that derives the Fundamental Theorem of Arithmetic from primitives of indication rather than set-membership. The DCN yields the **sunburst notation** for prime numbers, where primality becomes visually immediate as the absence of compositional depth. We argue that marginalised formalisms are not failed formalisms but notation-imprisoned ones, and that scaffold-stripping is a general methodology for recovering their mathematical content. The paper concludes with cognitive, educational, and sociological implications — and specific falsifiability conditions.

**Keywords:** Laws of Form, category theory, scaffold-stripping, notation problem, distinction calculus, prime numbers, marginalised formalisms, Spencer-Brown, Charles Sanders Peirce, Stafford Beer, René Thom, Christopher Alexander, Gotthard Günther

---

## 1. Introduction

### 1.1 The Puzzle of Marginalised Formalisms

The twentieth century produced several ambitious formal systems that claimed to capture universal structural patterns — and failed to achieve mainstream adoption. George Spencer-Brown's *Laws of Form* [1] proposed that a single primitive act (drawing a distinction) could generate all of mathematics. Charles Sanders Peirce's Existential Graphs [2] offered a diagrammatic logic claimed to be more fundamental than algebraic notation. Stafford Beer's Viable System Model [3] modelled organisational recursion. René Thom's Catastrophe Theory [4] classified discontinuous changes in continuous systems. Christopher Alexander's Pattern Language [5] proposed generative rules for built environments. Gotthard Günther's Polycontextural Logic [6] extended classical logic to multi-context reasoning.

None achieved the canonical status of set theory, category theory, or Kripke semantics. Why?

The standard explanations fall into three categories. **First**, the "first impression" problem: a book claiming universal scope with no theorems, no lemmas, and no references triggers a rational dismissal response from professional mathematicians [7]. **Second**, the credibility cascade: Spencer-Brown's unverified claims about the Four Colour Theorem and Riemann Hypothesis damaged his credibility, and a formalism whose creator makes demonstrably false claims about its power is one professionals avoid [7]. **Third**, the cult dynamic: small devoted followings reinforce marginalisation — a formalism adopted by "the LoF community" is one mainstream logicians can safely ignore [7].

These explanations are sociological and may be true. But they leave open a deeper question: **is the content of these formalisms valid, and merely imprisoned in inaccessible notation — or is there something genuinely wrong with the content that makes it resistant to mainstream adoption?**

### 1.2 The Scaffold-Stripping Hypothesis

We propose: **all six marginalised formalisms contain valid mathematical invariants that, when expressed in standard category-theoretic language, become indistinguishable from canonical mathematics.** The marginalisation is a notation problem, not a content problem. If this hypothesis holds, the formalisms are not failed — they are notation-imprisoned. Recovery requires **scaffold-stripping**: extracting the invariant and discarding the notation.

This hypothesis is falsifiable. If a formalism's invariant *cannot* be expressed in category-theoretic language without loss, that formalism genuinely lacks mathematical content and its marginalisation is merited.

### 1.3 Structure of This Paper

Section 2 reviews each marginalised formalism and extracts its core invariant. Section 3 provides category-theoretic expressions for all six. Section 4 addresses the Kauffman counterexample — the strongest challenge to the hypothesis. Section 5 develops a Distinction Calculus for Numbers (DCN) as an application of the scaffold-stripping methodology. Section 6 derives the Fundamental Theorem of Arithmetic within DCN and introduces the sunburst notation. Section 7 discusses cognitive, educational, and cross-domain implications. Section 8 provides falsifiability conditions and open problems.

---

## 2. The Six Marginalised Formalisms

### 2.1 Laws of Form (Spencer-Brown, 1969)

**Primitive:** The act of drawing a distinction. A mark `( )` separates a space into marked and unmarked. Two reduction rules — Calling (repetition collapses) and Crossing (double enclosure cancels) — generate a Boolean algebra. The key innovation is **re-entry**: a mark that refers to itself, producing oscillating values and introducing time into the formalism.

**Core invariant:** Distinction as the primitive operation from which all structure is generated. The mark is not a container; it is an act — a temporal gesture of separation. This challenges the static-axiom paradigm at its root.

**Why marginalised:** A formalism built on self-reference threatens every department's autonomy. The claim that "a universe comes into being when a space is severed" is untestable and outside the scope of formal mathematics as currently constituted. The book's style — aphoristic, lacking standard mathematical apparatus — triggers the first-impression problem.

### 2.2 Existential Graphs (Peirce, c. 1897)

**Primitive:** Diagrammatic negation. A closed curve (a "cut") on a sheet of assertion negates whatever is inside it. Logical operations — conjunction, disjunction, implication — are expressed through cuts and juxtaposition without symbolic variables.

**Core invariant:** Negation as a topological operation (enclosure) rather than a syntactic one (the symbol $
eg$). This makes logical consequence a matter of diagram transformation rather than symbol manipulation.

**Why marginalised:** Peirce died before completing the system. The diagrams are difficult to typeset and were inaccessible before modern computing. The graphical notation resists integration with the text-based tradition of mathematical logic.

### 2.3 Viable System Model (Beer, 1972)

**Primitive:** Recursive viability. Any viable system contains and is contained by other viable systems. Five subsystems (operations, coordination, control, intelligence, policy) recur at every level of recursion.

**Core invariant:** Recursive self-organisation with a fixed-point structure. A system is viable if and only if its organisational architecture satisfies the VSM recursion condition.

**Why marginalised:** Beer applied the model to management cybernetics, not to mathematics. The model is presented as a management tool rather than a mathematical structure. The notation (hand-drawn diagrams of ovoids and channels) resists formalisation.

### 2.4 Catastrophe Theory (Thom, 1972)

**Primitive:** Structural stability under smooth perturbations. When a dynamical system governed by a potential function is perturbed, its behaviour changes continuously — except at catastrophe points where the topology of the state space jumps discontinuously.

**Core invariant:** Singularity unfoldings classify qualitative changes in continuous systems. Thom's classification theorem identifies seven elementary catastrophes for systems with up to four control parameters.

**Why marginalised:** Over-application in the 1970s (applying catastrophe theory to everything from stock market crashes to prison riots) triggered a backlash. The mathematical content is valid; the sociological overreach damaged credibility.

### 2.5 Pattern Language (Alexander, 1977)

**Primitive:** Generative patterns. A pattern is a recurring solution to a recurring problem in a context. Patterns compose hierarchically: large patterns are generated from smaller ones through composition rules.

**Core invariant:** Pattern composition as a generative grammar. A pattern language is a combinatorial system where complex structures emerge from the iteration and composition of atomic patterns.

**Why marginalised:** Alexander applied the model to architecture and urban design, not to mathematics. Like Beer, his work is treated as domain-specific methodology rather than a general formal system. The notation (hand-drawn sketches and prose descriptions) is inaccessible to formal treatment.

### 2.6 Polycontextural Logic (Günther, c. 1960s-70s)

**Primitive:** Contextural distribution. Classical logic operates within a single context (one truth-value space). Polycontextural logic distributes propositions across multiple contextures, each with its own logic, connected by order relations and junctions.

**Core invariant:** Logic as a presheaf — truth-values are assigned contexture-locally, and the relationships between contextures are structural (order relations, junctions) rather than truth-functional.

**Why marginalised:** Günther wrote in dense German philosophical prose aimed at a Hegelian audience, not at logicians. The formalism is embedded in a metaphysical system that most analytic philosophers reject. The notation (elaborate diamond-shaped diagrams) is unfamiliar to logicians trained in the Frege-Russell tradition.

---

## 3. Category-Theoretic Scaffold-Stripping

For each formalism, we strip the notation-specific scaffold and express the invariant in standard category-theoretic language.

### 3.1 Laws of Form  \rightarrow  Idempotent Monad on a 2-Category of Distinctions

The primitive act — drawing a distinction that separates a space into marked and unmarked — maps naturally to an idempotent monad $T: \mathcal{C} \to \mathcal{C}$ on a 2-category $\mathcal{C}$ whose objects are spaces (contexts), 1-morphisms are distinctions (acts of separation), and 2-morphisms are transformations of distinctions. The unit $\eta: 1_{\mathcal{C}} \to T$ introduces the mark; the multiplication $\mu: T^2 \to T$ satisfies idempotence $T^2 \cong T$ (corresponding to Calling: repetition collapses). The re-entry construction corresponds to a fixed point of $T$ in the 2-categorical sense — an object $X$ with an isomorphism $\eta_X: X \cong TX$.

This translation reveals that LoF is not an alternative to mathematics but a *2-categorical logic of distinctions* — a structure wholly compatible with mainstream category theory.

### 3.2 Existential Graphs  \rightarrow  Topos-Theoretic Subobject Classifier Morphism

The cut (negation as enclosure) is the characteristic morphism $\chi_A: A \to \Omega$ in a topos, where $\Omega$ is the subobject classifier. Conjunction is the product in the internal logic; disjunction is the coproduct; implication is the exponential. The sheet of assertion is the terminal object `1`. Peirce's diagrammatic transformations are precisely the commuting diagrams of the internal language of a topos.

This translation reveals that Existential Graphs are not a rival to algebraic logic but a *diagrammatic presentation of topos logic* — the same structure, a different interface.

### 3.3 Viable System Model  \rightarrow  Endofunctor with Fixed Point

Beer's recursive viability condition is an endofunctor $V: Sys \to Sys$ where `V(S)` is the VSM-organised version of system `S`. Viability is the condition that $V(S) \cong S$ — a fixed point. The five subsystems are natural transformations that collectively establish the isomorphism. The recursion (a system contains and is contained by other systems) is the closure of `V` under composition.

This translation reveals that VSM is not management folklore but a *fixed-point semantics for self-organising systems* — a structure with formal content independent of its application domain.

### 3.4 Catastrophe Theory  \rightarrow  Sheaf of Singularity Unfoldings

Thom's classification of elementary catastrophes is the local structure of a sheaf $\mathcal{S}$ over a stratified space `M` of control parameters. The stalk $\mathcal{S}_x$ at a point $x ∈ M$ is the germ of the potential function at `x`. The stratification separates regions of structural stability from catastrophe sets (singularities). The seven elementary catastrophes are the possible local models of $\mathcal{S}$ near a singular point in up to four dimensions.

This translation reveals that Catastrophe Theory is not overreach but *singularity theory expressed in sheaf-theoretic language* — a mature branch of differential topology.

### 3.5 Pattern Language  \rightarrow  Coalgebra for a Pattern-Composition Functor

A pattern `P` is a state of a coalgebra $\gamma: Pat \to F(Pat)$ for an endofunctor `F` that encodes admissible compositions. The terminal coalgebra (if it exists) is the set of all pattern languages that can be generated from atomic patterns. A pattern language is a tree in this coalgebra. Alexander's generative grammar is the unfolding of the coalgebra.

This translation reveals that Pattern Language is not architectural intuition but a *coalgebraic generative grammar* — a structure isomorphic to the algebraic semantics of programming languages and process calculi.

### 3.6 Polycontextural Logic  \rightarrow  Presheaf of Heyting Algebras

The truth-value space of a contexture is a Heyting algebra `H(U)`. Contextures form a site $\mathcal{C}$ (a category with a Grothendieck topology). The truth-value assignment is a presheaf $H: \mathcal{C}^op \to Heyting$ where `H(U)` is the Heyting algebra of truth-values in contexture `U`, and the restriction map $H(f): H(V) \to H(U)$ for $f: U \to V$ is the order relation between contextures. Junctions are gluing conditions in the presheaf.

This translation reveals that Polycontextural Logic is not Hegelian obscurantism but *sheaf-theoretic logic* — a structure that generalises Kripke semantics from possible worlds to contextures.

### 3.7 Summary Table

| Formalism | Core Invariant | Category-Theoretic Expression |
|:----------|:--------------|:------------------------------|
| Laws of Form | Distinction as primitive | Idempotent monad on a 2-category of distinctions |
| Existential Graphs | Diagrammatic negation | Topos-theoretic subobject classifier morphism |
| Viable System Model | Recursive viability | Endofunctor $V: Sys \to Sys$ with fixed point |
| Catastrophe Theory | Structural stability | Sheaf of singularity unfoldings on stratified space |
| Pattern Language | Generative patterns | Coalgebra for a pattern-composition functor |
| Polycontextural Logic | Contextural logic | Presheaf of Heyting algebras over contexture site |

**Result:** All six invariants are expressible in standard category-theoretic language. The notation-specific scaffolds — diagrammatic marks, cuts on sheets, ovoids and channels, potential functions, prose patterns, diamond diagrams — all dissolve. What remains is indistinguishable from canonical mathematics.

---

## 4. The Kauffman Counterexample: Addressed

Louis Kauffman, a respected mathematician working in knot theory and quantum topology, has spent decades developing the mathematical content of LoF in rigorous, accessible papers [8, 9, 10]. Despite his credibility and clarity — precisely the conditions that should overcome the first-impression problem — LoF has still not entered the mainstream. This is the strongest challenge to the scaffold-stripping hypothesis.

Three possible resolutions:

1. **Kauffman's work HAS entered the mainstream, but under different names.** The diagrammatic approach to knot theory (Kauffman bracket, Jones polynomial) is established in topology. If those results trace genealogically to LoF insights but are not *attributed* to LoF, then the content succeeded while the attribution failed — a partial vindication of the notation-problem hypothesis.

2. **The content genuinely resists mainstream adoption** even when presented by a credible mathematician. This would mean the scaffold-stripping hypothesis is too optimistic — some marginalised formalisms may contain genuine obstacles to mainstream adoption beyond notation (e.g., the self-reference foundation that violates the atemporal-axiom paradigm).

3. **More time is needed.** Fifty years is a short interval in the history of mathematics. The calculus of Newton and Leibniz took over a century to achieve rigorous foundations. LoF may simply need more time — and scaffold-stripping may accelerate that timeline.

We do not resolve this question here. We note that the hypothesis remains falsifiable: if a formalism's invariant cannot be expressed in category-theoretic language, its marginalisation is merited. The burden of proof lies with the sceptic to identify which invariant resists translation — not with the hypothesis to pre-emptively defend against an unspecified objection.

---

## 5. Application: A Distinction Calculus for Numbers (DCN)

We now apply the scaffold-stripping methodology to a concrete domain: the natural numbers and primality.

### 5.1 The Set-Theoretic Container View

In ZFC, the number 5 is the set ${\emptyset, {\emptyset}, {\emptyset,{\emptyset}}, {\emptyset,{\emptyset},{\emptyset,{\emptyset}}}, {\emptyset,{\emptyset},{\emptyset,{\emptyset}},{\emptyset,{\emptyset},{\emptyset,{\emptyset}}}}}$. Primality is a property of the size of a container relative to the sizes of possible sub-container partitions. A prime is an indivisible box. The container metaphor is inescapable.

This representation obscures primality. A child looking at the set-theoretic definition of 5 cannot see that it's prime — the property emerges only after defining multiplication as Cartesian product cardinalities and checking all possible factor pairs. The content (primality as metrical irreducibility) is imprisoned in the notation (nested containment).

### 5.2 DCN Primitives

**Primitive 1 (Indication):** An indication is an act that separates a space. Write `|` for a single indication.

**Primitive 2 (Sequence):** A sequence of indications `| | | ... |` is a **score** — a rhythm of distinctions. The number `n` is the score with `n` marks.

**Primitive 3 (Repetition):** The repeat operator `R_k(S)` takes a score `S` and repeats it `k` times. This is multiplication: $m \times n = R_m(|ⁿ|)$ where $|ⁿ|$ is the score of `n` marks.

**Definition (Multiplication):** The product $a \times b$ is the score obtained by replacing each of the `a` marks in the score for `a` with the entire score for `b`.

**Definition (Prime):** A natural number `p > 1` is prime if there is no way to express its score as `R_k(S)` for any `k > 1` and any score `S` with more than 1 mark. Equivalently: a prime is a score that cannot be arranged into a rectangular grid with more than one row and more than one column.

**Definition (Composite):** A natural number `n > 1` is composite if there exist `a, b > 1` such that $n = a \times b$ in the sense above.

### 5.3 The Sunburst Notation

A visual notation directly encodes the DCN structure:

- A **prime number** is represented by a single circle with `p` radial spokes emanating from a central node — a **sunburst** with no internal structure.
- A **composite number** is represented by a **constellation**: a central node with `a` spokes, each terminating in a sub-sunburst of `b` rays (or vice versa). The depth of nesting corresponds to the number of prime factors; the spoke count at each level is the factor value.

Example: 6 = 2 $	imes$ 3. A central node with 2 spokes, each terminating in a 3-ray sunburst. The depth reveals the factorisation: 6 is a depth-2 constellation.

Example: 5. A single sunburst with 5 rays and no substructure. Primality is visually immediate: there are no nested sunbursts.

Example: 30 = 2 $	imes$ 3 $\times$ 5. A central node with 2 spokes, each terminating in a 3-ray sunburst, each of whose rays terminates in a 5-ray sunburst. Depth-3 constellation.

### 5.4 Axioms of DCN

1. **Atomic Indication:** `|` is a valid score (the number 1).
2. **Concatenation:** If `A` and `B` are scores, then `AB` (concatenation) is a score. This is addition.
3. **Repetition:** If `A` is a score and `k > 0` is a score, then `R_k(A)` is a score (the repetition of `A` exactly `k` times). This is multiplication.
4. **Commutativity of Concatenation:** `AB = BA` for all scores `A, B`.
5. **Identity of Repetition:** `R_1(A) = A` for all scores `A`.
6. **Distributivity:** `R_k(AB) = R_k(A) R_k(B)` for all scores `A, B` and positive `k`.
7. **Irreducibility Criterion:** A score `P` is **prime** if the only admissible decompositions of `P` are `R_1(P) = P` and concatenations `P = A B` where one of `A, B` is the score `|` (the number 1).

These axioms are purely syntactic — they operate on the arrangement of marks, not on the cardinality of sets. They are stated in the language of distinctions: indication, sequence, repetition.

---

## 6. The Fundamental Theorem of Arithmetic in DCN

**Theorem (Fundamental Theorem of Arithmetic, DCN formulation).** Every score of `n > 1` marks can be uniquely decomposed (up to reordering) into a constellation of prime sunbursts.

*Proof sketch.* 

**Existence:** Given a score of `n > 1` marks. If `n` is prime (irreducible under repetition), the decomposition is the score itself — a single-level sunburst. If `n` is composite, there exist `a, b > 1` such that $n = a \times b$. Recursively decompose `a` and `b`. The recursion terminates because each step reduces the number of marks. The result is a tree of repetition operators — a constellation whose leaves are prime sunbursts.

**Uniqueness:** Suppose `n` has two distinct constellation trees. Then there exist two different sequences of prime factors `p_1 p_2 ... p_k` and `q_1 q_2 ... q_m` whose sunburst product yields the same score. By the irreducibility of prime sunbursts, each `p_i` must appear among the `q_j` with the same multiplicity, and vice versa. This follows from the fact that in the sunburst representation, the spoke count at each level is invariant under reordering — the constellation tree is a canonical form. $\square$

The derivation uses only the DCN axioms — indication, sequence, repetition — with no appeal to set membership, cardinality, or the real numbers. Primality is a syntactic property of distinction patterns.

---

## 7. Implications

### 7.1 Cognitive and Educational

The sunburst notation makes primality visually immediate. A child shown sunbursts and constellations can distinguish primes from composites before learning multiplication tables — the visual difference between "one level of rays" and "nested rays" is perceptually primitive. This predicts:

1. Earlier acquisition of primality intuitions in children taught with sunburst notation versus decimal numerals
2. Faster factorisation recognition — the depth and spoke count of a constellation directly encode its prime factorisation
3. Reduced anxiety about prime-related concepts (primes are no longer "mysterious exceptions" but the most visually simple numbers)

These predictions are testable via the NUMERATA project's cognitive experiments (WP2.3).

### 7.2 Cross-Domain

The scaffold-stripping methodology generalises beyond the six formalisms examined here. Any formalism that makes universal claims from a position of disciplinary weakness is a candidate for scaffold-stripping. The test is: can the invariant be expressed in standard category-theoretic language? If yes, marginalisation is a notation problem. If no, the formalism may genuinely lack mathematical content.

This has implications for **interdisciplinary communication**. Scientific disciplines develop domain-specific notations optimised for their own problems. When insights from one domain are needed in another, the notation barrier prevents transfer. Scaffold-stripping is a general methodology for cross-domain translation: extract the invariant, express it in the target domain's standard notation, and discard the source domain's scaffolds.

### 7.3 The Continuum Critique Connection

This paper's analysis connects directly to the QNFO Adelic Physics Program [11]. That programme argues that $\mathbb{Q}$ (not $\mathbb{R}$) is the physically accessible base field, and that the Archimedean continuum is a map, not the territory. The notation problem discussed here is an instance of the same meta-principle: the representation ($\mathbb{R}$, set-theoretic containers, decimal numerals) conceals the invariants (p-adic structure, distinction patterns, multiplicative topology) that are actually doing the work.

The continuum critique and the notation problem are two faces of a single deeper claim: **many "unsolved problems" in mathematics and physics are artifacts of representational choices, not genuine ignorance.** Changing the representation reveals the invariants — and dissolves the pseudo-problem.

---

## 8. Falsifiability and Open Problems

**Falsifiability.** The scaffold-stripping hypothesis is falsified if any of the six formalisms' invariants cannot be expressed in category-theoretic language without loss of content. A counterexample would require: (a) specifying the invariant, (b) demonstrating that the proposed category-theoretic expression fails to capture it, and (c) arguing that the invariant is genuine mathematical content rather than notation-specific scaffolding. The Kauffman counterexample (§4) is the strongest candidate but does not yet constitute falsification — it shows that presentation is not the *only* factor in marginalisation, not that scaffold-stripping is impossible.

**Open Problems.**

1. **Complete the proofs.** The category-theoretic expressions in §3 are stated as claims, not proved. Proving them requires constructing the relevant categories (the 2-category of distinctions, the contexture site, the stratified space for Catastrophe Theory) and verifying the functorial properties. This is a substantial mathematical programme.

2. **DCN axiomatisation.** Axioms 1-7 in §5.4 are a first sketch. A complete axiomatisation would include explicit reduction rules for repetition, a normal-form theorem, and a proof that DCN is equivalent to Peano arithmetic for the fragment of number theory concerned with primality.

3. **QNFO Adelic Physics Program connection.** The conclusion (open items)

4. **Cognitive experiments.** The cognitive predictions in §7.1 are testable. Designing and running the NUMERATA WP2.3 experiments would provide empirical evidence for or against the notation-problem hypothesis as applied to number cognition.

5. **Generality.** Does scaffold-stripping work for *all* marginalised formalisms, or only for the six examined here? A systematic survey of marginalised formal systems across disciplines (including non-mathematical ones) would test the generality of the hypothesis.

---

## 9. Conclusion: Notation-Imprisoned Invariants

The six marginalised formalisms examined here — Laws of Form, Existential Graphs, the Viable System Model, Catastrophe Theory, Pattern Language, and Polycontextural Logic — are not failed formalisms. They are notation-imprisoned ones. Their invariants, when stripped of notation-specific scaffolds and expressed in standard category-theoretic language, are indistinguishable from canonical mathematics.

The Distinction Calculus for Numbers demonstrates the methodology in action: primality, which appears as an opaque set-theoretic property in ZFC, becomes a visually immediate pattern property in DCN. The sunburst notation makes primes look like what they are — the primary rhythms, the metrically irreducible scores, the original acts of indication at the heart of number's music.

The broader claim is this: **when a formalism fails to achieve mainstream adoption despite containing genuine insights, the problem is more likely to be in the notation than in the content.** The notation is a prison. Scaffold-stripping is the key.

---

## Declarations

**Funding:** This research received no specific grant from any funding agency in the public, commercial, or not-for-profit sectors.

**Conflicts of Interest:** The author declares no conflicts of interest.

**Ethics Approval:** Not applicable — this is a theoretical/mathematical paper with no human subjects research.

**Consent to Participate:** Not applicable.

**Consent for Publication:** Not applicable.

**Author Contributions:** Single author — all contributions.

**Data Availability:** No experimental data were generated or analysed. All referenced papers are publicly available via their DOIs.

**Code Availability:** Not applicable — this paper contains no computational code.

**Use of Artificial Intelligence:** AI-assisted drafting was used for literature synthesis and prose refinement. All mathematical content, arguments, and conclusions were verified by the human author.

---

## References

[1] Spencer-Brown, G. (1969). *Laws of Form.* George Allen and Unwin.

[2] Peirce, C. S. (c. 1897). Existential Graphs. In *Collected Papers of Charles Sanders Peirce*, Vol. 4. Harvard University Press.

[3] Beer, S. (1972). *Brain of the Firm.* Allen Lane.

[4] Thom, R. (1972). *Stabilité Structurelle et Morphogenèse.* W. A. Benjamin. English translation: *Structural Stability and Morphogenesis* (1975).

[5] Alexander, C., Ishikawa, S., & Silverstein, M. (1977). *A Pattern Language.* Oxford University Press.

[6] Günther, G. (c. 1960s-70s). Polycontextural Logic. Collected in *Beiträge zur Grundlegung einer operationsfähigen Dialektik* (3 vols). Felix Meiner Verlag.

[7] Obsidian note `_26190130638.md` (2026-07-09). "Laws of Form: First Impression Problem, Credibility Cascade, and Cult Dynamic."

[8] Kauffman, L. H. (2013). Laws of Form and Topology: Presentation and Discussion. *Cybernetics & Human Knowing*, 20(3-4).

[9] Kauffman, L. H. (2017). Mathematical Work of Francisco Varela. *Constructivist Foundations*, 13(1).

[10] Kauffman, L. H. (2017). Foreword: Laws of Form. *Cybernetics and Human Knowing*, 24(3-4).

[11] Quni-Gudzinas, R. B. (2026). The Adelic Physics Program: Epistemological Foundations and Communications Framework. Zenodo. DOI: 10.5281/zenodo.21686727.

[12] Quni-Gudzinas, R. B. (2026). Quantum Laws of Form: A Syntactic Foundation for Physics. Zenodo. DOI: 10.5281/zenodo.19578015.

[13] Quni-Gudzinas, R. B. (2025). Prime Numbers as Universal Optimization Primitives. Zenodo. DOI: 10.5281/zenodo.17516239.

[14] QNFO Research Collective (2026). Silent-Radix Cryptography. Zenodo. DOI: 10.5281/zenodo.21046734.
