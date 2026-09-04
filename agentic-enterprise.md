# Why Is There Still No Agentic Enterprise? Yet.

## A disputation, in two voices, with nine hypotheses and a way to test them

**Author:** Ragnar Pitla
**Version:** 3.0, 4 September 2026
**Status:** Working paper. Circulated for disagreement.
**Companion site:** https://ragnarpitla.github.io/Agentic-Enterprise/
**Measurement script:** [`census.py`](census.py), six controls, output in [`evidence-census.txt`](evidence-census.txt)

---

## How to read this paper

Most papers about enterprise AI are written from one seat. Either the engineering seat, which
knows what the systems do and is naive about what institutions are, or the institutional seat,
which knows what firms are and treats the technology as a black box with a marketing budget. Each
produces a literature the other does not read.

This paper is written from both, on purpose, and it does not hide the seam.

> **PROPOSITION** marks the constructive argument: computation, agentic engineering, and what a
> deployment actually does when it meets an enterprise. It builds the case.

> **OBJECTION** marks the adversarial reading: institutional economics, the sociology of work, and
> the accounting and control literature. Its job is to break the case, and several times it does.

Where the two cannot be reconciled, the paper says so and leaves the disagreement standing. A
synthesis that resolves every tension is a synthesis that was never tested.

**Nine hypotheses (H1 to H9) are stated formally in section 3**, each with the observation that
would falsify it. Everything after that section is an attempt to support, attack, or operationalise
one of them. If you read nothing else, read section 3 and section 10.

**Epistemic key.** Every substantive claim carries one of five labels.

| Label | Meaning |
|---|---|
| `[MEASURED]` | Verified by direct measurement in this work; method stated; script included |
| `[ESTABLISHED]` | Supported by a primary source that was fetched and read |
| `[ARGUED]` | Reasoning offered, no external evidence yet |
| `[SPECULATIVE]` | Deliberately beyond current practice, flagged so a reader can discount it |
| `[CORRECTED]` | A claim this paper made and then withdrew. Appendix D lists all of them |

Nothing is `[ESTABLISHED]` on the strength of recollection. **Appendix D contains thirty-one
corrections of record**, including two of the paper's own measurements. That appendix is not an
apology. It is the evidence that the method works, and it is the part of this paper I would defend
hardest.

---

## 1. The question, and why the obvious answers fail

Enterprises bought agents. Budgets were approved, pilots ran, vendors shipped catalogues. Almost
nobody describes their enterprise as agentic.

That gap is the subject. "There are too many agents" is a complaint, not a question. The question
is **why the spending did not convert**, and what would have to become true for it to convert.

Three answers are commonly given. All three are available, all three are comfortable, and this
paper argues all three are wrong in the same way.

**"The models are not good enough yet."** This predicts that the gap closes on its own as capability
rises. It is unfalsifiable in practice, because any given failure can be attributed to the current
generation. Section 9.1 turns it into a real experiment with a real losing condition.

**"Enterprises are slow, change management is hard."** True of every technology, and therefore
explains nothing specific about this one. It also fails a timing test: the same organisations
adopted cloud, mobile and SaaS on ordinary curves.

**"We need better orchestration."** The most popular answer, and the one this paper takes most
seriously before rejecting it. Orchestration coordinates things that already exist. Section 2
argues the thing that needs coordinating has no representation.

> **PROPOSITION.** The three standard answers share a structure: each treats the shortfall as a
> quantity problem. More capability, more time, more coordination. If the shortfall were instead a
> **representation** problem, all three would be locally reasonable and globally useless, which is
> exactly the pattern the field is exhibiting: rising capability, rising spend, flat crossing rate.

> **OBJECTION.** That is a rhetorically convenient trichotomy. A fourth answer exists and it is the
> boring one: **the work being targeted is not economically worth automating.** Most enterprise
> boundary-crossing is low-volume, high-variance and already handled by a human in four minutes on
> a call. The observed shortfall may simply be a rational market declining to buy a solution to a
> problem that does not cost enough. This objection is not answered anywhere in this paper. It is
> the strongest one against it, and it is stated at full strength in section 8.1.

### 1.1 A definition that survives its counter-examples

"Agentic enterprise" is a phrase people nod at. A paper that will not define it measurably is
indistinguishable from the marketing it criticises.

**An earlier definition is withdrawn.** `[CORRECTED]` It read: *work crosses system and departmental
boundaries without a human relaying it*. The counter-examples are decisive and historical rather
than hypothetical. In 1998, FIX protocol engines carried a trade from buy-side order management to
broker to clearing house to custodian, three corporate boundaries in twelve milliseconds, no human
involved. A Zapier webhook today fires Shopify to SAP to Stripe across commerce, ERP and finance
with no human relay. Both score as maximally agentic under that definition. Neither has any agency
whatever: no goal-directed planning, no epistemic adaptability, and both fail the moment an input
schema shifts.

The defect was defining agency by its **side effect** (no human present) rather than by its
**mechanism**.

> **Working definition.** An enterprise is agentic to the degree that **commitments are autonomously
> formed, monitored, fulfilled, or renegotiated across authority boundaries in the presence of
> unmodelled perturbations**, without human mediation.

`[ARGUED]` The discriminator is behaviour under perturbation, and it is observable from outside:

| Automation (STP, RPA, scripts) | Agency |
|---|---|
| Deterministic path execution | Path generated at runtime |
| Fixed environmental mapping | Recovers from unmodelled intermediate failure |
| **Halts on invariant breach** | **Renegotiates or replans around the breach** |
| Monitors return codes | Closes or escalates the underlying commitment |

> **OBJECTION.** The definition now contains "unmodelled perturbations", which is unfalsifiable
> without a specification of the model. Anything a system handles was modelled; anything it fails
> is declared unmodelled after the fact. The definition risks being a tautology dressed as a test.

> **PROPOSITION, conceding partially.** The repair is to fix the perturbation set **in advance**,
> as a published suite: schema drift, partial outage, authority revocation mid-task, contradictory
> instruction, and counterparty non-response. Agency is then measured against a pre-registered
> perturbation battery rather than against whatever happened to go wrong. This is section 9.2, and
> it is the objection that produced it.

### 1.2 The ladder

| Level | Behaviour | Where deployments sit |
|---|---|---|
| 0 | Assistive. Human works, agent drafts | Common |
| 1 | Task automation inside one system | Almost all of it |
| 2 | Cross-system execution, human approves at gates | Rare |
| 3 | Cross-system with autonomous compensation, human on exception | Almost none |
| 4 | Objective-level delegation | None |

`[ARGUED]` **No quantity of Level 1 sums to Level 2.** Buying more agents is horizontal motion.
Becoming agentic is vertical. That is a structural claim and it predicts the observed symptom:
high pilot counts, low production crossing.

---

## 2. What actually blocks the crossing

### 2.1 The commitment is real, represented, and cannot travel

`[CORRECTED]` An earlier draft of this paper claimed that enterprise software never modelled
obligations, only nouns. **That claim is false and it was the paper's central assertion.** It was
refuted by a reviewer with three citations, all of which were then fetched and read.

**ISO 15944-4** standardises the REA ontology for cross-organisational business, with commitments
as first-class citizens and explicit contract state machines. **ASC 606 and IFRS 15** mandate that
firms track *performance obligations* through formation, satisfaction and modification. **IAS 37**
mandates probabilistic obligations. A legally required, globally deployed obligation ledger already
exists inside every public company.

So the honest claim is much narrower, and more interesting:

> **The representation exists between companies and inside accounting. It was never built between
> departments, and it is not the object any agent is assigned.**

REA and ISO 15944-4 were built for inter-firm trade, where the counterparty is adversarial and the
contract is the artifact. ASC 606 obligations are maintained for **reporting**, on a quarterly
cadence, by a function whose job is retrospective assurance. Neither is a live, operational,
sub-daily object that an autonomous process can read, hold, and act on. The finance department
knows what was owed. It knows it in arrears, at a grain of a quarter, for the purpose of telling
the truth to a regulator.

> **OBJECTION.** This concedes the interesting half and keeps the rhetoric. If the object exists in
> two places already, the parsimonious explanation is that building a third one is redundant, and
> that the correct engineering move is to **project** from the existing sources rather than to
> introduce a new primitive with new failure modes. Master data management died on exactly this
> hill.

> **PROPOSITION.** Agreed on the mechanism, and this is where the argument turns. The reply is in
> section 6.2, and it is the single most important distinction in this paper: **the proposal is a
> write-side capture mechanism, not a read-side semantic layer.** MDM decayed because it was a copy
> of an original held elsewhere. A commitment recorded at the instant of promising **is** the
> original. There is nothing upstream of it to drift from.

### 2.2 Enterprise systems have no pencil `[ARGUED]`

This is the strongest single mechanism in the paper and the one I would build first.

State in enterprise software is binary: written or not written. Ink or nothing. What a competent
human does under uncertainty is act **provisionally**: *I am pencilling you in for Friday.* That
creates real, visible, actionable state, which other parties can see and rely on **weakly**, and
which evaporates unless confirmed.

There are exactly two widespread instances, and both are domain-specific hacks that nobody
generalised: **the airline seat hold** and **the inventory reservation**.

> **The missing primitive.** A universal provisional-write state class. Every writable field
> supports a third value-state - *provisionally set, by claimant C, expiring at T, visible to all
> readers as provisional* - which is neither a lock, which blocks others, nor a commit, which is
> final, and which auto-reverts unless confirmed.

**Why this beats governing autonomy with a risk budget.** A budget tries to *estimate and gate*
irreversibility, which requires predicting the cost of undo before acting. Provisional writes
**manufacture reversibility by construction.** A large class of agent actions becomes mechanically
reversible, not because a cost was estimated correctly, but because the substrate reverts them for
free. **No reversibility budget is needed for actions that expire on their own.**

It also defuses the objection that killed the budget approach: provisional state is *visibly*
provisional, so third-party reliance on it is weak by construction, and third-party reliance is
precisely the mechanism that made reversal costs heavy-tailed and non-additive. A counterparty who
saw a pencilled date and staffed a warehouse against it bears that risk explicitly.

> **OBJECTION, and it is a serious one.** Provisional state is not free. It creates a distributed
> garbage collection problem, a visibility problem for reporting, and a new class of exploit:
> **provisional-write denial of service**, where an agent reserves capacity it never confirms and
> starves competitors. Airlines have this problem today and manage it with fees and inventory
> heuristics tuned over decades. Generalising the primitive generalises the pathology.

> **PROPOSITION, conceding.** The pathology is real and it is the reason expiry is in the primitive
> rather than optional. But this objection is not fully answered, and it belongs on the risk list in
> section 8.

### 2.3 The warranted dry run `[ARGUED]`

Every mutation interface should expose `predict(mutation) -> effect set, invariants touched,
reversal plan`, and it must be produced **by the owner of the state, not by the agent**, because
only the owner knows its own invariants.

This resolves a standing puzzle. Enterprise reinforcement learning is impossible because there is
no simulator. There is no simulator because no system of record was ever asked to describe what a
write would do *before* doing it. Databases compute exactly this internally in order to plan and
validate transactions. Exposing it is an interface convention, not a research problem.

---

## 3. Nine hypotheses

This is the spine of the paper. Each hypothesis is stated so that a reasonable person could gather
evidence against it, and each carries the observation that would kill it.

### H1 - The decomposition hypothesis `[ARGUED]`

> Enterprise agent fleets are partitioned along **application** boundaries. Application boundaries
> are set by vendor packaging and are **uncorrelated with the minimum cut of the write-dependency
> graph** of the business processes they serve. The fleet is therefore a bad decomposition of the
> work, independent of how capable each agent is.

**Falsified if:** measured on real ACLs and change logs, application boundaries turn out to sit at
or near the min-cut of the write-dependency graph. Then the fleet is a good decomposition and the
naming is merely cosmetic.

**Note on an earlier version.** `[CORRECTED]` This hypothesis was first stated in complexity-theoretic
terms, claiming siloed agents form a decentralised POMDP and are therefore NEXP-complete rather than
PSPACE-complete. That was a category error: those results concern computing an optimal policy
offline over a known model, and no system in this stack does that. The replacement above is weaker,
computable, and immune to the objection that the agents can simply talk to each other.

### H2 - The cliff hypothesis `[ARGUED]`

> Autonomous completion rate falls **discontinuously** at authority boundaries, and the size of the
> discontinuity **does not shrink as model capability rises**, because the missing information was
> never recorded and cannot be inferred.

**Falsified if:** completion decays smoothly with the number of boundaries crossed, and the curve
lifts with each model generation. That result would mean the shortfall is a reliability problem,
the capability answer is correct, and most of this paper is decoration.

This is **the decisive experiment** and it is specified in section 9.1. It has not been run.

### H3 - The reachability hypothesis `[MEASURED, in part]`

> Capability registries grow monotonically because **no deletion event exists** in their lifecycle.
> No deletion event exists because **objectives have no durable identity**, so no reachability graph
> can be computed, so nothing can ever be shown to be garbage.

**Falsified if:** a registry is found that shrinks under normal operation, or if reachability can be
computed from existing artifacts without introducing a durable objective object.

This is the one hypothesis with direct measurement behind it already. Section 5.2.

### H4 - The selection hypothesis `[ARGUED]`

> In real capability libraries the mutual information between task evidence and correct capability
> does **not** grow with `log N`, because selection metadata is hand-written prose. By Fano's
> inequality, selection error therefore rises with library size. The degradation is **contingent on
> a design choice**, not necessary.

**Falsified if:** measured `I(Z;X)` grows with `log N` in a real library, or if selection accuracy
holds flat as `N` rises under a controlled sweep with confusability held constant.

### H5 - The provisional-write hypothesis `[ARGUED]`

> The binding constraint on cross-boundary autonomy is the **absence of a provisional-write state
> class** in systems of record, not model capability.

**This one has a natural experiment available and it has not been run.** Two domains already have
provisional writes in production: airline seat inventory and warehouse stock reservation. If H5 is
right, autonomous cross-boundary behaviour should be **measurably further along in those domains
than in domains of comparable complexity without the primitive.** If it is not further along, H5 is
in serious trouble and the pencil is a nice idea that does not bind.

**Falsified if:** domains with provisional writes show no advantage in autonomous crossing.

### H6 - The reconciliation hypothesis `[ARGUED]`

> The expensive part of commitment tracking is **reconciliation**, not declaration. Determining
> whether a promise was kept is contested judgment in a large fraction of real cases, and no amount
> of capture removes that.

**Falsified if:** in a real commitment corpus, the labour splits heavily toward declaration and
disputed fulfilment is rare.

`[CORRECTED]` An earlier draft asserted the opposite: that declaration was the expensive part and
that agents remove it because they do not find bookkeeping tedious. That framing survived three
reviews before being reversed.

### H7 - The capture hypothesis `[ARGUED]`

> **Information never recorded cannot be recovered by a more capable model.** If a salesperson said
> "Friday" on a call and nobody wrote it down, no scaling law retrieves it.

**Falsified if:** downstream artifacts turn out to contain enough residue to reconstruct the
commitment reliably. This is genuinely testable: take a corpus of known commitments, delete the
record, and measure reconstruction from surrounding evidence.

> **OBJECTION.** H7 is close to tautological and does less work than it appears to. Nearly every
> commitment leaves residue: a calendar entry, a shipping quote, a Slack line, a changed field. The
> question is not whether the information was recorded but whether it was recorded **as a
> commitment**. State that way, H7 is a claim about *typing*, not about *existence*, and it is much
> weaker than the paper's rhetoric around it suggests.

> **PROPOSITION, conceding.** That is right, and the sharpened form is better: the claim is that
> commitments recorded only as residue cannot be **enumerated**, and an obligation you cannot
> enumerate is one you cannot monitor. The strong version is withdrawn.

### H8 - The concentration hypothesis `[ARGUED]`

> Agentic capability is concentrating into roughly five model vendors. Enterprise **state** is
> fragmenting across hundreds of application vendors. The agentic layer requires both, and no party
> owns both. Therefore any proposal that depends on **cooperation from the state vendors cannot
> scale past the top twenty**, and the long tail never cooperates.
>
> The corollary is the useful part: commitments are **formed** in a concentrated surface, and
> **fulfilled** in a fragmented one. Capture at formation is tractable where capture at fulfilment
> is not.

**Falsified if:** a commitment layer is delivered by integrating at the system-of-record tier across
a realistic vendor tail, or if the utterance surface turns out to be as fragmented as the state
surface.

This hypothesis was added after the rest of the paper was drafted, and **it overturns the conclusion
in section 10.5 as originally written.** Section 8.3.

### H9 - The human ceiling hypothesis `[ARGUED]`

> System-level agency is bounded by human capability **at the exception boundary**, and automation
> **raises** rather than lowers the skill required there. An enterprise cannot operate at Level 3
> while its people operate at Level 0, because Level 3 is defined as *human on exception*, and the
> exceptions that survive automation are the hard ones.

**Falsified if:** organisations reach Level 3 crossing rates without a measurable change in the
capability of the people handling exceptions.

Section 8.4.

---

## 4. What the two seats disagree about

The disputation format is not decoration. On three questions the engineering seat and the
institutional seat give different answers, and the paper does not resolve them.

### 4.1 Is ambiguity a defect or a feature?

> **PROPOSITION.** Commitments are kept ambiguous because there was no cheap way to record them
> precisely. Lower the cost and precision follows.

> **OBJECTION.** No. Humans keep commitments ambiguous **deliberately**, because ambiguity absorbs
> variance without producing breach. "Early next week" is not a failure to say Tuesday; it is a
> option purchased against uncertainty. Formalise every promise and you convert a system with slack
> into one with cascading rigid dependencies, which is how you get gridlock rather than throughput.
> The 1980s Coordinator project failed on precisely this, and Lucy Suchman's critique is not that
> declaration is tedious but that **categorisation is an exercise of power**: someone decides which
> box your work goes in, and agents industrialise that rather than removing it.

**Unresolved.** The paper's response is to make tolerance a first-class attribute rather than an
absence of one, so that "Friday plus or minus two days, hard stop month end" is representable. That
is a partial answer at best, and it does not touch the power critique at all.

### 4.2 Who does the ledger actually kill?

> **PROPOSITION.** The blocker is engineering effort and vendor write interfaces.

> **OBJECTION.** The blocker is **legal**. A complete, timestamped, machine-readable record of every
> commitment the firm made and every one it broke is a discovery target. Opposing counsel would like
> nothing better. General counsel will kill this before any CTO gets to evaluate it, and the more
> faithful the record, the stronger the argument for killing it.

**Unresolved, and nobody in this work has an answer.** It is listed in section 8 as an open risk
rather than dressed up as a solved problem.

### 4.3 Is this new?

> **PROPOSITION.** The layer does not exist, therefore it is new.

> **OBJECTION.** Every component is old. REA is 1982. Winograd and Flores is 1986. Singh on social
> commitments is 1999. Burgess on promise theory is 2005. Sagas are 1987. Event sourcing gives most
> of the durable-episode mechanics today. Workflow and BPM engines have had durable case identity
> with timers and compensation for twenty years. **A paper claiming novelty here is claiming it
> against a large and unread literature.**

> **PROPOSITION, conceding almost entirely.** The genuine delta is narrow and should be stated
> narrowly: **language models are the first practical translation interface between informal human
> promising and a formal commitment representation.** Every prior attempt required humans to type
> into structured forms, and every prior attempt died there. That is a claim about the input method,
> not about the ontology, and the ontology should be borrowed rather than invented.

---

## 5. Evidence

### 5.1 The selection tax `[MEASURED]`

**Scope limit, stated before the numbers.** This census measures a coding-assistant skill library:
markdown procedure files, symlinks, a token menu. Vendor "agents" are commercial products carrying
data gravity, identity, service levels and warranty. These are different objects. The census is
evidence about **skill libraries and progressive disclosure**. It is not a natural experiment on
enterprise agent catalogues, and using it as one would be decoration with a spreadsheet.

Measured 4 September 2026 on one practitioner's installed library, with six control assertions and
a real tokenizer rather than a character estimate. Script: `census.py`,
which asserts six controls and refuses to print if any of them fail.

| Quantity | Value |
|---|---|
| Copilot `SKILL.md` files / unique names | 309 / **308** (`mia-video` duplicated) |
| Claude `SKILL.md` files / unique names | 249 / 249 |
| Names in **both** | **249** |
| Only in Copilot / only in Claude | **59 / 0** |
| Always-loaded selection metadata | 105,581 chars, **22,312 tokens** (cl100k, measured) |
| All skill bodies, frontmatter stripped | 2,903,213 chars |
| Body-to-metadata ratio | **27.5x** |
| Not edited in 90 days | 196/309 = **63.4%** |
| Broken symlinks | **19 in each directory** |

**Cite the absolute tax, not the ratio.** Roughly 22,000 tokens of always-on menu is charged to
every run, including runs that need no skill at all, describing capabilities the majority of which
have not been touched in a quarter.

**What `mtime` does not show.** `[CORRECTED]` 63.4% is *not edited*. It is not *not invoked*. No
usage telemetry was collected, so the claim is about maintenance, not demand.

### 5.2 The finding that changed the paper: no garbage collector `[MEASURED]`

The census was built to measure a selection tax. Read again, it measures something more useful.

| Decay mode | Signal | Collector |
|---|---|---|
| Disuse | 196 of 309 untouched in 90 days | **None** |
| Dangling reference | 19 broken symlinks per side | **None** |
| Supersession | Worst duplicate pair scores **1.00**, a dated backup folder loaded as a live skill | **None** |
| Divergence | **0** skills exist only on the Claude side; one library is a strict subset of the other | **None** |

Four independent decay modes, no collector for any of them. **The library did not reach 309 because
309 capabilities were needed. It reached 309 because nothing is ever removed.** There is no deletion
event anywhere in the lifecycle.

`[ARGUED]` This reframes the sprawl argument away from where it started. The problem is not that
somebody designed a fleet badly. **Capability registries are allocated and never freed**, which is a
problem the industry solved for memory in the 1960s and has not noticed it has again. Reference
counting, reachability tracing and tombstones are all sitting unused.

And the reason they are unused is the subject of this entire paper:

> **You cannot garbage-collect a capability registry, because there is no reachability graph.**

Reachability requires knowing which live objectives reference which capabilities. That graph does
not exist because **objectives are not durable objects**. They are prompts, tickets, conversations
and intentions that evaporate at the end of a session. A capability cannot be shown unreachable
when nothing durable ever pointed at it.

So the two halves of the field's complaint are one finding:

- Work does not cross boundaries autonomously, because **the commitment** has no durable identity.
- Capability libraries grow without bound, because **the objective** has no durable identity.

**Same missing object. Two symptoms.** This is H3, and it is the argument for building the primitive
rather than buying more of the other thing.

**A cheap test that needs no architecture.** Instrument invocation, then delete everything with zero
invocations and zero inbound references for two quarters. If the library survives, the reachability
graph is latent in telemetry and can be made explicit. **If nobody dares run it, that fear is the
finding.**

### 5.3 Two corrections to this paper's own measurements `[CORRECTED]`

Recorded here rather than in an appendix, because they are the strongest available evidence for the
method this paper is recommending.

**First error.** An early draft reported 19,437 tokens and a 39x ratio. The parser captured only the
first line of multi-line YAML descriptions, undercounting metadata by 35%. It passed a non-emptiness
check because every skill returned *some* description. **A non-emptiness guard detects total
blindness, never partial blindness, and partial blindness is the reachable failure.**

**Second error.** The corrected draft then reported **274 shared names and 25 exclusive to one
side**. Those numbers are arithmetically impossible: an intersection cannot be 274 when one of the
sets holds 249 elements. A union had been computed as though it were an intersection. That figure
survived **three adversarial reviews on frontier models**, all of which read the prose and none of
which checked whether the number could exist. It was caught by a fourth reviewer who re-ran the
census.

**The pattern is the lesson.** Neither error was found by re-reading the argument. Both were found by
re-running the measurement. A paper that argues organisations should keep receipts has now twice been
wrong about its own, and both times the receipt is what caught it.

**A control that failed for the wrong reason, also recorded.** The first verification run asserted
that a known skill's description contains the word "slop". It does not; the word appears in the name
and body, never the description. The control fired correctly, but my assumption was about the
*control*, not the data. **A control must assert something independently verified, or it fails for
its own reasons and teaches nothing.**

### 5.4 A claim withdrawn, and one weakened

`[CORRECTED]` **Withdrawn: the duplication tax.** An earlier draft argued the two libraries impose a
maintenance cost through divergence. Direct measurement refutes it: most entries on both sides are
symlinks to the same files on disk, with genuine divergence at 7 forks out of 249. The strategy
works, and the paper will not claim a problem its own data refutes.

`[CORRECTED]` **Weakened: near-duplicate counts.** An earlier draft reported 28 description pairs
above 0.30 Jaccard similarity. An independent implementation produced 48. Neither is wrong; the count
is tokenizer- and stop-word-dependent and is **not a robust quantity**. The phenomenon is real and
the worst pair remains an exact 1.00. The count is withdrawn as a citable number.

---

### 5.5 External evidence, and what failed verification `[ESTABLISHED]`

A census of one laptop is evidence about skill libraries, not about enterprises. Claims that carry weight were checked against primary sources; those that failed were dropped rather than softened.

**PROPOSITION.** The mechanism this paper describes -- an agent forming a commitment no system of record holds -- is not hypothetical. It has been litigated. In *Moffatt v. Air Canada*, 2024 BCCRT 149 (decided 14 February 2024), a chatbot told a passenger he could claim a bereavement fare retroactively; the airline's policy page said the opposite. The tribunal found negligent misrepresentation, applying *Queen v. Cognos Inc.*, 1993 CanLII 146 (SCC), and awarded CAD 812.02.

Paragraph 28 of the decision is the one that matters, and it is the one nobody quotes. The airline could not explain why the page titled "Bereavement travel" was inherently more trustworthy than its chatbot, nor why a customer should have to check one part of a website against another. Air Canada *had* the authoritative page and *had* linked to it (paragraph 16). The commitment was still formed at the conversational surface, and the tribunal declined to privilege the system of record over it. This is the grounding-plus-disclaimer remedy failing in court, which makes it the strongest available answer to the most common objection to H1.

**OBJECTION.** A small-claims tribunal, CAD 812.02, no binding precedent, and the tribunal never used the words *authority*, *ownership* or *system of record*. One documented instance is not a trend, and reading a doctrine of write authority into a consumer-protection award is exactly the overreach this paper accuses others of. The proposition is entitled to say the mechanism *occurs*. It is not entitled to say it is *common*.

**PROPOSITION.** Accepted, and the claim is narrowed accordingly: existence, not prevalence.

Second item. Section 5.1 could show that a capability index costs tokens; it could not show the index degrades selection, having no accuracy data. Anthropic has published some, as an admission against interest: on MCP evaluations over large tool libraries, Opus 4 moved from 49% to 74%, and Opus 4.5 from 79.5% to 88.1%, when tools were *removed* from context and searched for on demand. Fifty-eight tools across five connectors consume roughly 55K tokens before a conversation starts; Anthropic reports 134K internally before optimisation. The failure mode they name is wrong tool selection, worst when names are similar -- structurally the same finding as the 1.00-similarity pair in section 5.2, now with an accuracy number attached to it. These are internal evaluations with no published methodology, sample size or confidence intervals; a 25-point gap is too large to be noise, but it is not a controlled result.

This matters for the Fano argument in Appendix C. The bound degrades only if evidence stays bounded as N grows. Anthropic's result is the same claim from the other direction: hold evidence fixed and grow the tool set, accuracy falls; restore selective evidence and it recovers 25 points. The triggering condition is not merely plausible, it is measured.

Third item, and the one that costs this paper something. Thoughtworks has published an Agentic Scope of Authority Framework, framed on what an agent is legally authorised to commit the enterprise to, and reaching for agency law to ground it. The authority problem is therefore already recognised in practitioner literature, published before this paper, by Martin Fowler's own employer. What appears to remain unoccupied is the specific move from *authority* to *bounded context as the correct unit of decomposition*; novelty is claimed for that synthesis only, and not for noticing that authority is the problem.

**Numbers deliberately not used.** The widely-circulated "1.3 billion agents by 2028" is an IDC Info Snapshot sponsored by Microsoft, per Microsoft's own footnote -- a vendor-commissioned forecast, not independent analysis and not a measurement. No primary, methodologically-disclosed dataset quantifying enterprise agent duplication, abandonment or maintenance cost was found, which is why this paper argues from mechanism rather than market size. A claim that scaffolding moved task success from 42% to 78% was traced to arXiv:2607.22585, which reports 0-8 percentage points with confidence intervals including zero; it is false as attributed and is not used.

One figure survived because it is self-refuting. Workday markets its Agent System of Record as a way for one team to govern thousands of AI agents. The published catalogue on the same page contains 21.

## 6. The architecture that survives

### 6.1 The headline was wrong

This work began from a sentence: *we do not need hundreds of agents, we need one agent that picks
the right skill, objective and harness.* That sentence is dead, and a reviewer killed it cleanly:

> If authority is genuinely the right boundary, then multiple independent authorities imply multiple
> principals. The authority thesis does not entail one executor with broad rights. It entails an
> unprivileged planner coordinating several narrow, independently authorised executors, which is a
> multi-agent architecture in every security-relevant sense.

**But the objection proves less than it looks, and the difference is the architecture.** It moves
from "multiple authorities imply multiple principals" to "therefore multi-agent in every
security-relevant sense". The qualifier carries enormous weight. In the security sense it is right.
In the **cognitive** sense, which is what the thesis was about, it does not follow, because **a
principal is not an agent.**

A principal is an identity holding authority. An agent is a locus of decision. One process routinely
acts under many principals and nobody calls it many processes: `sudo -u` does this, a connection pool
with per-request credentials does this, OAuth token exchange exists to do this, and a web server
serving ten thousand authenticated users is not ten thousand web servers. Multiplicity of authority
requires multiplicity of **credential**. It does not require multiplicity of **policy**, of **control
loop**, or of **deployed artifact**.

| Axis | Claim | Status |
|---|---|---|
| **Authority** | Must be partitioned narrowly, per principal, outside the model | **Objection is right** |
| **Cognition** | Should not be partitioned by application or department | **Proposition is unrefuted** |

What dies is the phrase "one agent". What survives: **do not cut the thinking along the vendor's
seams, and never let the thinker hold the credential.**

### 6.2 The design rule, in one line

The rule is about **where the capability set is computed**, not how many agents exist:

| | |
|---|---|
| **Fatal** | `K = capabilities chosen by the model` |
| **Defensible** | `K = G(authenticated requester, workflow state, approvals, policy)` |

where `G` is a deterministic policy decision point outside the model. **The model may request
authority. It cannot grant it.**

Five reasons a separately-authorised executor wins, each surviving the whole argument: separation of
duties, which a prompt cannot implement; the confused deputy, where one executor holding the union
of privileges gives any injected request the union blast radius; common-mode failure, where one
shared model or gateway fails every process at once; information barriers, where the control
prohibits *observation* and a mask over actions does not deliver it; and ownership, meaning an
accountable control owner and an on-call rota, without which a shared executor becomes a commons
with no owner.

### 6.3 Capture at creation, not reconciliation afterwards

This is the reply to the master-data objection in section 2.1, and it is the distinction the paper
rests on.

> The proposal is a **write-side capture mechanism**, not a read-side semantic layer.

MDM decayed because it was a copy of an original maintained elsewhere; copies drift from originals.
A commitment written **at the instant of promising is the original**. There is nothing upstream to
drift from. Naturally implemented, it is an **event-sourced projection**, which converts it from
novel-and-unbuildable to derivative-and-shippable. That is the better trade.

`[CORRECTED]` An earlier draft proposed mining invariants from human correction history. Demoted to
advisory only: survivorship bias, since only detected errors are logged; policy freeze under bandit
feedback; and non-stationary human actors. Mined gates would codify blind spots and quarter-end
gaming into machine-enforced rules.

### 6.4 Two holes that remain open

**Local gates do not compose.** Every authority can approve correctly and the firm can still be
wrong, because the violated invariant spans contexts that no single gate can see. Sagas compensate
known reverse actions; they do not invent the missing cross-context invariant.

**The model was a call stack; enterprises are standing processes.** Nothing in the current design
owns a case over calendar time. The missing object is a durable case with identity, an authority
set, a state machine, receipts, wait conditions and a compensation cursor. **The public surface is
the case. The planner is episodic against it.**

Workflow and BPM engines already have case identity, and that is conceded rather than worked around.

---

## 7. Where the reviews overreached

Four adversarial reviews produced thirty-one reversals. A paper that logs every one without ever
defending a position has stopped being a paper and become a transcript. Two objections do not
survive contact.

**"The one-executor thesis is unfalsifiable, because a harness that swaps model, prompt, memory and
permissions can emulate any specialist. It is a universal host."**

The premise is true and the conclusion does not follow. A general-purpose CPU can emulate any ASIC.
That did not render forty years of computer-architecture claims unfalsifiable; it relocated the
falsifiable content from the capability set to the **cost model**, which is where it lives for any
architectural claim.

More decisively, **the objection is symmetric and therefore proves too much.** N specialised agents
can emulate one generalist by routing everything to the fattest one. Any architecture with enough
configuration emulates any other. If that were disqualifying, no architectural proposition in
computing could be tested, including the fleet proposition this paper argues against. What the
objection does correctly establish is that **capability parity is the wrong outcome variable**. The
testable claims are cost, drift, blast radius, governance surface and time-to-change.

**"Selection cannot degrade with library size; no such theorem exists."**

Correct as stated, and better read as **the first rigorous formulation of the claim** rather than a
refutation. Fano's inequality gives the bound: with `Z` the correct capability among `N` and `X` the
task evidence,

> `P_e >= 1 - (I(Z;X) + 1) / log N`

Error rises with `N` **only if** task evidence supplies bounded information while the library grows.
Typed preconditions that make `I(Z;X)` grow with `log N` lift the ceiling entirely.

**That is H4, made checkable.** And this paper measured the input: in the surveyed corpus the
selection evidence is hand-written prose, near-duplicate pairs reach an exact 1.00, and typed
preconditions appear nowhere. Prose written by one author does not carry information growing with
the logarithm of library size. **The condition under which Fano predicts rising error is the
condition that actually holds.** The correction is that degradation is contingent rather than
necessary, and the contingency is a design choice nobody is currently making.

It also separates two things this paper had run together: **progressive disclosure reduces token
cost; it does not reduce selection ambiguity.**

---

## 8. Where this breaks, and the two things this paper left out

### 8.1 The mundane steelman, at full strength

The best counter-argument does not dispute a single mechanism above. It disputes that any of them
bind.

**Leg one: it is a reliability problem.** Cross-boundary work fails because multi-step autonomy is
unreliable and the failure compounds. Nothing about commitments is required to explain it, and it
dissolves as capability rises.

**Leg two: the economics are wrong.** Most boundary crossings are low-volume and high-variance. A
human resolves them in four minutes on a call. The engineering cost of a commitment layer exceeds
the labour it displaces, and the market is rationally declining.

**Leg three: the data is rotten.** Real ERP fields are named `ZZ_CUST_FLAG_3` and mean four different
things by region. A commitment layer built on that substrate inherits the rot. **Conceded without
mitigation.**

**Leg four: it already exists in pieces.** Event sourcing, BPM engines, CLM tools, and ASC 606
obligation tracking each cover part of the ground. The residual may not justify a new primitive.

`[ARGUED]` The paper's answer to legs one and four is the experiment in section 9.1. **It has no
answer to leg two**, and leg two is the one that decides whether any of this gets built.

### 8.2 Open risks, unmitigated

| Risk | Status |
|---|---|
| Legal discoverability of a complete commitment record | **No answer.** Section 4.2 |
| Provisional-write denial of service | Partially handled by expiry; pathology remains |
| Data rot in the underlying fields | Conceded, no mitigation |
| Local gates do not compose | Open |
| Reconciliation is judgment, not bookkeeping | H6; may be the real cost centre |

### 8.3 The omission that breaks the conclusion: intelligence concentrates, state does not

`[ARGUED]` This paper was drafted as though the enterprise were negotiating with a handful of
vendors. It is not, and the asymmetry is the whole problem.

| Layer | Vendor structure | Direction of travel |
|---|---|---|
| **Reasoning** | Roughly five frontier model vendors | Concentrating |
| **State of record** | Hundreds of application vendors per large enterprise | Fragmenting |
| **Utterance** (email, chat, meetings, calls) | Effectively two suites | Already concentrated |

The agentic layer needs all three. **No party owns more than one of them.**

**Why this kills the procurement lever as originally stated.** Section 10.5 concluded that
provisional writes and warranted dry runs must live inside the systems of record, and that the buyer
should force this through contracts. Against SAP, Salesforce, Workday and Oracle, that is a real
lever: twenty vendors might cover the majority of high-value workflows. But a large enterprise runs
hundreds of applications, and **the tail does not negotiate.** A three-person vendor with a renewal
worth forty thousand dollars will not re-architect its write interface because one customer asked.
The commitment layer cannot be built on a precondition that hundreds of independent firms cooperate.

> **PROPOSITION, revised.** The proposal only survives if it does **not** require the state tier to
> cooperate. And there is a route, which the concentration table makes visible: **commitments are
> formed in a surface that is already concentrated, and fulfilled in one that is not.** The
> salesperson promises Friday on a call, in an email, or in a chat thread. Two vendors carry
> essentially all of that traffic. Capture at formation needs cooperation from two parties. Capture
> at fulfilment needs it from four hundred.

This is a second, independent argument for capture at creation, and it is stronger than the one in
section 6.3. That one said copies drift from originals. This one says **the origin is reachable and
the destination is not.**

**And it produces a procurement ask that is actually winnable.** Not "add a state class to your
database", which the tail will refuse, but: *give me a structured, exportable commitment stream from
the surface where my people make promises, in a format I own.* That is one clause, aimed at two
vendors, both of whom already sell compliance and eDiscovery products built on exactly this data.

> **OBJECTION, and it is the sharpest one in this section.** Capturing at the utterance surface
> makes the communications vendor the owner of the commitment graph. The paper closes by calling the
> decision graph the enterprise's moat. A moat that lives in someone else's product is not a moat;
> it is a dependency with better branding. You have swapped four hundred weak dependencies for one
> strong one, and strong dependencies are the expensive kind.

> **PROPOSITION, conceding the shape and disputing the conclusion.** Conceded that residency is the
> risk, which is why the ask above specifies *exportable* and *in a format I own*. The decision graph
> must be enterprise-held data, not a vendor feature, or the moat argument collapses. That constraint
> is now a design requirement rather than an afterthought. It is also the reason the layer should be
> an event-sourced projection over an owned event log: the events are yours even when the surface
> that emitted them is not.

**A second consequence, which reframes the sprawl argument entirely.** If an enterprise runs four
hundred applications, and every one of those vendors is now shipping an agent, then the fleet is not
an architectural decision anybody made. **It is the supply side's shape reproducing itself inside the
buyer.** Conway's Law is usually told as a story about org charts. This is Conway's Law operating
through procurement: you did not choose to have hundreds of agents, you chose hundreds of vendors,
and the agents arrived attached.

That explains something the earlier draft could not. It explains why the sprawl appears even in
organisations with competent architecture functions and a genuine desire to consolidate. Nobody
approved the fleet. The fleet is what a purchasing history looks like when each line item ships an
assistant.

`[SPECULATIVE]` It also predicts the next move, and it is not consolidation. It is that the
application vendors will each try to become the orchestrator of the others, because the orchestrator
position is the only one with pricing power. Most of them will fail, the attempts will be expensive,
and the interoperability standards produced along the way may be the most durable output of this
period.

### 8.4 The omission that breaks the timeline: the people

`[ARGUED]` The ladder in section 1.2 measures the system. There is a second ladder, it is not
measured anywhere, and it is the binding constraint far more often than the first.

**Seats are not capability.** Enterprises report adoption as licences deployed. The distribution of
value is not uniform and is not close to uniform: a minority of users find the workflows that
compound, and the rest use the tool as a better search box. Buying ten thousand seats and reporting
ten thousand adopters is a measurement error of the same class as the two this paper made in section
5.3, and it has the same cause: counting what is easy to count and calling it the thing you wanted.

**Automation raises the skill floor for what is left.** `[ESTABLISHED]` This is the *Ironies of
Automation* result (Bainbridge, 1983), and it is forty years old and still routinely ignored. The
more of a process you automate, the more critical and the more **degraded** the remaining human role
becomes: operators are left with the exceptions, which are the hardest cases, while losing the
routine practice that built the judgment those exceptions require.

Level 3 on the ladder is defined as *human on exception*. Bainbridge's result says that is the
hardest possible job description, and that it gets harder as the automation improves.

> **This is the inversion nobody prices in.** An organisation moving from Level 1 to Level 3 does not
> need fewer skilled people. It needs **more skilled people, doing a harder job, less often**, with
> less routine practice to stay sharp on. A programme that funds the platform and not the capability
> is buying a ceiling and calling it a floor.

**Shadow AI is not a side issue. It is this paper's failure mode, running at scale, today.**

An employee who is not given a usable tool uses a consumer one. A customer email is pasted into a
chat window, a reply is drafted, judgment is applied, and the reply is sent. **A commitment has been
formed.** No enterprise system saw the reasoning, the alternatives, the risk that was accepted, or in
many cases the promise itself.

> Shadow AI **increases the rate at which commitments are formed and decreases the rate at which they
> are captured.** It widens precisely the gap this paper is about, and it widens it fastest in the
> organisations that are slowest to provide tools.

That framing also settles whether shadow AI is good or bad, a question usually argued at the level of
policy. It is both, and the two are not in tension:

- **Useful**, because the work gets done and the employee is often right.
- **Harmful**, because the employee personally absorbs a risk the firm cannot see, the organisation
  learns nothing from a discovery that took real skill, and the commitment enters the world untyped
  and unenumerable.

The person doing it is running unpaid research and development for their employer, carrying the
liability personally, and receiving none of the credit. That is a bad trade for both parties, and it
persists because the alternative on offer is four hundred vendor agents that nobody can find, none of
which do the specific thing being asked.

**The uncomfortable link back to the fleet.** People route around tools they cannot navigate. A
catalogue with hundreds of entries, no reachability graph and 63% of it untouched for a quarter is
not a capability library from the user's side. It is a maze. **Sprawl and shadow AI are the same
phenomenon observed from opposite ends**: the organisation sees uncontrolled supply, the employee
sees no usable supply, and both are looking at the absence of the same missing object.

**What follows for the programme.** Section 10.2 gains a phase that should have been in it from the
start, and it is not a training phase. Training assumes the tool is fine and the person is deficient.
The right move is to **instrument what people already do in the shadow**, treat it as the demand
signal it is, and build the two or three workflows it reveals. The people using consumer tools to do
their jobs have already run the discovery exercise. Nobody has asked them for the results.

### 8.5 Standing kill criteria

The thesis should be abandoned if: cross-boundary completion improves smoothly with model generation
(kills H2); a fleet of application-shaped agents reaches Level 3 on the ladder without a shared
commitment object (kills H1 and H5); or provisional-write domains show no autonomy advantage
(kills H5).

Two further criteria follow from the omissions above. If a commitment layer is delivered by
integrating at the system-of-record tier across a realistic vendor tail, H8 is wrong and the
formation-surface argument in section 8.3 was unnecessary. If organisations reach Level 3 crossing
rates with no measurable change in the capability of the people handling exceptions, H9 is wrong and
Bainbridge does not bind here.

---

## 9. How to test it

### 9.1 The decisive experiment: cliff versus smooth

`[ARGUED]` This makes the paper empirical rather than aesthetic, and it must be run before any of it
is believed.

| Hypothesis | Prediction |
|---|---|
| **Mundane** (reliability) | Cross-boundary completion rises **smoothly** with capability. No discontinuity at authority crossings |
| **Representational** (H2) | Within-boundary autonomy improves, then **plateaus at the crossing**. The cliff does **not** move as models improve, because the missing information was never recorded |

**Method.** Plot autonomous completion against the number of authority boundaries a task crosses,
holding capability fixed. Repeat across model generations.

**Reading it.** Smooth decay that lifts each generation means the mundane thesis wins and the
commitment layer is decoration. A cliff that stays put means the layer is real.

### 9.2 Why that experiment is not sufficient

`[CORRECTED]` The cliff test addresses H2 and says nothing about the architecture. A naive
"many agents versus one agent" A/B is worse than useless because it confounds routing, policy
specialisation, authorisation and deployment topology in a single comparison. The arms must separate
them:

| Arm | Execution | Routing | Authority |
|---|---|---|---|
| A1 | Specialised controllers | Deterministic external router | Static narrow principals |
| A2 | Specialised controllers | Model router | Static narrow principals |
| B1 | Shared executor | Flat capability menu | Out-of-band, task-scoped |
| B2 | Shared executor | Hierarchical retrieval | Out-of-band, task-scoped |
| **B3** | Shared executor | **Oracle capability and harness** | Out-of-band, task-scoped |
| **C0** | Shared executor | **No capability library at all** | Out-of-band, task-scoped |

**B3 and C0 make the result readable, and the original design had neither.**

- If forcing the correct capability into the shared executor **recovers** performance, selection was
  causal.
- If it does not, the benchmark is measuring execution competence, and the entire selection argument
  is measuring the wrong thing.
- **If C0, with no capabilities at all, matches the full library, the library contributes nothing**
  and the selection tax in section 5.1 buys exactly zero.

That last arm is the control this paper most needed and did not have. A census proves a library is
expensive. It says nothing about whether the library **works**, and on the evidence gathered here the
C0 outcome is not ruled out.

**Sweep the right variables.** Library size, active branching factor, semantic confusability,
description length, metadata budget and target position must vary **independently**. Run two
distractor regimes: orthogonal distractors raise `N` without raising confusion, hard negatives share
terminology and preconditions. If only hard negatives hurt, the ceiling is semantic entropy and
pruning the library is the wrong remedy.

**Score state, not labels.** Verified postconditions in a simulator, unauthorised capability exercise
at the enforcement point, separation-of-duty violations, and mutation blast radius at tail
percentiles. Exact capability-label accuracy is the wrong primary metric, because several
capabilities may be equivalent and a label score marks a correct outcome wrong.

### 9.3 The natural experiment nobody has run

H5 is testable **today, with no new engineering**, and this is the cheapest high-value study
available. Airline seat inventory and warehouse stock reservation already have provisional writes.
Compare autonomous cross-boundary behaviour in those domains against domains of comparable
transaction complexity that lack the primitive. If the pencil binds, the advantage shows up. If it
does not, H5 is wrong and section 2.2 is a nice idea about nothing.

### 9.4 The metric

One number, reported by boundary count:

> **Boundary-crossing completion rate.** The share of work items that cross at least one authority
> boundary and reach a terminal state without human relay, segmented by number of boundaries crossed
> and by whether the terminal state was the intended one.

---

## 10. How we get there

The paper would be worth little if it only explained a failure. This section is the constructive
half, and each phase is designed to pay for itself before the next begins, because a programme that
requires belief in the whole thesis before delivering anything will not be funded.

### 10.1 The unlock

You do not build the decision layer. **You stop discarding it.**

Every agent run today produces a rich object: what was intended, what was tried, what was refused,
what was written, what was reversed. At the end of the session it is thrown away and a chat
transcript is kept. The capture cost is near zero because the information is already in memory. The
only change is not deleting it.

### 10.2 Six phases

| Phase | What ships | Why it pays for itself |
|---|---|---|
| **0. Demand signal** | Instrument what people already do in the shadow. Survey, amnesty, log what tools are actually in use and for what | Costs almost nothing, and the workflows people built for themselves are the shortlist. They already ran the discovery |
| **1. Receipts** | Every automated action emits a structured receipt: intent, authority, effect, reversal plan | Audit evidence that already has a buyer in compliance |
| **2. Gates on humans** | Deterministic policy checks run against **human** actions first | Finds broken controls immediately, with no agent risk. The gates are validated before anything autonomous depends on them |
| **3. Case identity** | A durable case object with a state machine, timers and a compensation cursor | Cross-system status becomes answerable, which is already a reporting request |
| **4. Provisional writes** | One system of record exposes a provisional-write state class and a `predict()` endpoint | Enables dry runs and safe retries for existing automation, before any agent uses it |
| **5. Commitment capture** | Models transcribe informal promises into typed commitments at the moment of promising, from the formation surface, into a log the enterprise owns | The translation interface is the genuine delta from section 4.3, and section 8.3 is why it starts at formation rather than at fulfilment |
| **6. Delegation** | Objectives assigned against cases, executed by an unprivileged planner through narrow authorised executors | Level 3 on the ladder |

**Phase 0 is new and it is deliberately first.** `[CORRECTED]` The earlier version of this plan began
at receipts, which assumes you already know which work to instrument. You do not, and the people who
do know are the ones currently pasting customer emails into consumer chat windows. Ask them before
building anything. A programme that opens by telling people to stop using the tool that works will
get one honest answer and then no more.

### 10.3 Two contrarian commitments

**Gates before agents, validated on humans.** Everyone builds the agent first and the guardrails
after. Reverse it. Run the policy checks against human actions for a quarter. You will find that
some fraction of your controls do not fire, and you will find it without an autonomous process in
the blast radius. Gates that have never rejected a real action are not gates.

**Expand by reversibility, not by department.** The instinct is to pick a department and go deep.
Wrong axis. Order the work by how cheaply an action can be undone, and cross departmental lines
freely within a reversibility tier. Reversibility is the property that governs risk; departments are
an artifact of Conway's Law.

### 10.4 Where this goes `[SPECULATIVE]`

`[SPECULATIVE]`, and labelled so a reader can discount it.

Four generations of this discipline have now shipped: prompt engineering, harness engineering,
context engineering, loop engineering. **All four are session-scoped.** They optimise what happens
between the start and end of a run. Enterprise work is not session-scoped: a commitment made on
Tuesday is breached in March, and the object that connects them does not exist.

The next unit is not a better prompt or a longer context. It is **decision engineering**: treating
the decision, with its authority, its alternatives, its evidence and its reversal path, as the
durable artifact.

> **Actions are durable. Decisions are not.** We spent forty years building systems of record. An
> agentic enterprise needs a system of decision.

### 10.5 The uncomfortable conclusion, and its revision

The most useful sentence in this paper is also the one that most undermines its author's ability to
act on it.

Provisional writes and warranted dry runs must live **inside** SAP, Salesforce, Workday and Oracle.
They are properties of the write interface of a system of record. **The agentic enterprise is
therefore blocked on a change to enterprise write interfaces, and the agent industry cannot make
that change.** No orchestration layer, no framework, no fleet of agents can add a state class to a
database it does not own.

The original conclusion followed: the lever is not engineering, it is **procurement**, and ten large
customers asking in the same renewal cycle would move it.

**That conclusion was drafted before H8, and H8 breaks half of it.** `[CORRECTED]` Procurement is a
real lever against twenty large vendors. It is no lever at all against the tail of several hundred
applications a large enterprise actually runs, where a renewal is worth less than the engineering it
would fund. Any plan requiring the state tier to cooperate stops at the top twenty, and the work that
crosses boundaries does not confine itself to the top twenty.

> **The revised conclusion.** Split the ask by where the vendor sits.
>
> **Against the top twenty,** ask for the write interface: a provisional-write state class, a
> `predict()` endpoint, commitment events on the bus. Winnable, slow, and worth starting now because
> the cycle is measured in years.
>
> **Against the tail,** ask for nothing, because nothing is what you will get. Capture at the
> **formation** surface instead, which is concentrated in two vendors, and require that the stream be
> **exportable into a log you own**. The commitment enters your system of decision at the moment it
> is made, whether or not the four hundredth application ever learns what a commitment is.

The second half is the part that can start this quarter, and it is the part the industry is not
working on, because it is not a model problem and it does not demo well.

**And the corollary, which is the last thing to say.** If this is right, the durable asset is not the
agents. Anyone can buy those, and by the argument in section 5.2 they will accumulate whether or not
anyone wants them. It is not the models either: those concentrate into five vendors and none of them
will be yours.

> **The decision graph is the moat. The agents are not.**

Which imposes one final constraint, from the objection in section 8.3: **it has to be a moat you
own.** A commitment history that lives inside a vendor's product is that vendor's asset with your
name on the invoice. Own the log, project everything else from it, and treat every reasoning layer,
including the five that currently look permanent, as replaceable.

---

## Appendix A - Terminology

| Term | Definition used here |
|---|---|
| **Objective** | What is to be achieved, with its acceptance predicate |
| **Skill / capability** | A reusable procedure with preconditions and effects |
| **Harness** | The runtime envelope: model, tools, permissions, memory, budget |
| **Authority** | An identity that may perform a class of mutations |
| **Principal** | The identity under which an action executes. Not the same as an agent |
| **Commitment** | A promise with obligor, obligee, condition, deadline, tolerance and remedy |
| **Case** | The durable object that owns a commitment over calendar time |
| **Provisional write** | A third value-state: set by a claimant, expiring, visibly weak |
| **Receipt** | Structured evidence of intent, authority, effect and reversal plan |

## Appendix B - Prior art, and the genuine delta

| Source | Year | What it already provides |
|---|---|---|
| REA ontology, McCarthy | 1982 | Resources, events, agents; commitments as first-class |
| **ISO 15944-4** | - | REA standardised for cross-organisational business, with contract state machines |
| Winograd and Flores, *Understanding Computers and Cognition* | 1986 | Conversation for action; the Coordinator |
| Sagas, Garcia-Molina and Salem | 1987 | Long-running transactions with compensation |
| Singh, social commitments | 1999 | Formal commitment semantics for multi-agent systems |
| Burgess, Promise Theory | 2005 | Only the holder of state may promise about it |
| ASC 606 / IFRS 15 | 2014 | Mandated tracking of performance obligations |
| Event sourcing / BPM engines | current | Durable case identity, timers, compensation |

**The genuine delta, stated narrowly:** language models are the first practical translation interface
between informal human promising and a formal commitment representation. Every prior attempt required
a human to type into a structured form, and every prior attempt died there. The ontology should be
borrowed, not invented.

## Appendix C - The Bitter Lesson, read from the primary sources

Sutton's argument names two scaling substrates, **search** and **learning**, and targets *models of
cognition*. It does not say that all modularity is bad, that all explicit knowledge is bad, or that
security boundaries should be learned.

AlphaZero's own methods section enumerates the domain knowledge it **retained**: a perfect rules
simulator, a rules-derived encoding, a grid-matched architecture, and terminal scoring. It deleted
the handcrafted *evaluation function*, not the environment specification. Brooks' *A Better Lesson*
(2019) reads the trend as displacement rather than elimination. Sutton himself argued in 2025 that
large language models do not satisfy the Bitter Lesson.

**The consequence for this paper.** Commitments, authority maps and invariants are **environment
specification**, not encoded cognition, and are therefore not what the Bitter Lesson targets. But the
lesson does bite in one place, and a reviewer put it sharply: **if a rule is already enforced by a
system of record, a capability that restates it is a cache, and caches drift.** The 7 forked skills
are the exhibit. Reference authority; never copy it.

`[CORRECTED]` An earlier draft cited Gato as evidence that generality beats structure. Deleted: it
was behaviour-cloned from specialists, lost to them, showed negative transfer in ablation, and its
in-context prompting failed on held-out tasks.

## Appendix D - Corrections of record

Thirty-one claims from earlier drafts were withdrawn, reversed or narrowed across four adversarial
reviews on separate frontier models. The full thirty-one row table lives in the companion file
[`corrections-full.md`](corrections-full.md), section D. The categories:

| Category | Count | Most consequential |
|---|---|---|
| Deleted outright | 4 | The Dec-POMDP complexity argument, a category error |
| Refuted by a source | 5 | ISO 15944-4 refuting the paper's central claim |
| Polarity inverted | 2 | Promise theory: record self-promises, not imposed obligations |
| Scoped down | 4 | The census is evidence about skill libraries, not vendor catalogues |
| Measurement errors | 3 | 274 shared names, arithmetically impossible |
| Demoted to advisory | 2 | Mining invariants from correction history |
| Reversed | 6 | Declaration is not the expensive part; reconciliation is |
| Narrowed or weakened | 5 | Jaccard pair counts are not robust |

**Why this appendix exists.** A paper arguing that organisations should keep receipts of their own
decisions has an obligation to keep its own. Two of the entries are errors in this paper's own
measurements, and both were caught by re-running the measurement rather than by re-reading the
argument. That is the method, demonstrated on itself.

## Appendix E - Three routes, one object

The strongest evidence in this work is not any single measurement. It is that three independent lines
of reasoning arrive at the same missing object.

| Route | Starting point | Where it lands |
|---|---|---|
| **Speech act** | Winograd and Flores; what a promise is | A durable commitment with obligor, condition, tolerance and remedy |
| **Distributed systems** | Atomicity across authorities; sagas cannot compensate the uncompensable | A durable case with a state machine and a compensation cursor |
| **History of the discipline** | Four generations of session-scoped engineering | A durable decision object that outlives the session |

Three routes, three vocabularies, one object. That convergence is the reason to take the hypothesis
seriously, and it is also the reason to be suspicious: convergence is what a well-constructed
rationalisation also produces. **Section 9 exists so that the question is settled by measurement
rather than by how satisfying the convergence feels.**
