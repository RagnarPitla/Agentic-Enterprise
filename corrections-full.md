# Why There Is No Agentic Enterprise

## And what would have to exist before there is one

**Author:** Ragnar Pitla
**Draft:** v2, 4 September 2026
**Status:** WORKING DRAFT. Do not circulate.

**Epistemic key.** Every substantive claim in this paper carries one of four labels.
`[MEASURED]` - verified by direct measurement, method stated.
`[ESTABLISHED]` - supported by a primary source, cited, verified before print.
`[ARGUED]` - reasoning offered, no external evidence yet.
`[SPECULATIVE]` - deliberately beyond current practice. Flagged so a reader can discount it.

Nothing is labelled `[ESTABLISHED]` until its citation has been fetched and read. Claims awaiting
verification are marked `[PENDING]`.

---

## 1. The question

Enterprises have bought agents. Salesforce, Microsoft, SAP and Oracle each publish catalogues of
prebuilt agents `[PENDING - counts and segmentation being enumerated]`. Budgets have been spent.
Pilots have run.

And almost nobody would describe their enterprise as agentic.

That gap is the subject. Not "there are too many agents" - that is a complaint. The question is
why the money did not convert, and what would have to be true for it to convert.

### 1.1 A definition that can be measured

"Agentic enterprise" is currently a phrase people nod at. A paper that does not define it
measurably is indistinguishable from the marketing it criticises.

**An earlier definition is withdrawn.** `[CORRECTED]` It read: *work crosses system and
departmental boundaries without a human relaying it*. That definition is broken, and the
counter-examples are decisive rather than hypothetical. In 1998, FIX protocol engines carried a
trade from buy-side OMS to broker to clearing house to custodian - three corporate boundaries in
twelve milliseconds, no human involved. A Zapier webhook today fires Shopify to SAP to Stripe
across commerce, ERP and finance with no human relay. Both score as maximally agentic under the
old definition. Neither has any agency at all: zero goal-directed planning, zero epistemic
adaptability, and both break the moment an input schema shifts.

The defect is that it defined agency by its **side effect** (no human in the loop) rather than by
its **mechanism**.

> **Working definition.** An enterprise is agentic to the degree that **commitments are
> autonomously formed, monitored, fulfilled, or renegotiated across authority boundaries in the
> presence of unmodelled perturbations and system failures**, without human mediation.

`[ARGUED]` The discriminator is the behaviour under perturbation, and it is observable:

| Automation (STP, scripts, RPA) | Agency |
|---|---|
| Deterministic path execution | Path generated at runtime |
| Fixed environmental mapping | Recovers from unmodelled intermediate failures |
| **Crashes on invariant breach** | **Renegotiates or replans around the breach** |
| Monitors return codes | Closes or escalates the underlying commitment |

This is measurable without new instrumentation: take deployed cross-boundary flows, inject an
unmodelled perturbation - a supplier misses a date, a schema field changes, a credit check fails
mid-flow - and count how many close or escalate the commitment versus how many halt and page a
human. Straight-through processing scores zero on that test, which is the correct answer.

### 1.2 The maturity ladder, and the structural claim

| Level | Behaviour |
|---|---|
| 0 | Assistive. Human does the work; the agent drafts. |
| 1 | Task automation **within one system**. |
| 2 | Cross-system execution, human approves at gates. |
| 3 | Cross-system with autonomous compensation; human on exception only. |
| 4 | Objective-level delegation. |

`[PENDING]` Vendor catalogue classification will establish what share of shipping agents sit at
Level 1. The working expectation is that it is almost all of them.

`[ARGUED]` **No quantity of Level 1 agents sums to Level 2.** Buying more is horizontal motion;
becoming agentic is vertical. This is a structural claim, not a rhetorical one, and it predicts
the observed symptom precisely: many pilots, little production crossing, and value that never
appears because it was always located in the seam.

---

## 2. The diagnosis: commitments are represented, and cannot cross

**The central claim has been narrowed.** `[CORRECTED]` An earlier draft asserted *there is no
representation of the commitment*. That is false, and it is refuted by a single citation:
**ISO 15944-4** standardises the REA ontology for cross-organisational electronic business with
**commitments as first-class citizens**, contracts as bundles of reciprocal commitments, and
business transaction state machines tracking progression from commitment to fulfilment. Obligor,
beneficiary, condition and current state, cross-system, in an international standard, since 2007.

`[ARGUED]` The surviving claim is narrower, harder to dismiss, and better supported by the
evidence in this paper:

> **Commitment representation exists, is standardised, and is deployed - between companies. It
> was never built between departments inside one.**

EDI and RosettaNet PIPs have specified two-party transactions with time-to-acknowledge,
time-to-perform, retries and signed non-repudiable receipts for twenty-five years, at industrial
scale. Nothing of the kind exists between Sales and Operations in the same building.

### 2.1 What an enterprise is

`[ARGUED]` An enterprise is not a set of systems. It is a machine for making promises and
keeping them. Selling is a promise to deliver. Buying is a promise to pay. Employing is a promise
to compensate. Reporting is a promise that you told the truth. Every system of record is a ledger
of promises in some state of fulfilment.

### 2.1a Why the asymmetry exists, and why it matters now

`[ARGUED]` This is the paper's "why now", and it replaces a weaker earlier argument.

Inside a company, **trust was substituted for protocol.** No one needed a signed, dual-held,
non-repudiable record of what Sales promised Operations, because Sales and Operations were
colleagues: shared employer, shared consequences, social accountability, and the ability to be
asked next Tuesday what they meant. Cross-company transactions needed EDI precisely because that
trust substrate was absent.

> **Agents void the trust substitution.**

An agent is not a colleague. It has no career at stake, cannot be socially sanctioned, and cannot
be asked next Tuesday what it meant. The moment both parties to an internal promise are
non-human, the intra-company case acquires exactly the properties that forced the invention of
EDI for the inter-company case.

This argument does not depend on the false claim that commitments were never represented. It
explains the specific gap the evidence supports. And it survives the Suchman critique in section
4.2, because the categorisation is being imposed on **agents**, not on people.

### 2.2 Noun-shaped software, verb-shaped work

`[ARGUED]` Enterprise software modelled the nouns - customer, order, invoice, asset - and very
little of the verbs that carry obligation: promised, owed, overdue, forgiven, renegotiated,
escalated.

> **We built noun-shaped software and we are asking for verb-shaped work.**

**Necessary qualification.** The strong form of this claim is false and must not be published.
Enterprise systems *do* model obligations, extensively and by regulation. An accounts-payable
balance is literally a deferred obligation to an external creditor. SAP's schedule-line table
`VBEP` carries `EDATU` (requested delivery date) and `BMENG` (confirmed quantity) - a concrete
promise to a customer. ASC 606 and IFRS 15 *mandate* tracking performance obligations separately
from invoices. Double-entry bookkeeping is itself an obligation ledger, and REA accounting
(McCarthy, 1982) formalised this forty years ago with its **duality** principle: every economic
decrement must link to a future increment.

`[ARGUED]` **The defensible narrow form, sharpened:** obligations are strictly encapsulated within
local transaction contexts and **cannot maintain identity across authority boundaries.**

The canonical failure is mundane. CRM holds a deal field reading "Delivery: Oct 12". ERP holds an
order line reading "Ship date: Oct 18". These are the *same promise to the same customer*, and
there is no object in the enterprise of which both are projections. Nothing detects the
contradiction, because nothing knows they are the same commitment. An AP liability is legible to
finance; a delivery promise made in a sales conversation, which finance will pay a penalty for,
is legible to no system at all.

The crossing is exactly where the agentic value was supposed to be, and exactly where the
representation stops.

### 2.3 The consequence

`[ARGUED]` Agents operate on records. A record is a row. A commitment is a promise with an
obligor, a beneficiary, a condition, a deadline, and a consequence for breach.

When a salesperson promises a delivery date, that commitment spans CRM (where it was made), ERP
(where it must be fulfilled) and finance (where the penalty lands). No system holds it as one
object. It lives in the gap between them, and the gap is where the enterprise actually operates.

**You cannot delegate a goal to a machine that has no representation of a promise.**

### 2.3a Polarity: promises, not obligations

`[CORRECTED]` Burgess's Promise Theory supplies a correction that changes the design rather than
the citation list. An autonomous agent can only promise about **its own** behaviour; obligations
imposed from outside are less reliable, because only the promiser holds the information and the
agency to keep them.

An *obligation* ledger - one system recording what it says another owes - reproduces exactly the
failure this paper set out to fix: the CRM agent promising a delivery date that ERP never agreed
to. The polarity is wrong.

> The ledger must record **self-promises attributed to the authority that can keep them**, not
> obligations asserted about someone else.

This welds the commitment thesis to the authority thesis: a promise is only recordable by the
authority that owns the state required to fulfil it. Sales does not promise a ship date. Sales
requests one; Operations promises it, or declines.

### 2.3b The hard part is after the breach

`[ESTABLISHED]` Deontic logic supplies a warning that should be stated plainly. **Chisholm's
contrary-to-duty paradox** concerns what one ought to do *having already violated* an obligation
- which is the enterprise's normal operating state. The delivery is already late. Now what?

Representing obligations is the easy half. **Representing what is owed after breach** is a
known-hard problem in the formal literature, not an implementation detail, and any commitment
layer that does not address it will be correct exactly until the first thing goes wrong.

### 2.3c Reconciliation, not data entry, is the expensive part

`[CORRECTED]` An earlier draft assumed the blocking cost of commitment tracking was the burden of
declaring promises, and that agents remove it. Even granting that, someone must **reconcile**
declared commitments against actual world state, and "did we deliver on time?" is genuinely
contested in a large fraction of real cases: partial delivery, changed specification, waived
condition, informal extension. That is judgment, not bookkeeping.

The declaration burden was the visible cost. The reconciliation burden is the real one, and this
paper does not solve it.

### 2.4 Independent convergence on the same point

`[ARGUED]` Two independent lines of reasoning reached this conclusion during the preparation of
this paper. From speech-act theory: agents read the exhaust of commitments rather than the
commitments. From distributed systems: *a message bus carries beliefs, not authority*. "Customer
wants Friday" is not a commitment; to make a cross-authority commitment binding you need atomic
commit, sagas buy compensation rather than atomicity, and irreversible actions have no
compensating transaction at all.

That convergence is the reason this is the paper's central claim rather than a flourish.

### 2.5 Why the fleet exists

`[ARGUED]` "ERP agent" and "CRM agent" are **noun-shaped agents** - each named after a place
where nouns are stored. Hundreds of them is what you inevitably get when you have no
representation of the verb. The fleet is a symptom of the missing layer, not the disease.

---

## 3. What does not exist

`[SPECULATIVE]` throughout this section, deliberately. Each is a research and engineering
proposal, not an observation.

### 3.0 Enterprise systems have no pencil

This is the strongest single item in the section, it was not in earlier drafts, and it partly
supersedes 3.2.

State in enterprise software is binary: written or not written. Ink or nothing. But the thing a
competent human does when acting under uncertainty is act **provisionally** - "I am pencilling
you in for Friday". That creates real, visible, actionable state which other parties can see and
rely on *weakly*, and which evaporates if it is not confirmed.

There are exactly two widespread instances of this, and both are domain-specific hacks nobody
generalised: **the airline seat hold** and **the inventory reservation**.

> **The missing primitive: a universal provisional-write state class.** Every writable field
> supports a third value-state - *provisionally set, by claimant C, expiring at T, visible to all
> readers as provisional* - which is neither a lock (which blocks others) nor a commit (which is
> final), and which auto-reverts unless confirmed.

**Why this is better than the reversibility work in 3.2.** That approach tries to *measure and
gate* irreversibility. This one **manufactures reversibility by construction.** Make the default
write provisional and a large class of agent actions becomes structurally, mechanically
reversible - not because a cost was estimated correctly, but because the substrate reverts them
for free. **No reversibility budget is needed for actions that expire on their own.**

It also answers the objection that killed the continuous budget in 3.2. Provisional state is
*visibly* provisional, so third-party reliance on it is weak by construction - and third-party
reliance was precisely the mechanism that made reversal cost heavy-tailed and non-additive. A
counterparty who saw a provisional date and relied on it anyway bears that risk explicitly.

### 3.0a The warranted dry run

Every mutation interface should expose `predict(mutation) -> effect set, invariants touched,
reversal plan` - and it must be produced **by the owner of the state, not by the agent**, because
only the owner knows its own invariants.

`[ARGUED]` This explains a standing puzzle. Enterprise reinforcement learning is impossible
because there is no simulator; there is no simulator because no system of record was ever asked to
describe what a write would do *before* doing it. Databases already compute this internally to
plan and validate transactions. Exposing it is an interface convention, not a research problem.

### 3.1 An obligation ledger

**3.1 An obligation ledger.** First-class and cross-system: obligor, beneficiary, condition,
deadline, consequence, current state. Workflow engines model steps; this models promises.

**3.2 A discrete reversibility partition in place of permissions.** `[CORRECTED]` An earlier draft
proposed a *continuous* reversibility budget - autonomy governed by expected cost of undo. That
version is withdrawn. Adversarial review found it elegant and operationally fatal, for three
reasons that are not fixable by better estimation:

- **The cost is non-computable ex ante.** True reversal cost depends on downstream reactions by
  external actors who are strategic, not deterministic. An automated 10% credit to an angry
  customer costs 50 dollars to reverse until the customer forwards it to a regulator or an
  industry list, at which point it has set a pricing precedent. Reversal costs in human systems
  are **heavy-tailed**, and an expected-value threshold under fat tails systematically
  underestimates exactly the ruin scenario it exists to prevent.
- **Cost is non-additive.** Reserve parts (10), notify the carrier (20), charge the card (5) - each
  trivially reversible alone. Executed together they trigger a truck roll, an ERP lock that
  starves a priority order, and an immutable customer email. `Cost(A1 U A2 U A3)` is
  super-linear in the parts. An agent checking each step against a local threshold walks over a
  cliff one cheap step at a time.
- **An auditor will reject it outright.** Under SOX 404 or Basel, a control must demonstrate
  non-repudiable determinism. "The model estimated expected reversal cost at 4,200, below our
  5,000 threshold, so it committed" is a confession of a non-compliant control. Probabilistic risk
  pricing is not permitted on financial integrity controls.

`[ARGUED]` **What survives is a discrete, deterministic partition** - and it is stronger than the
permission model it replaces because the tiers are properties of the *action*, not of the actor:

| Tier | Formal property | Runtime |
|---|---|---|
| **Reversible** | a deterministic inverse exists within a bounded window: `f^-1(f(S)) = S` within tau | Autonomous. Rollback token minted into the case ledger |
| **Compensable** | cannot be undone, but has a bounded compensation protocol - credit note, return, reissue | Autonomous **only up to a pre-allocated escrow balance**. Compensation must be tested, not assumed |
| **Immutable** | state escapes the system boundary - wires, emails, filings, physical shipment | **Hard stop.** The model cannot emit the mutation. Out-of-band human sign-off required |

The escrow balance on the middle tier is what makes this operational rather than theoretical: it
converts an unbounded probabilistic judgment into a bounded, pre-funded, auditable quantity.

**3.3 Correction history as an anomaly detector, not as a source of invariants.** `[CORRECTED]` An
earlier draft proposed mining the gates from correction history rather than authoring them. That
is demoted, hard. Three failures, each sufficient on its own:

- **Survivorship (Wald's airplane).** The log records *detected* errors. A billing leak nobody
  noticed emits zero corrections and is marked valid. A model trained on corrections learns that
  uncorrected actions are invariants - and the uncorrected set is precisely where the
  enterprise's entrenched, invisible leaks live. You would be training the agent to reproduce the
  organisation's blind spots with machine consistency.
- **Policy freeze under bandit feedback.** Observe that managers reject discounts above 15%,
  harden `discount <= 15%`, deploy. The agent now never attempts 16%, so no manager is ever asked
  about the exceptional high-margin deal at 16%, so that region of the state space generates no
  further signal, ever. The policy is frozen at the status quo permanently, and the freeze is
  invisible.
- **Non-stationary human actors.** A VP approving an over-limit invoice on 30 September to hit
  quarter numbers was not expressing an invariant. Mining history codifies end-of-quarter panic,
  golf-course agreements and local political deals into immutable machine gates.

`[ARGUED]` **The surviving role is advisory.** A learned model over corrections can say "a human
usually intervenes here, flag it". It can never say "this is a sound corporate invariant".
Explicit invariant authoring cannot be avoided, and this paper should stop implying otherwise.

**A note on why this strengthens the central claim.** The policy-freeze failure exists *because*
the enterprise records only actions taken, never alternatives considered and rejected. A decision
record carrying the alternatives is exactly the counterfactual data whose absence causes the
freeze. The correct response to this objection is not to defend learned invariants. It is to
observe that the objection is another symptom of the missing primitive.

**3.4 The episode as the unit of work.** Not a session, ticket or workflow instance. One
objective, its full causal trace across systems, the commitments it created, its reversibility
state, its outcome. Enterprises have orders, cases and opportunities - all application-local.
**There is no episode table.**

**3.5 Enterprise state addressable for writing.** MDM, data lakes, fabric and mesh were built for
reporting: read-only, stale, analytical. Acting requires a transactional semantic layer with
write-through.

---

## 4. Prior art, stated honestly

`[ESTABLISHED]` The reckoning is now specific, and the conclusion is that **this paper contributes
a synthesis and a mechanism, not the concept.** The concept of computational commitment is forty
years old and was worked out carefully by people who are not cited enough.

| Work | What it solved | Why it did not land |
|---|---|---|
| **Winograd & Flores (1986)**, the Coordinator, ActionWorkflow (Medina-Mora et al. 1992) | Modelled commitment directly: request, promise, counter-offer, decline | Forcing humans to label every message felt like a bureaucratic straitjacket. Critiqued by **Suchman, *Do Categories Have Politics?* (1994)** |
| **REA accounting (McCarthy, 1982; ISO 15944-4)** | Resources, Events, Agents with **duality** - every economic decrement links to a future increment. That link is a commitment | Stayed in academic accounting and niche standards. ERPs flattened REA back into static relational documents |
| **Singh, commitment protocols (1999, 2008)** | Formalised `C(x, y, p, q)` - debtor x owes creditor y condition q under context p - enabling flexible coordination without hardcoded control flow | Required symbolic predicates. Legacy systems emit dirty HTTP payloads, flat files and rows, not predicates |
| **Burgess, Promise Theory (2005, 2015)** | Obligations cannot be imposed externally; an autonomous agent can only emit promises about its own behaviour, which others assess | Descriptive modelling paradigm, not a transaction coordinator |
| **Sagas (Garcia-Molina & Salem, 1987)** | Long-lived distributed transactions with compensating actions | Pure control flow. A saga knows step 3 failed and step 2 must compensate. It has no concept of *who* was promised *what*, or whether the breach is renegotiable |

### 4.1 The genuine delta

`[ARGUED]` Stated plainly, so that no reader has to discover it as a rebuttal:

> This work does not discover computational commitments. It observes that **language models are
> the translation interface that finally makes Singh, McCarthy and Winograd deployable against
> legacy enterprise reality.**

Every one of those programmes failed at the same joint: they required a formal commitment graph,
and the only available way to produce one was for a human to type it. A model can ingest
unstructured email, dirty REST logs, meeting transcripts and PDF contracts, and extract and
maintain the commitment graph that humans were too exhausted to maintain by hand. The blocking
constraint on a forty-year-old correct idea has been removed, and that is a different claim from
having had the idea.

### 4.2 The correction to the Winograd reading

`[CORRECTED]` An earlier draft argued the Coordinator failed because humans found
promise-declaration bureaucratic, that this was a property of the participant rather than the
idea, and that agents do not mind bookkeeping. **That answers the wrong critique**, and if
published as written the first CSCW-literate reader ends the argument in one paragraph.

**Suchman's actual objection** (*Do Categories Have Politics?*, CSCW 1994) is not that declaring
promises is laborious. It is that **imposing a fixed taxonomy of speech acts is an exercise of
power.** Classifying an utterance as a "promise" is itself a political act; the categories encode
a managerial logic optimised for traceability and accountability; and the ambiguity destroyed in
the process was **functional, not defective**.

The "agents do not mind bookkeeping" rebuttal does not touch this. It **inverts on it**: with
agents, classification happens at scale, probabilistically, by a system, with no human present to
contest the categorisation. That does not remove Suchman's objection. It industrialises it.

**The four blockers, scored honestly:**

| Blocker | Removed by agents? |
|---|---|
| Declaration burden on humans | **Yes** - the one genuine win |
| Categorisation as an exercise of power (Suchman) | **No - made worse** |
| Ambiguity is commercially load-bearing | **No** |
| Network effect: useless unless all parties log | **No** |

**The one answer that survives** is in section 2.1a: the categorisation this paper proposes is
imposed on **agents**, not on people. An agent has no professional standing to be diminished by
having its utterance classified, and no interest in strategic vagueness of its own. Suchman's
objection is about what taxonomy does to *humans* in a workplace. Applied to machine-to-machine
promises it loses its force - and applied to human utterances it retains every bit of it. The
boundary must be stated explicitly, and the ledger must not classify human speech without a human
able to contest the classification.

**Ambiguity is load-bearing.** Humans keep commitments vague deliberately. "We should be able to
get that to you around mid-month" preserves optionality, avoids creating a liability, and permits
renegotiation without loss of face. Formalise every exchange into a rigid contract with no slack
and the result is not efficiency - it is brittle cascading gridlock, where a supplier delay a
human would have absorbed silently now propagates as a formal breach through the whole graph.

**Design consequence, not a footnote:** the commitment representation must carry **tolerance as a
first-class field** - a promised range with an escalation threshold rather than a point value, and
a renegotiation path that does not begin with a breach.

---

## 5. The execution architecture

This section is the implementable layer. It is not the contribution; section 2 is. It is included
because a paper that only names a missing abstraction is not actionable.

### 5.1 The error was publishing the wrong object

**CORRECTED.** An earlier draft claimed the error was publication itself. That is false as stated,
and the POSIX/SQL/HTTP counter-case defeats it. Publication of a narrow waist is how a market and
a warranty become possible. The error was publishing **N departmental minds** rather than a waist.

`[ARGUED]` **Criterion - publish and freeze if and only if all five hold:**

1. **Narrow waist.** Many implementations below, many consumers above.
2. **Hides implementation, not authority.** The variation it conceals is *how*, never *who may
   commit*.
3. **Domain-true, org-chart-false.** The interface stays meaningful if Sales is merged into
   Growth.
4. **Conformance without proper nouns.** A conformance test that names no vendor, department or
   model.
5. **Cheaper to freeze wrongly than to renegotiate perpetually.**

Agent catalogues fail 2, 3 and 4. "Sales agent" is a job title, and job titles are not conserved
quantities. Kubernetes published Pod and Deployment, not "Scheduler Agent". Payment processors
published charge and refund, not "Fraud Agent" - fraud stayed internal.

**What should be published instead:** the bounded-context **mutation contract** -
`Invoice.submit(mu)` succeeds iff `V_invoice(s, mu) = commit` - together with the receipt type and
the case type. That is SQL-shaped, an algebra of legal writes. It is not persona-shaped.

The slogan "do not publish the decomposition" must be dropped. Taken literally it forbids
publishing the gates, which leaves an unbounded natural-language oracle as the only product
surface. That is worse than catalogues.

### 5.2 The tiers

| Tier | What it is | Public? | May mutate state? |
|---|---|---|---|
| **Case** | durable work item: identity, authority set, state machine, receipts, wait conditions, compensation cursor. Owns the work across calendar time | **Yes - the case type is the published interface** | Only via gates |
| **Planner** | one general executor, episodic against a case; resolves objective, mounts harness, loads skills, delegates | Yes - the only conversational surface | **No - proposes only** |
| **Skill** | portable procedure; no context of its own; a cache | No | No |
| **Expert agent** | internal specialist, justified only by information firewall or parallelism | **Never** | **No - returns findings and proposals** |
| **Authority gate** | deterministic invariant validator owning one bounded context | Contract published | **Yes** |
| **Joint kernel** | validator for invariants spanning two or more authorities | Contract published | Adjudicates cross-context commits |

**Authority is not a tier.** It is a first-class scope object that parameterizes both the
observation function and the admissible action set, and against which objective, skill and
harness all resolve. An earlier draft smeared authority across two axes; since authority is the
load-bearing concept, that was a structural error.

**Harness** is not action masking. `[CORRECTED]` A harness varies the action set, *the observation
kernel*, the acting identity and credentials, the model and decoding, the context budget, and the
gate. Only the first is masking; the rest are outside the classical decision-process tuple
entirely. The honest object is a **configured execution context**
`h = (A_h, Omega_h, identity, model, budget, gate)`, and the executor is one family `pi(. | s, g, h)`.

> Naming each `h` a product is a projection from configuration space onto job titles.

**When an expert agent is justified `[CORRECTED]`.** The earlier test - "does it need its own
context window?" - is retired. It bets on a decaying constraint; context capacity grows every
year. Three predicates, all required:

1. **Firewall.** Mixing this working set with the parent's would violate authorization or would
   place untrusted content in the same state as a principal that can mutate.
2. **Parallelism.** Independent work genuinely worth a second tape.
3. **Non-mutation.** The output is findings and proposals only.

If 1 and 2 are both false, it is a skill or an in-process tool call, not an agent. Context size is
not on the list.

**The confused-deputy constraint.** A single planner that mounts ERP and then CRM, with untrusted
documents in the same context as privileged tools, is a textbook confused deputy - and this is the
strongest surviving argument for the fleet. It is answered only by an explicit rule, not by
assertion: **the planner never holds two authorities' data and tools simultaneously, and untrusted
content is quarantined behind an expert that cannot mutate.** Without that rule stated and
enforced, process isolation is a real control and the fleet wins the security argument.

### 5.3 Properties the gates must have

`[ARGUED]` **Gates must be adversarial, not subordinate.** A gate that is *called by* the planner
is not a control. Separation of duties requires a component that can refuse the planner and
cannot be argued out of it.

`[ARGUED]` **The mask must be enforced outside the policy.** If the executor computes its own
mask, the mask is a suggestion. The receipt must record *who computed the mask*, not only what
was called.

**CORRECTED - a gate is not an agent.** An earlier draft conceded that a gate able to refuse is
therefore an agent. Reversed. Two different refusals must be distinguished:

- **Policy refusal:** a controller maps observations to act / wait / reject and can be wrong in
  both directions. That is an agent.
- **Invariant refusal:** a pure function `V(s, mu) -> {commit, reject, reason}` with no degrees of
  freedom. That is a typechecker.

Only the second is a gate. If the validating tier is an LLM instructed to be adversarial, the
fleet has been re-derived: N named refusers plus one namer. Manners are not architecture.

**What is expressible deterministically** - algebraic invariants (conservation, bounds, debit
equals credit, quantity non-negative); finite-state constraints (a cancelled order cannot ship);
authorization logic (principal, role, purpose, separation-of-duty sets); schema, idempotency keys
and uniqueness; temporal logic over recorded events on a closed alphabet.

**What is not an invariant** - "a commercially reasonable discount", email tone, "the spirit of
the contract", novel fraud not already a predicate. These are judgments and must live outside the
gate, in one of two forms: a human decision recorded as a signed fact that the gate then checks,
or an expert **proposal** that becomes a fact only when an authorized principal accepts it.

If most real rules appear to require judgment, that is a statement about the current encoding, not
about the business. A 50,000 approval threshold is not a vibe; it is already in the system of
record, or it is a ghost rule that will drift.

### 5.3a The two tiers that were missing

`[ARGUED]` Both holes were found by adversarial review of the four-tier model, and both are
structural rather than cosmetic.

**Local gates do not compose.** Each gate owning one bounded context can accept a mutation that is
locally legal while the planner drives a globally illegal trajectory. Every kernel says yes and
the company is still wrong: CRM records closed-won and ERP never invoices; separation of duties
holds within each system and is violated across them. Sagas compensate *known* reverse actions;
they do not invent the missing cross-context invariant. The four-tier model has no tier whose job
is composition of authorities, and the planner cannot be that tier because it is both forbidden
to mutate and assumed untrusted.

**The mechanism that closes it: shadow-fork escrow.** `[SPECULATIVE - but concrete]` This hole was
identified by one reviewer and the mechanism proposed independently by another, neither seeing the
other's work. The construction:

1. **Agents never hold write credentials to a system of record.** Not scoped ones. None.
2. Systems of record expose **reservation and intent endpoints** to an escrow layer - a temporary
   expiring inventory lock, a conditional hold on an account.
3. The planner submits a **state-delta bundle**, not a sequence of calls. The escrow layer opens a
   **shadow fork** across every affected context simultaneously.
4. A **deterministic** verifier - solvers and rule engines, explicitly not a model - evaluates the
   **joint** invariants over the combined shadow state. Credit *and* inventory *and* margin *and*
   separation of duties, together, before anything materialises.
5. On pass: two-phase atomic materialisation across all systems, with a signed receipt. On fail:
   the fork evaporates, every reservation expires, **no production state was ever touched**, and a
   structured breach reason returns to the planner - "failed ERP invariant: margin below 12%".

This is what makes the joint kernel implementable rather than aspirational, and it inverts the
usual safety posture. The planner may be as probabilistic, creative and wrong as it likes, because
its output is a *proposal over a fork*, never a write. Correctness is enforced at materialisation
by deterministic code over joint state.

> The obligation ledger stops being a passive historical table and becomes an active transaction
> firewall.

**Honest limits.** This requires systems of record to expose reservation semantics, which most do
only partially and some not at all. Where a context cannot be forked, it must be sequenced last
and treated as immutable-tier. That constraint is real and should be stated rather than designed
around.

**The model was a call stack; enterprises are standing processes.** Plan, load procedure, isolate
thought, commit - that is invocation structure. Nothing in it owns a case across calendar time.
Skills have no context, experts cannot mutate, gates only validate, and the planner is a single
run. But a supplier-communications product exists because something must wait, wake on a message,
hold an SLA, survive process restart, and still be the same work item. That is **temporal
ownership**, not application decomposition.

The missing object is a durable **case**: identity, authority set, state machine, receipts, wait
conditions, and a compensation cursor. Planner invocations are events against that case.

> **The public surface is the case. The planner is episodic against it.**

**Idempotency of intent.** Compensation owned by the mutating gate is undefined unless the
business operation has an identity independent of the model run. Planners retry. Without an
idempotency key on the case and mutation type, a receipt records *a* run rather than *the*
operation, and rollback either double-applies or silently no-ops.

**Honest concession.** Workflow and BPM engines already have case identity, wait states and
compensation cursors. This paper cannot claim to have invented them, and an earlier draft came
close to describing their inner loop while declaring the rest of the machine nonexistent. The
genuine delta is narrower and is stated in section 2: those engines record what happened to a
case, never **why it was decided** - no authority, no alternatives, no revisit condition, no
reversibility budget.

### 5.4 Every run carries a machine-checkable acceptance predicate

`[ARGUED]` This is a stronger and more defensible engineering claim than "one executor", and it
is independent of the decomposition argument. A checkable done-condition moves the system from
open-ended generation to search against a verifier, which is the regime in which agentic systems
have actually worked.

### 5.5 A note on the word "orchestrator"

Every major vendor ships one, and it is the product sold to reconnect the fleet.

> An incumbent orchestrator **routes between sealed products it cannot see into**. The planner
> proposed here **composes parts it fully controls**. The first is a broker across opaque
> boundaries; the second is a compiler over transparent ones.

---

## 6. Evidence

### 6.1 The selection tax `[MEASURED]`

**Scope limit, stated before the numbers.** `[CORRECTED]` This census measures a coding-assistant
skill library: markdown procedure files, symlinks, token menus. Vendor "agents" are commercial
SKUs carrying data gravity, identity, SLA and warranty. These are different objects. The census is
evidence **about skill libraries and progressive disclosure**. It is not a natural experiment on
enterprise agent catalogues, and using it as one would be decoration with a spreadsheet. Every
number below is scoped accordingly.

Measured 4 September 2026 on a single practitioner's installed skill library, using a frontmatter
parser with four control assertions, and a real tokenizer rather than a character estimate.

| Quantity | Value |
|---|---|
| Copilot `SKILL.md` files / unique names | 309 / **308** (`mia-video` duplicated) |
| Claude `SKILL.md` files / unique names | 249 / 249 |
| Names in **both** | **249** |
| Only in Copilot / only in Claude | **59 / 0** |
| Always-loaded selection metadata | 105,581 chars, **22,312 tokens** (cl100k, measured) |
| All skill bodies (frontmatter stripped) | 2,903,213 chars |
| Body-to-metadata char ratio | **27.5x** |
| Untouched in 90 days | 196/309 = **63.4%** by `mtime` |
| Broken symlinks | **19 in each directory** |

**The number to cite is the absolute tax, not the ratio:** approximately 22,000 tokens of
always-on menu charged to every run, including runs that require no skill at all, describing
capabilities the majority of which have been untouched for a quarter.

**What `mtime` does and does not show.** `[CORRECTED]` 63.4% is *not edited* in 90 days. It is not
*not invoked*. No invocation telemetry was collected, so the staleness claim is about maintenance,
not usage, and the paper should not have been ambiguous between them.

**Two corrections of record on this table.** `[CORRECTED]`

An earlier draft reported 19,437 tokens and a 39x ratio. Both were wrong: the parser captured only
the first line of multi-line YAML descriptions, under-counting metadata by 35%. The error passed a
non-emptiness check because every skill returned *some* description. A non-emptiness guard detects
total blindness, never partial blindness, and partial blindness is the reachable failure.

The corrected draft then reported **274 shared names and 25 exclusive to one side**. Those numbers
are *arithmetically impossible* and should never have survived: an intersection of two sets cannot
be 274 when one of the sets contains 249 elements. The figure was a union computed as if it were an
intersection. Re-measurement gives 249 shared, 59 Copilot-only, 0 Claude-only. **A reviewer caught
this by re-running the measurement; no amount of re-reading the prose would have.**

**A finding the corrected measurement produced that neither draft had.** Zero skills exist only on
the Claude side. One library is a **strict subset** of the other. The "two harnesses" framing that
opened this work was weaker than stated: there is one library and one partial mirror of it.

**A control that failed for the wrong reason, recorded because it is the point of the paper.** The
first verification run asserted that the `de-slop` skill's description contains the word "slop." It
does not - the word appears in the name and the body, never the description. The control fired,
correctly reporting that my assumption was wrong, but my assumption was about the *control*, not
about the data. A control must assert something already independently verified, or it fails for its
own reasons and teaches nothing.

**A claim weakened, not withdrawn.** `[CORRECTED]` An earlier draft reported 28 description pairs
above 0.30 Jaccard similarity. A reviewer's independent implementation produced 48. Neither is
wrong; the count is tokenizer- and stop-word-dependent and therefore **not a robust quantity**. The
near-duplicate phenomenon is real and the worst pair remains an exact 1.00 - a dated backup
directory loaded as a live skill. The *count* is withdrawn as a citable number.

**A claim withdrawn.** An earlier draft argued a duplication tax across two harness directories.
Direct measurement refutes it: 156 of 309 Copilot entries and 161 of 249 Claude entries are
symlinks, with 160 shared realpaths - the same file on disk, not two copies. Genuine divergence
is 7 forks out of 249. The symlink strategy is working, and the paper will not claim a problem
its own data refutes.

### 6.2 The partition-quality argument `[ARGUED]`

The complexity-theoretic argument attempted in an earlier draft - that siloed agents constitute a
Dec-POMDP and are therefore NEXP-complete rather than PSPACE-complete - **is withdrawn.** Those
results concern computing an optimal policy offline over a known model. No system in this stack
does that; an LLM performs greedy, myopic, single-step selection with no transition model. Citing
the gap between two complexity classes that neither architecture inhabits is a category error.

The replacement is narrower and computable:

> A decomposition is a **partition of the write-dependency graph**. It is good to the degree that
> it induces **transition independence** - that it cuts near a minimum cut. Application-shaped
> partitions are chosen by vendor boundary and are **uncorrelated with the cut structure of the
> business process**.

`[PENDING]` Transition-independent decentralised MDPs are reported to be materially easier than
the general case. Citation to be verified before print.

This version is falsifiable, computable from real ACLs and change logs, and immune to the
objection that the agents can talk to each other.

### 6.3 The atomicity argument `[ARGUED]`

A shared message bus is not equivalent to shared state, and the reason is not information - it is
atomicity. A bus carries beliefs; it does not carry authority. Sagas provide compensation, not
atomicity, and irreversible actions have no compensating transaction.

Which yields the formal statement of the authority thesis:

> **Draw boundaries so that irreversible effects are contained within a single authority, because
> cross-authority irreversibility can be neither atomically committed nor compensated.**

`[ARGUED]` This is the same invariant as Simon's near-decomposability, DDD aggregate roots, and
the ACID transaction boundary, now applied to probabilistic actors. It should be presented as
that, not as a novel discovery.

---

## 7. Where this breaks

**7.1 Separation of duties, and it is close to fatal.** A single executor holding both
capabilities - even masked per run - relocates the control boundary into masking logic written by
the controlled party and running in-process with the thing it constrains. Auditors do not accept
"the same actor holds both privileges but only uses one at a time". Physically separate
principals fail closed and fail independently; a logical mask does not.

The available answer is per-run, short-lived, externally minted scoped credentials, so the
executor never holds the union. That is real architecture - **and it reintroduces the per-scope
identities and permission models the paper called the tax of the fleet.**

**7.2 The unexamined empirical assumption, which may be fatal to the economics.** The cost
argument assumes distinct authority scopes are **fewer** than applications. This has not been
measured and is probably false: real ERP permission models are finer-grained than "ERP" - an AP
clerk is not a GL accountant is not an MM buyer. If write-scopes outnumber applications, "cost is
linear in N" survives the refactor with a larger N.

What survives regardless, and what the paper should claim: **you do not eliminate N. You factor
the common runtime out of N** - one eval harness, one audit format, one lifecycle, one receipt
schema. Valuable, and considerably more modest than "the unit of decomposition is wrong".

**Required before publication:** measure the ratio of distinct write-scopes to distinct
applications in one real tenant.

**7.3 The Bitter Lesson, turned on this paper's own proposal.** A hand-authored skill library is
hand-crafted feature engineering wearing a different hat, and the telemetry in section 6.1 is the
decay signature of a hand-maintained knowledge base. Both arms are transitional: the fleet
hard-codes decomposition, the library hard-codes procedure.

`[ARGUED]` The defence, which is not the weak one about proprietary data: **the Bitter Lesson is
conditional on the ability to scale experience, and enterprise operations violate that condition
about as hard as any domain.** Self-play produces unbounded, free, safe, perfectly-scored
trajectories. Enterprise transitions are expensive, unsafe because irreversible, slowly scored,
and non-stationary because the environment is other people's adapting policies. Compute does not
substitute for experience one is legally and physically forbidden to collect.

Note that this defence and the authority thesis are **the same claim about irreversibility**,
which is a point in favour of both.

**The audit this implies, to be run on all 309 skills:** could a sufficiently capable model derive
this from general competence plus the current state of the world? If yes, it is compressible
procedure with a known expiry. If no, it is **local fiat** - "discounts above 15% require VP
approval" is a specification, not knowledge - and it should not be a markdown file competing for
retrieval attention. It belongs in a machine-readable constraint store enforced at the harness.

**7.4 The mundane steelman.** The agentic enterprise may not be blocked on any missing
representational layer at all. It may be blocked on data quality, authentication, latency, cost,
liability, or models simply not yet being reliable enough - in which case the commitment layer is
an elegant abstraction nobody needs.

### 7.1 The mundane steelman, stated at full strength

`[ARGUED]` This is the strongest objection to the entire paper, and it deserves to be put in its
best form rather than a convenient one. **The enterprise is not waiting for a philosophical
revolution. It is waiting for three boring things, none of which is a commitment ontology.**

**1. Write reliability arithmetic.** A model that is 99% reliable is economically unusable for
unguarded writes. At 100,000 transactions a day, 1% is **1,000 corporate state corruptions per
day**. Untangling one erratic dirty row costs more human labour than having a person type the
transaction correctly in the first place. Enterprises keep human relays not because humans are
accurate, but because **humans fail in predictable ways and carry legal liability**.

**2. The identity vacuum.** Enterprise systems authenticate identities - OAuth, Kerberos, service
principals. When an agent acts, whose identity does it use? A service account destroys audit trail
and non-repudiation. Impersonating the user bypasses separation of duties. The infrastructure for
**delegated, scoped, short-lived, non-human cryptographic identity** does not exist in most
estates. This is the same problem section 7 already flagged for the single executor, arriving from
the opposite direction.

**3. Data rot and semantic drift.** SAP field `ZZ_CUST_FLAG_3` was defined in 2004 by a contractor
who left in 2008, and when set to `X` it silently overrides the delivery date in a batch job
nobody has read this decade. Humans navigate this by folklore. An agent reading schemas, standard
APIs or a naive semantic layer will confidently produce wrong answers, because **the enterprise's
operational truth does not live in its schema definitions.**

**4. Legal discoverability, which kills the product before IT sees it.** `[ARGUED]` A ledger
recording *"obligor: Sales; beneficiary: ACME; deadline: Friday; consequence: 2% credit"*
manufactures **discoverable evidence in litigation** that does not currently exist. Enterprises
keep commitments vague partly to avoid creating liability. **Legal will kill the commitment
ledger, not the CTO**, and this paper has no answer to that objection. The nearest available
mitigations - privilege scoping, retention limits, recording tolerance ranges rather than point
commitments - are untested and would need counsel, not architects.

**What this paper owes in response.** Points 1 and 2 are conceded as real and are partly *answered*
by the architecture rather than opposed by it - the shadow-fork escrow in section 5.3a exists
precisely because write reliability cannot be assumed, and scoped ephemeral identity is a stated
prerequisite rather than a detail. Point 3 is conceded without mitigation: it is the strongest
single argument in the objection, it is orthogonal to everything proposed here, and no commitment
representation repairs an estate whose real rules live in undocumented batch jobs.

The honest position is that this paper describes what must exist *if* those three constraints are
relieved, and that it is not evidence they will be.

### 7.2 The decay objection, and the only answer to it

`[ARGUED]` This is the strongest single argument against the whole thesis, and it is historical
rather than theoretical.

**Every semantic middle layer ever attempted decayed.** Master data management, enterprise data
warehouses, canonical data models, ESB canonical schemas, enterprise ontologies, data mesh. Each
was elegant, each was correct in the abstract, and each degraded into a stale, partially
populated artifact within roughly two years, because nothing forces a derived layer to stay true.

An obligation ledger is a canonical semantic layer **with a deadline attached**, which makes it
worse rather than better. A stale MDM record is merely useless. **A stale obligation is actively
harmful**: it fires alerts for promises already renegotiated, and stays silent on promises never
logged.

**There is exactly one answer, and the entire proposal depends on it.**

> The commitment ledger is **not a read-side semantic layer. It is a write-side capture
> mechanism.**

Its justification is not that it helps agents reason. It is that it **captures information at the
moment of creation that is otherwise destroyed.** MDM decayed because it was a *copy* of state
maintained separately from an original that kept moving. A commitment written at the instant of
promising, as a side effect of the promising act, is not a copy - **it is the original.**

**The load-bearing design rule:** the ledger must be the system of record for the promise, written
at the instant of the promise, or it will decay exactly like MDM. Every derived layer decays.
Only originals survive.

### 7.3 The irreducible core

`[ARGUED]` This is also the honest reply to the Bitter Lesson pointed at this thesis - the
objection that a sufficiently capable model needs the substrate a human uses, not a better one,
making the commitment layer a crutch for an unreliable actor.

> **Information never recorded cannot be recovered by a better model.**

If a salesperson said "Friday" on a call and nobody wrote it down, no amount of capability
retrieves it. That is not a claim about model quality, now or ever. It is the one part of this
proposal that scaling cannot dissolve, and the rest of the argument should be built on it rather
than on the fleet-versus-planner question.

### 7.4 The contradiction at the centre of the original thesis `[CORRECTED]`

The sharpest objection this paper received is not empirical. It is that the argument refutes its own
headline.

> If authority is genuinely the right boundary, then **multiple independent authorities imply
> multiple principals.** The authority thesis therefore does not entail one executor holding broad
> rights. It entails an unprivileged planner coordinating several narrow, independently authorised
> executors - which is a multi-agent architecture in every security-relevant sense.

That is correct about the slogan, and the slogan is dead: "we do not need hundreds of agents, we need
one agent" is wrong as stated.

**But the objection proves less than it appears to, and the difference matters.** It moves from
"multiple authorities imply multiple principals" to "therefore this is a multi-agent architecture in
every security-relevant sense." The qualifier is doing enormous work. In the security sense the
conclusion is right. In the *cognitive* sense - which is the sense the thesis was about - it does not
follow, because **a principal is not an agent.**

A principal is an identity that holds authority. An agent is a locus of decision. One process
routinely acts under many principals, and we do not describe it as many processes: `sudo -u` does
this, a connection pool with per-request credentials does this, OAuth token exchange exists to do
exactly this, and a web server serving ten thousand authenticated users is not ten thousand web
servers. Multiplicity of authority requires multiplicity of *credential*. It does not require
multiplicity of *policy*, of *control loop*, or of *deployed artefact*.

So the two claims are on different axes and both survive:

| Axis | Claim | Status |
|---|---|---|
| **Authority** | Must be partitioned, narrowly, per principal, outside the model | **Reviewer is right** |
| **Cognition** | Should not be partitioned by application or department | **Thesis is unrefuted** |

The reviewer refuted a decomposition claim about credentials. The paper was making one about
cognition. What dies is the word "one agent"; what survives is *do not cut the thinking along the
vendor's seams, and never let the thinker hold the credential.* Section 5 was already built that way.
The correction is to the headline, not to the architecture.

Five specific reasons the specialised agent wins, each of which survives the whole argument:

**Separation of duties.** A controller that can both initiate and approve a transaction breaks the
control structurally. "The model is instructed not to self-approve" is not separation of duties; it
is a prompt. NIST SP 800-53 Rev. 5 AC-5 and AC-6 require genuine separation and least privilege.

**Confused deputy.** If one executor holds the union of ERP, CRM, payment and communications
privileges, any injected or misclassified request inherits the union blast radius. This is the
Saltzer and Schroeder complete-mediation failure with a language model in the middle.

**Common-mode failure.** One shared model, prompt, resolver, registry or gateway fails across every
business process at once. Separate agents are bulkheads: independent rollback, model diversity,
bounded deployment radius.

**Information barriers.** Some controls prohibit *observation*, not just action. A mask over the
action space does not prevent cross-domain memory contamination or disclosure. That can require
physically separate execution contexts, not one context with a filter.

**Ownership.** Accountable control owner, on-call rota, attestation, incident response, rollback
authority, change approval. A single shared executor becomes an organisational commons with no
unambiguous owner. This is not Conway's Law as pathology; it is Conway's Law as a control.

The design rule that survives is a statement about *where the mask is computed*, not about how many
agents there are:

| | |
|---|---|
| **Fatal** | `K_t` = the set of capabilities chosen by the model |
| **Defensible** | `K_t` = `Gamma(authenticated requester, workflow state, approvals, policy)` |

where `Gamma` is a deterministic policy decision point outside the model. **The model may request
authority. It cannot grant it.** Every architecture in section 5 is an attempt to build `Gamma`; the
paper is better described by that formula than by any claim about agent count.

**One further point, which the reviews scored as a refutation and which is better read as the first
rigorous statement of the claim.** `[CORRECTED]` I argued that skill selection necessarily degrades
as the library grows. That is too strong: no theorem says so. The governing quantity is not global
library size `N` but the **active branching factor** - how many options are applicable in the current
state - and the confusability of those options. A library can hold a million options with disjoint,
machine-checkable initiation sets and still present exactly one choice.

Fano's inequality gives the real bound. With `Z` the correct skill among `N` and `X` the task
evidence:

> `P_e >= 1 - (I(Z;X) + 1) / log N`

Error rises with `N` **only if the task representation supplies bounded information while the library
grows.** If typed preconditions make `I(Z;X)` grow with `log N`, it need not rise at all.

**Read carefully, this is not a refutation - it is the thesis, made checkable.** The bound converts a
hand-waved intuition into an empirical question with a measurable answer: *does `I(Z;X)` grow with
`log N` in real libraries?* And this paper happens to have measured the input to that question. In
the surveyed corpus the selection evidence is **prose descriptions written by hand**, with
near-duplicate pairs up to an exact 1.00 and no typed preconditions anywhere. Prose written
independently by the same author does not carry information that grows with the logarithm of the
library size. So the condition under which Fano predicts rising error is the condition that actually
holds, and the reviewer supplied the theorem that makes the paper's claim testable rather than
rhetorical.

The honest correction is therefore narrower than "refuted": **the degradation is contingent, not
necessary, and the contingency is a design choice nobody is currently making.** Build typed
preconditions and the ceiling lifts. Ship 309 prose blurbs and it does not.

This also separates two things the paper had run together: **progressive disclosure reduces token
cost; it does not reduce selection ambiguity.** Different problems, different remedies - preconditions,
typed capability matching, hierarchy, deduplication, abstention and downstream verification for the
second.

### 7.5 Where the reviews overreached `[ARGUED]`

Four adversarial reviews produced roughly thirty reversals, and a paper that logs all of them without
ever defending one has stopped being a paper and become a transcript. Two of the strongest-sounding
objections do not survive contact.

**"The one-executor thesis is unfalsifiable, because a harness that swaps model, prompt, memory and
permissions can emulate any specialist. It is a universal host."**

The premise is true and the conclusion does not follow. A general-purpose CPU can emulate any ASIC;
that did not make forty years of computer-architecture claims unfalsifiable. It relocated the
falsifiable content from the capability set to the **cost model** - transistors, watts, latency,
yield - which is where it always lives for an architectural claim.

More decisively: **the objection is symmetric, and therefore proves too much.** N specialised agents
can emulate one generalist by routing everything to the fattest one. Any architecture with sufficient
configuration can emulate any other. If that were disqualifying, no architectural proposition in
computing could ever be tested, including the fleet proposition this paper is arguing against. What
the objection correctly establishes is that *capability parity is the wrong outcome variable*. The
testable claims are about cost, drift, blast radius, governance surface and time-to-change - all of
which section 8.1a now measures, and none of which a universal host wins by default.

**"The census supports a registry governance problem, not an architectural one."**

Conceded on its own terms, and then it opens a door the reviewer did not walk through. If it is a
governance problem, the interesting question is *why the governance failed*, and the data answers it
in a way that is not a governance story at all. See section 7.6.

### 7.6 The finding nobody asked for: the registry has no garbage collector `[ARGUED]`

The census was built to measure a selection tax. Read a second time it measures something more
specific and, I think, more useful.

| Signal | Value | What it indicates |
|---|---|---|
| Untouched in 90 days | 196 of 309 | Nothing prunes on disuse |
| Broken symlinks | 19 per directory, both sides | Nothing prunes on dangling reference |
| Worst duplicate pair | **1.00** - a dated backup folder loaded as a live skill | Nothing prunes on supersession |
| Claude-only skills | **0** of 249 | One side is a pure accretion of the other |

Four independent decay modes, and **not one of them has a collector.** The library did not grow to
309 because 309 capabilities were needed. It grew to 309 because nothing has ever been removed. There
is no deletion event anywhere in the lifecycle: not on disuse, not on breakage, not on supersession,
not on merge.

This reframes the sprawl argument, and away from the version I started with. The problem is not that
someone designed a fleet badly. **It is that capability registries are allocated and never freed**,
which is a problem the industry solved for memory in the 1960s and has not noticed it has again.
Reference counting, reachability tracing and tombstones are all sitting there unused.

And then the reason they are unused turns out to be the subject of this entire paper.

> **You cannot garbage-collect a capability registry, because there is no reachability graph.**

Reachability requires knowing which live objectives reference which capabilities. That graph does not
exist, and it does not exist because **objectives are not durable objects** - they are prompts,
tickets, conversations and intentions that evaporate at the end of a session. A skill cannot be shown
to be unreachable because nothing durable was ever pointing at it in the first place.

So the two halves of this paper are one finding, which I did not see until the measurement was
corrected:

- Work does not cross boundaries autonomously, because the commitment has no durable identity.
- Capability libraries grow without bound, because the objective has no durable identity.

**Same missing object. Two symptoms.** The sprawl everyone complains about and the non-agentic-ness
everyone complains about are not two problems that happen to co-occur in the same slide deck. They
are the presenting symptoms of a single absent primitive, and that is the strongest argument in this
paper for building the thing rather than buying more of the other thing.

It also yields a cheap, immediate test that requires no architecture at all: **instrument invocation,
then delete everything with zero invocations and zero inbound references for two quarters.** If the
library can survive that, the reachability graph is latent in the telemetry and can be made explicit.
If nobody dares run it, that fear is the finding.

---

### 8.1 The decisive experiment: cliff versus smooth

`[ARGUED]` This is the experiment that makes the whole thesis empirical rather than aesthetic, and
it must be run **before publication**. It exists because the mundane thesis in section 7.1 and the
representational thesis in section 2 make **different, cheaply distinguishable predictions.**

| Thesis | Prediction |
|---|---|
| **Mundane** (it is a reliability problem) | Cross-boundary autonomous completion rises **smoothly** with model capability. No discontinuity at authority crossings |
| **Representational** (this paper) | Within-boundary autonomy improves with capability and then **plateaus at the crossing** - a cliff that does **not** move as models get better, because the missing information was never recorded |

**Method.** Plot autonomous completion rate against the number of authority boundaries a task
crosses, holding model capability fixed. Repeat across model generations.

**Reading the result.** Smooth decay that lifts with each model generation means the mundane
thesis wins and the commitment layer is decoration. A cliff at the first crossing that stays put
as models improve means the layer is real.

This is the single most important open item in the paper. Everything else is subordinate to it.

### 8.1a Why the experiment above is not sufficient `[CORRECTED]`

The cliff-versus-smooth design tests the *representational* claim. It does not test the
*architectural* one, and a reviewer showed that the architectural claim is, as written, **not
falsifiable at all**:

> Because the harness may select the model, the prompt, the memory, the permissions and the skills,
> "one executor" can emulate every specialised agent. It becomes a universal host rather than a
> substantive architectural claim.

This is correct and it is the most serious methodological defect found in this work. A thesis that
cannot lose is not a thesis. The repair is to constrain the shared-executor arm so that it is a real
commitment: **one policy and model, one control loop, one memory architecture, one resolver, and no
complete specialist policy smuggled in under the name "harness."** Without that constraint, any
result confirms the thesis, which is why the earlier draft found it so easy to believe.

**A second defect: the naive A/B is confounded.** "Many agents versus one agent" mixes routing,
policy specialisation, authorisation and deployment topology into a single comparison. The arms have
to separate them:

| Arm | Execution | Routing | Authority |
|---|---|---|---|
| A1 | Specialised controllers | Deterministic external router | Static narrow principals |
| A2 | Specialised controllers | LLM router | Static narrow principals |
| B1 | Shared executor | Flat skill menu | Out-of-band, task-scoped |
| B2 | Shared executor | Hierarchical retrieval | Out-of-band, task-scoped |
| **B3** | Shared executor | **Oracle skill and harness** | Out-of-band, task-scoped |
| C0 | Shared executor | No skill at all | Out-of-band, task-scoped |

**B3 and C0 are the arms that make the result readable**, and the earlier design had neither.

- If forcing the correct skill and harness into the shared executor **recovers** performance,
  selection was causal.
- If it does **not**, the benchmark is measuring execution competence or context interference, and
  the entire selection argument is measuring the wrong thing.
- If **C0, with no skills at all**, performs as well as the full library, the library is not
  contributing and the selection tax in section 6.1 buys nothing.

That last line is the control this paper most needed and did not have. A census of a skill library
proves the library is expensive. It says nothing about whether the library *works*. C0 is the arm
that could show 22,312 tokens of always-loaded metadata purchasing zero measured benefit - and on
the evidence gathered here, that outcome is not ruled out.

**Two distractor regimes, swept independently.** Orthogonal distractors raise `N` without raising
local confusion; hard negatives share terminology and preconditions. If only hard negatives degrade
performance, the ceiling is semantic entropy and pruning the library is the wrong remedy. Vary
library size, active branching factor, confusability, description length, metadata budget and target
position separately - the earlier design varied only the first and would have attributed everything
to it.

**Score state, not labels.** Verified postconditions in a simulator, plus unauthorised capability
exercise rate at the enforcement point, separation-of-duty violations, and mutation blast radius at
tail percentiles. Exact skill-label accuracy is the wrong primary metric: several skills may be
equivalent or composable, and a label-based score marks a correct outcome wrong.

### 8.2 Standing kill criteria

| Claim | What kills it |
|---|---|
| Catalogues are module-shaped | Vendor catalogues turn out to be segmented by business process |
| Level 1 does not sum to Level 2 | A production example of cross-boundary autonomy assembled purely from single-system agents |
| Commitments cannot cross departmental authority | A shipping intra-enterprise commitment protocol with dual-held non-repudiable state |
| Authority scopes are fewer than applications | Measurement in a real tenant shows write-scopes outnumber applications |
| Selection is not the ceiling | Skill-selection accuracy holds flat as library size grows |
| Harness matters more than model | Scaffold-controlled studies show negligible harness sensitivity |
| Provisional writes are the missing primitive | A tenant adds provisional-write semantics and cross-boundary completion does not move |

**Secondary experiment - the selection ceiling.** Measure selection accuracy against library size N
with distractors, on a real corpus. Negative control: purely intra-domain tasks requiring no
crossing. If the single-planner arm underperforms on those, resolver overhead is injecting
entropy and the measurement is reporting cost rather than capability.

### 8.3 The metric

`[ARGUED]` Boundary-crossing completion rate, refined so that scripted automation cannot score on
it:

> **Agency = (novel exceptions resolved without human relay, weighted by deviation from the
> specified path)  x  (1 - subsequent reversal rate at 30 and 90 days)**

The first factor excludes straight-through processing, which resolves no novel exceptions. The
second excludes an agent that closes cases by doing the wrong thing quickly, which is the failure
mode any single-factor completion metric rewards.

---

## 9. How we get there

Diagnosis without a path is commentary. This section is the path, ordered so that **each phase
pays for itself before the next one starts** - which is the only sequencing an enterprise will
actually fund.

### 9.1 The unlock: you do not build the decision layer, you stop discarding it

`[ARGUED]` The enterprise already produces decisions and throws them away. Every approval,
override, exception, escalation, credit note and manual reversal is a decision record being
discarded at the moment it is made. The first move is capture, not construction. This matters
because it removes the usual objection - that a new substrate requires a transformation programme
before anything works.

### 9.2 The six phases

**Phase 1. Record the decisions you already make.** No agents involved. For the highest
consequence decision types - approvals, exceptions, overrides - capture objective, authority
under which it was taken, alternatives considered, chosen action, expected consequence,
reversibility window, and the condition under which it should be revisited.
*Pays off immediately:* the organisation can answer "why did we do that" for the first time, and
audit cost falls. Value with zero AI.

**Phase 2. Make commitments first-class, but only where they cross authority.** Not every
promise - only those made in one authority and owed by another. The delivery date promised in CRM
that ERP must fulfil and finance pays a penalty for.
*Pays off:* promise breach becomes visible before it occurs, which is a profit-and-loss number
rather than an architecture argument.

**Phase 3. Classify every action type as reversible, compensable, or irreversible.** A one-time
taxonomy exercise over the existing action catalogue.
*Pays off:* the organisation learns where anything at all is safe to act. This is a governance
artifact, and it is worth producing whether or not agents ever arrive.

**Phase 4. Build the gates before the agents, and validate them against humans.**
`[ARGUED]` This inverts the standard order, deliberately. The usual sequence is to build the agent
and then retrofit controls. Instead, build the deterministic invariant validators first - mined
where possible from the correction history captured in Phase 1 - and run them against *human*
actions.
*Pays off:* controls are proven against real human error, where ground truth already exists and no
new risk is introduced. The argument is simple: a gate that cannot catch a human error will
certainly not govern an agent.

**Phase 5. One planner, one crossing.** Select a single cross-boundary process. The planner reads
everywhere, proposes everywhere, and mutates only through gates.
*Pays off:* boundary-crossing completion rate - the metric proposed in section 1 - moves for the
first time.

**Phase 6. Widen by reversibility, not by department.**
`[ARGUED]` The standard expansion path is organisational: sales, then service, then finance. The
correct axis is reversibility. Extend autonomy first over everything reversible, then over the
compensable with receipts and compensation tested, and never over the irreversible without a
human at the gate.
*Pays off:* autonomy expands along the axis that actually tracks risk, rather than along the org
chart, which tracks nothing relevant.

### 9.3 Two contrarian commitments

Both of these are load-bearing and both will be argued with:

1. **Gates before agents, validated on humans.** Controls are cheapest to prove where ground truth
   already exists.
2. **Expand by reversibility, not by department.** This is the operational expression of the whole
   thesis: the org chart is not a risk boundary, and reversibility is.

### 9.4 Where this goes `[SPECULATIVE]`

End state: objectives are declared, decisions are recorded, commitments are tracked, and
reversibility governs autonomy. Agents become interchangeable - a model is swapped the way a
runtime is swapped, because nothing durable lives inside it.

Which yields the strategic claim this paper closes on:

> **The decision graph is the moat. The agents are not.**

Buying agents buys a depreciating asset; each is obsoleted by the next model release. A decade of
recorded decisions - with their authority, alternatives, consequences and outcomes - is an
appreciating one. No model provider can replicate it, because it is the accumulated judgment of
one specific institution. It is also the only plausible training signal for a system that must
learn that institution's actual rules rather than generic competence.

The investment case is therefore not "buy agents in order to be agentic". It is:

> **Record decisions so that agency becomes possible, and so that the record outlives whatever
> model you are using this year.**

### 9.5 The uncomfortable conclusion

`[ARGUED]` The two strongest primitives in this paper - the provisional write in section 3.0 and
the warranted dry run in section 3.0a - share a property that undermines the comfortable version
of the roadmap above.

**Both live inside the systems of record, not in the agent layer.** Provisional writes must be
implemented by SAP, Salesforce, Workday and ServiceNow. Warranted dry runs must be produced by the
owner of the state, because only the owner knows its invariants.

> **The agentic enterprise is blocked on a change to the write interfaces of enterprise
> application software, and the agent industry cannot make that change.**

This reorders the paper's own list. "Enterprise state addressable for writing" was listed fifth
of five. It is not fifth. It is the only item that is **not the agent industry's to build**, and
every other item is downstream of it.

It also explains the observation this paper opened with - hundreds of vendor agents, little
crossing - better than the missing-commitment claim does. Vendors ship agents because agents are
what a vendor can ship unilaterally. Nobody ships the write interface, because it requires the
application vendors to change the semantics of their own state, and no agent company can compel
that.

**What follows for a buyer.** The leverage is not in agent procurement. It is in demanding
provisional-write and dry-run semantics from application vendors as a purchasing requirement -
the same way buyers once forced SSO, audit logging and API access into products that shipped
without them. That is a procurement lever, not an engineering project, and it is available now.

---

## Appendix A - Terminology

**Commitment.** A promise with an obligor, a beneficiary, a condition, a deadline and a
consequence for breach. Distinct from a record, which is a row.

**Authority.** Ownership of truth for a piece of state, plus the right to change it irreversibly.
A first-class scope object, not a tier.

**Harness.** The tools, acting identity, permission scope, model, context budget and verification
gate a run executes under.

**Episode.** One objective, its causal trace across systems, the commitments it created, its
reversibility state, and its outcome.

**Receipt.** The durable typed record of what a run selected, mounted, changed, and what verified
it - including who computed the mask.

---

## Appendix B - The progression, and where it ends

`[ARGUED]` Four generations of agent engineering have appeared in rapid succession. Each made one
component of a decision process explicit and engineerable:

| Generation | Unit | Made engineerable |
|---|---|---|
| Prompt engineering | a string | what the model is TOLD |
| Context engineering | the window | what the model can SEE |
| Harness engineering | the action space | what the model can DO |
| Loop engineering | the iteration | when the model STOPS |

Instruction, observation, action, termination. The field has been reconstructing a decision
process by hand, component by component, without announcing it.

Each generation arrived when the previous one hit the same ceiling: **the unit of work outgrew
the unit of engineering.** Prompts broke when the task needed more information than fit. Context
broke when the task needed to act. Harness broke when the task needed more than one step.

`[ARGUED]` **Loop engineering breaks when the task outlives the session.** All four generations
are session-scoped: each engineers one agent doing one thing once. Enterprise work is not
session-scoped. A promise made on Tuesday falls due in March; the run that made it is gone, and
so is the context window that held its reasoning.

This is the paper's answer to its own title question. The blocker is not model capability. It is
that every engineering discipline the field has produced evaporates at the end of the session,
while enterprise work outlives the session by orders of magnitude.

### The next unit `[SPECULATIVE]`

> Prompt, context, harness and loop all engineer A RUN. The next discipline engineers WHAT
> SURVIVES THE RUN.

The missing primitive, stated precisely:

> **Actions are durable. Decisions are not.**

Enterprise systems record that a discount was applied. None record that a decision was made to
apply it: by whom, under what authority, against which alternatives, with what expected
consequence, with what reversibility window, and under what condition it should be revisited.
Event sourcing records events; audit logs record actions; neither records decisions. Enterprises
store outcomes and discard the reasoning that produced them.

Consequences: an agent cannot be audited, only its effects observed; it cannot be learned from,
because there are no counterfactuals; its actions cannot be intelligently reversed, because what
changed is known and why is not; and it cannot be delegated to, because a decision boundary
cannot be specified when decisions are not objects.

> **We spent forty years building systems of record. An agentic enterprise needs a system of
> decision.**

### This subsumes section 3

`[ARGUED]` The five missing components proposed in section 3 are not five proposals. They are
facets of one primitive. A commitment is a decision with an obligor and a deadline. An episode is
a decision's causal trace. Reversibility is a property of a decision. Learned invariants are
mined from decisions that were overturned. An obligation ledger is a decision store indexed by
consequence.

Section 3 should be rewritten as one claim with five consequences.

---

## Appendix C - The Bitter Lesson, read correctly

`[ESTABLISHED - primary sources read]` The Bitter Lesson is routinely invoked to argue that any
hand-authored structure will be subsumed by a larger general model. The primary sources do not
support that use.

**Sutton (2019) names two scaling substrates, search and learning, and targets models of
cognition specifically:** "the actual contents of minds are tremendously, irredeemably complex...
we should build in only the meta-methods that can find and capture this arbitrary complexity."
The essay also concedes its own exception explicitly: research conducted as if compute were
constant is a case "in which case leveraging human knowledge would be one of the only ways to
improve performance." And the horizon is stated as the limit, not the quarter: knowledge "always
helps in the short term".

**AlphaZero removed the handcrafted evaluation function, not structure.** Its Methods section
contains an enumerated list of retained domain knowledge: a perfect rules simulator, rules-derived
state and action encoding, an architecture matched to the board grid, and terminal scoring. What
was deleted was handcrafted *judgment* - piece-square tables, king safety, mobility, pawn
structure, and the associated tuned weights.

**Gato is a weak witness and should not be cited.** It was trained by supervised behaviour cloning
on demonstrations generated by task-specific specialists, cleared a 50%-of-expert bar on 450 of
604 tasks, lost to the specialists that produced its data, showed negative transfer in ablation,
and its in-context prompting failed on genuinely held-out tasks, requiring weight fine-tuning.

**Sutton argued in 2025 that LLMs do not satisfy the Bitter Lesson.** Invoking him for the
opposite claim invokes an author who rejects that reading.

**Brooks, *A Better Lesson* (2019)**, gives the strongest counter-reading: the human effort is
displaced rather than eliminated - "shifting the human workload to creating massive training sets
and encoding what we want the system to learn in the labels... It is sleight of hand in moving
the human intellectual work to somewhere else."

### The consequence for this paper

`[ARGUED]` The skill library splits along Sutton's own line, but the split is finer than an
earlier draft claimed, and the correction matters:

- **Procedural skill** - how to debug, how to write a test, how to structure a migration - is a
  human-authored approximation of judgment. It is exactly what the Bitter Lesson eats, and its
  expiry is set by someone else's training run.
- **Local fiat that is already in a system of record** - "discounts above 15% require VP
  approval", when SAP already enforces it - is **a cache**, not durable knowledge. Caches drift.
  The seven same-name divergent skill bodies measured in section 6 are the exhibit. Restating an
  enforced rule in markdown creates a second source of truth that will disagree with the first.
- **Unencoded local dynamics** - the rule that exists only in people's heads and nowhere in any
  system - is genuinely durable, and only until it is written into a gate or into the system of
  record. At that point it too becomes a cache.

So the environment-specification argument survives, with a sharp qualification: local fiat belongs
in a machine-readable constraint store enforced at the harness - **by reference to its authority,
never by copying it**. AlphaZero kept one rules simulator, not a second transcription of the
rules kept beside it.

`[ARGUED]` What is actually durable in this architecture is therefore not the skill library at
all. It is: **tool and effect interfaces, deterministic gates, receipts, and the identity and
authority map.** Skills are a compiler cache for procedures the model cannot yet induce and the
system of record does not yet state. No product thesis should rest on their permanence.

---

## Appendix D - Corrections of record

Four adversarial reviews were run against this paper on separate frontier models. The following
claims were withdrawn or reversed as a result. They are recorded rather than deleted, because a
paper that argues for receipts should keep its own.

| Claim in an earlier draft | Status | Reason |
|---|---|---|
| Agent fleets are hard because Dec-POMDP is NEXP-complete | **Deleted** | Category error. That result concerns computing an optimal policy offline over a known model; these systems do greedy single-step selection. Enterprise partial observability is an authorization partition plus a lossy interface, not a sensor kernel |
| A hedged restatement of the above under bounded communication | **Deleted** | True the way "physics under friction" is true. Predicts nothing falsifiable |
| Harness is action masking, and this is mathematically clean | **Reversed** | A harness also varies the observation kernel, identity, model and budget. Only the action set is masking; identity and budget are outside the tuple entirely |
| A gate that can refuse is therefore an agent | **Reversed** | Conflates policy refusal with invariant refusal. Accepting it licensed LLM gates, which re-derives the fleet as N refusers plus one namer |
| The error was publication itself | **Reversed** | POSIX, SQL, HTTP, Kubernetes resources. Publishing a narrow waist is how a market and a warranty exist. The error was publishing N job titles |
| Local fiat is durable knowledge for a constraint store | **Refined** | If the rule is already in a system of record, restating it creates a cache, and caches drift. Reference authority; never copy it |
| Spawn an expert when it needs its own context window | **Retired** | Bets on a decaying constraint. Replaced by firewall, parallelism, non-mutation |
| The 309-skill census supports claims about vendor agent catalogues | **Scoped down** | Domain transfer failure. It is evidence about skill libraries only |
| Gato supports the generality-beats-structure reading | **Deleted** | Behaviour-cloned from specialists, lost to them, negative transfer in ablation, in-context prompting failed on held-out tasks |
| Agentic = work crosses boundaries without a human relaying it | **Reversed** | Defines agency by side effect, not mechanism. 1998 FIX/STP and a Zapier webhook both score maximally agentic. Replaced with a definition centred on behaviour under unmodelled perturbation |
| Reversibility budget: autonomy governed by expected cost of undo | **Reversed** | Non-computable ex ante under heavy tails; non-additive across composed actions; and a confession of a non-compliant control under SOX 404. Replaced with a discrete three-tier partition plus escrow |
| Mine the gates from correction history rather than authoring them | **Demoted to advisory** | Survivorship bias (only detected errors are logged), policy freeze under bandit feedback, and non-stationary human actors. Codifies blind spots and quarter-end gaming into machine gates |
| The Coordinator failed because humans found bookkeeping bureaucratic | **Refined** | Half blind. Humans keep commitments ambiguous deliberately, to absorb variance without breaching. Rigid formalisation yields cascading gridlock. Tolerance must be first-class |
| This work identifies the missing commitment primitive | **Scoped down** | The concept is forty years old: REA (1982), Winograd & Flores (1986), Singh (1999), Burgess (2005). The delta is that models are the translation interface that makes them deployable |
| There is no representation of the commitment | **Refuted** | **ISO 15944-4** standardises REA for cross-organisational business with commitments as first-class citizens and contract state machines. Narrowed to: it exists *between* companies and was never built *between departments* |
| Enterprise software modelled nouns, not obligations | **Cut** | ASC 606 and IFRS 15 mandate tracking **performance obligations**; IAS 37 mandates probabilistic ones. A legally required, globally deployed obligation ledger already exists |
| The Coordinator failed on declaration burden; agents remove it | **Refuted** | Answers the wrong critique. Suchman's objection is categorisation-as-power, and agents *industrialise* it rather than removing it. Survives only for machine-to-machine promises |
| An obligation ledger | **Polarity inverted** | Promise Theory: only the holder of the state can promise about it. Recording what one system says another owes reproduces the exact failure being diagnosed. Record self-promises |
| The reversibility budget is the governing mechanism | **Superseded** | Manufacture reversibility by construction (provisional writes) instead of estimating and gating it. And SLO error budgets are already this mechanism in production, so the novelty claim goes too |
| The obligation ledger is a new kind of artifact | **Demoted to derivative** | It is naturally an **event-sourced projection**. Saying so converts it from novel-and-unbuildable to derivative-and-shippable, which is the better trade |
| Declaration was the expensive part of commitment tracking | **Reversed** | Reconciliation is. "Did we deliver on time?" is contested in a large share of real cases and is judgment, not bookkeeping |
| 274 skill names shared across the two harnesses, 25 exclusive to one side | **Refuted, arithmetically** | An intersection cannot be 274 when one set holds 249 elements. A union was computed as if it were an intersection. Truth: 249 shared, 59 Copilot-only, **0 Claude-only** - one library is a strict subset of the other |
| Always-loaded metadata is ~26,344 tokens | **Corrected** | That figure was characters divided by four. A real cl100k tokenizer gives **22,312** - the estimate was 18% high. An arithmetic convention is not a measurement |
| All skill bodies total 3,037,217 characters | **Corrected** | That is the total of the *complete files including frontmatter*. Bodies alone are 2,903,213, and the ratio is 27.5x |
| 28 description pairs above 0.30 Jaccard | **Withdrawn as a number** | An independent implementation produced 48. The count is tokenizer- and stop-word-dependent and is not robust. The phenomenon stands; the figure does not |
| 63% of skills are stale | **Narrowed** | `mtime` shows *not edited*, never *not invoked*. No usage telemetry was collected, so the claim is about maintenance only |
| Skill selection necessarily degrades as the library grows | **Refuted** | No such theorem. Fano's inequality bounds error by `1 - (I(Z;X)+1)/log N`: degradation requires task evidence to stay bounded while `N` grows. The governing quantity is the active branching factor, not global size. **The ceiling is residual conditional entropy after filtering** |
| Progressive disclosure addresses the selection problem | **Split in two** | It reduces token cost. It does not reduce selection ambiguity. The paper had run two different problems together |
| Authority is the right boundary, therefore one executor | **Self-contradictory** | Multiple independent authorities imply multiple principals. The premise entails an unprivileged planner over several narrow, separately authorised executors - a multi-agent architecture in every security-relevant sense. The headline sentence of this work is wrong as stated |
| The one-executor architecture is an empirical claim | **Refuted as unfalsifiable** | If the harness may swap model, prompt, memory, permissions and skills, the single executor can emulate any specialist. It is a universal host, and no result can contradict it. Only survives if the arm is constrained to one policy, one loop, one memory, one resolver |
| A many-agents-versus-one-agent A/B would settle it | **Refuted as confounded** | Mixes routing, policy specialisation, authorisation and deployment topology. Needs an oracle-selection arm and a **no-skill** arm; without the latter, the census cannot show whether the library contributes anything at all |

Two holes were found that no earlier review caught, and both are now sections 5.3a: **local gates
do not compose**, and **the model was a call stack while enterprises are standing processes**.

**The pattern in this table is worth more than any single row.** Of the reversals above, the ones
that mattered most were not caught by re-reading the argument. They were caught by **re-running the
measurement** and by **checking the arithmetic of a claim against its own premises**. The
274-versus-249 error sat in a document that had already survived three adversarial reviews on
frontier models, all of which read the prose and none of which checked whether the number could
exist. It was false on its face - an intersection larger than one of its sets - and it took a
reviewer who re-ran the census to see it.

This is the second measurement error in the same table, after the truncating YAML parser. Both
passed a check. The first passed a non-emptiness check while silently truncating 187 descriptions;
the second passed every reading while being arithmetically impossible. **A paper that argues
organisations should keep receipts has now twice been wrong about its own, and both times the
receipt is what caught it.**

---

## Appendix E - Three routes, one object

`[ARGUED]` The strongest evidence for this paper's central claim is not any single argument. It is
that three independent lines of reasoning, pursued separately and by different reviewers, arrive
at the same missing primitive.

| Route | Starting point | Conclusion |
|---|---|---|
| **Speech acts** | An enterprise is a promise-keeping machine; software stores records, not commitments | There is no representation of the commitment |
| **Distributed systems** | A message bus carries beliefs, not authority; sagas buy compensation, not atomicity | Irreversible effects must be contained within one authority, and joint invariants need a home |
| **History of the discipline** | Prompt, context, harness and loop are all session-scoped; enterprise work is not | Nothing owns a case across calendar time |

All three name one object: **a durable, addressable record of what was decided - carrying
authority, alternatives, commitment, reversibility and revisit condition - that outlives the run
that produced it.**

The convergence is the argument. Any one route alone would be a plausible story; three routes from
different literatures landing on one primitive is the signal that the primitive is real and
genuinely absent.

> Prompt engineering, context engineering, harness engineering and loop engineering each made one
> component of a decision process explicit. None of them made the **decision** explicit. That is
> the next unit of work, and until it exists there is no agentic enterprise to speak of.
