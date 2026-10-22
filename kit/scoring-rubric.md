# Scoring rubric (Level 2)

*The level wording inside the rubric blocks on this page comes from `data/model.yaml`; for six questions and the data classes it is adapted from the AI Security Risk Workbook v3.0 by Jason Robbins and stays Apache-2.0. See NOTICE.*

All fourteen Three Surfaces questions with their four levels. Level 1 uses seven of them through the [quick-score worksheet](quick-score-worksheet.md); a Level 2 assessment answers all fourteen. The text here is copied from [data/model.yaml](../data/model.yaml), which is the definition.

## Rules

- **Rate it as configured.** Score the tool as it is set up for this use today. A setting that lowers a rating becomes a condition of the decision.
- **The worst rating decides.** The tool's tier is the highest rating of any question.
- **The lethal trifecta is Severe.** Data rated High or above, untrusted input rated Medium or above, and a way to put content where someone outside can see it make the use case Severe, unless every path in one leg is closed, each shown by a document or by a setting a named person checked. "Assume no untrusted input" with nothing behind it does not break a leg. The settings that usually break one are listed in `settings_that_break_a_leg` in [data/model.yaml](../data/model.yaml).
- **Ceilings.** Crossing a ceiling makes the use case Severe. One applies by default: a decision impact of High or Severe together with reliance Severe (a consequential decision about people made by the tool) routes as Severe and needs an impact assessment. Your profile can tighten the others, such as "no Confidential data without an exception".
- **Unknown is worst.** An unanswered question is rated at the worst level it could plausibly be, and the tier is marked provisional. An "assumed" answer about data, untrusted input, external reach or the exfiltration path counts as unknown until someone checks a document or a named owner confirms it.
- **Evidence can lower a rating only from a document.** Marketing pages, help articles and pasted text can raise a rating, never lower one or fill an unknown. The vendor's contract terms for your plan, quoted and read on the vendor's own site, count as a document.

## Data

### Data sensitivity: what is the most sensitive information that goes into it, or that it could produce?

<!-- rubric: data.sensitivity -->
- **Low:** Public information only.
- **Medium:** Internal business information that is not sensitive.
- **High:** Confidential information such as strategy, proprietary code, or customer and employee personal data held under contract.
- **Severe:** Regulated information such as health data, payment or financial account data, government IDs, biometrics, data about minors, or privileged client material.
<!-- /rubric -->

### Retention and training: what happens to what we put in, after we use it?

<!-- rubric: data.persistence -->
- **Low:** Nothing kept. Ephemeral, or processed locally.
- **Medium:** Kept for the session only or a short stated period, or stored in our own tenant under our own retention policy; never used for training.
- **High:** Stored or cached by the vendor for a longer or unbounded period, with no training on it.
- **Severe:** The vendor may train on it, or it goes into memory shared across users or customers.
<!-- /rubric -->

### Contract coverage: do our terms with the vendor cover the data we will send it?

<!-- rubric: data.contract_coverage -->
- **Low:** Only public data is involved, or a DPA and written no-training terms cover all data in scope.
- **Medium:** Terms cover the data in scope with minor gaps, such as unstated residency for internal data.
- **High:** Terms are silent or unclear on training, retention or subprocessors for confidential data, or no DPA is in place.
- **Severe:** Regulated data without the agreement it legally needs (for example PHI without a BAA), or terms that allow training on it.
<!-- /rubric -->

## People

### Audience: who sees what it produces before a person on your side has reviewed it?

<!-- rubric: people.audience -->
- **Low:** The requester alone, or a small named internal team.
- **Medium:** A whole department or the whole organization.
- **High:** People outside the organization reached through a known relationship or channel, such as clients, partners, or customers in an authenticated or support channel.
- **Severe:** The public, with no relationship or authentication, or output published openly.
<!-- /rubric -->

### Reliance: how much do people trust the output before they check it?

<!-- rubric: people.reliance -->
- **Low:** Advisory. A person checks every output before it is used.
- **Medium:** Spot-checked. Output is used after a light or sampled review.
- **High:** Authoritative. Output is acted on without routine verification.
- **Severe:** Decision-driving. Output directly determines a decision or action.
<!-- /rubric -->

At Level 2, rating reliance Low needs evidence that the review is real, such as edit or rejection rates.

### Decision impact: if the output is wrong, who outside your own team is affected, and how badly?

<!-- rubric: people.decision_impact -->
- **Low:** No effect beyond minor inconvenience.
- **Medium:** Affects work quality or time; easily corrected before anyone relies on it.
- **High:** Affects a person's money, access, employment or legal position, or a client's decisions, contract or confidential information, and can be put right with effort.
- **Severe:** A consequential decision about a person (hiring, credit, health, legal advice, benefits) or a client that is hard to reverse, or any significant effect on minors or other vulnerable people.
<!-- /rubric -->

### Disclosure and consent: have we told the people affected what we must, and do we have consent where it is needed?

<!-- rubric: people.disclosure -->
- **Low:** No disclosure or consent obligation applies.
- **Medium:** A disclosure or consent is needed and is already in place.
- **High:** A disclosure or consent is needed and is not yet in place.
- **Severe:** The use contradicts a commitment already made, such as a contract clause or public statement that client data is not processed by AI.
<!-- /rubric -->

## Capability

### Function: what is the most it is allowed to do?

<!-- rubric: capability.function -->
- **Low:** Assist or analyze.
- **Medium:** Recommend or influence.
- **High:** Take action, or operate autonomously within set limits.
- **Severe:** Operate without defined limits.
<!-- /rubric -->

### Autonomy: how much does it do without a person approving each step?

<!-- rubric: capability.autonomy -->
- **Low:** No autonomy. A person prompts each action.
- **Medium:** Scoped autonomy. A person approves every write.
- **High:** Autonomous within an allowlist. A person approves severe actions only.
- **Severe:** Fully autonomous with no human gate, or able to spawn sub-agents.
<!-- /rubric -->

If autonomy is "within an allowlist", record the allowlist. If you don't know it, rate autonomy Severe until you do.

### Reversibility: if it does the wrong thing, can we undo it?

<!-- rubric: capability.reversibility -->
- **Low:** Read-only. No change of state.
- **Medium:** Reversible writes, such as editing a document or retrying a task.
- **High:** Hard to reverse, such as sending an email or triggering a payment.
- **Severe:** Irreversible, such as deleting records, posting publicly or moving money.
<!-- /rubric -->

### Access: what can it read and change inside our environment?

<!-- rubric: capability.access -->
- **Low:** Read-only and scoped to what the task needs.
- **Medium:** Limited write to scoped resources, or read-only access to everything in a system (such as a CRM service account that can read every record).
- **High:** Full read and write on production resources.
- **Severe:** Admin, root or infrastructure control.
<!-- /rubric -->

### Integration: how deeply is it wired into our systems?

<!-- rubric: capability.integration -->
- **Low:** Standalone. No integrations.
- **Medium:** Limited, rate-capped API connections to one or two internal tools.
- **High:** Direct access to production systems such as databases, file stores or connectors.
- **Severe:** Privileged control plane, such as identity, secrets or infrastructure.
<!-- /rubric -->

### Untrusted input: does it read content that nobody in the organization wrote or checked?

<!-- rubric: capability.untrusted_input -->
- **Low:** None. Only what the requester types or internal content the organization controls.
- **Medium:** Documents or messages from known outside parties, such as client uploads or partner email.
- **High:** Open external content, such as web pages, inbound email, support tickets from any sender, or third-party tool output.
- **Severe:** Open external content that drives a tool able to act without a person approving each action.
<!-- /rubric -->

### External reach: what can it reach outside our environment?

<!-- rubric: capability.external_reach -->
- **Low:** Nothing. Internal only.
- **Medium:** Allowlisted endpoints, logged.
- **High:** Broad internet access with logged egress.
- **Severe:** Unrestricted or unlogged egress, including sending data or calling third-party APIs at will.
<!-- /rubric -->

<!-- licence-footer -->

---

*Handrail by [Keith Crawford](https://keithcrawford.me). Licensed [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). If you adapt this page, keep this line and say what you changed.*
