# Quick-score worksheet (Level 1)

*The level wording inside the rubric blocks on this page comes from `data/model.yaml`; for six questions and the data classes it is adapted from the AI Security Risk Workbook v3.0 by Jason Robbins and stays Apache-2.0. See NOTICE.*

Use one worksheet per AI tool, per purpose. If the same tool is used two ways, such as a chat assistant for internal research and for client drafts, fill in two worksheets. It takes about fifteen minutes, including checking settings in the admin console, once you have the vendor terms check done. Unfamiliar terms are in the [glossary](../docs/glossary.md).

**Tool:** ____________________ **Plan or edition:** ____________________

**Used for:** ____________________ **Filled in by and date:** ____________________

## How to rate

Rate the tool as it is set up for this purpose today, not as it could be set up. "Allowed to do" means switched on in your plan and settings. For each question, tick the line that fits best. If you don't know the answer yet, tick the worst line it could be and write "unknown" next to it; that rating is provisional until you find out. The vendor's contract terms for your plan count as evidence: the terms of service, the data processing agreement, product terms for the plan, and pages those documents say are part of them. Their marketing pages and help articles never lower a rating, and never turn an unknown into a lower rating.

## The seven questions

### 1. What is the most sensitive information that goes into it, or that it could produce?

<!-- rubric: data.sensitivity -->
- **Low:** Public information only.
- **Medium:** Internal business information that is not sensitive.
- **High:** Confidential information such as strategy, proprietary code, or customer and employee personal data held under contract.
- **Severe:** Regulated information such as health data, payment or financial account data, government IDs, biometrics, data about minors, or privileged client material.
<!-- /rubric -->

*If the rating depends on keeping something out, such as redacting account numbers or keeping client material out, write that into the Conditions column. Client financial statements, forecasts and deal material under an NDA are High. Account numbers, card numbers and government IDs are Severe. A notetaker that stores voiceprints to recognize speakers handles biometrics (Severe); one that takes names from the meeting invite does not.*

Rating: ______ Evidence: ____________________

### 2. What happens to what we put in, after we use it?

<!-- rubric: data.persistence -->
- **Low:** Nothing kept. Ephemeral, or processed locally.
- **Medium:** Kept for the session only or a short stated period, or stored in our own tenant under our own retention policy; never used for training.
- **High:** Stored or cached by the vendor for a longer or unbounded period, with no training on it.
- **Severe:** The vendor may train on it, or it goes into memory shared across users or customers.
<!-- /rubric -->

*"Our own tenant" means a workspace where your admin sets how long content is kept and can delete it, and the vendor does not train on it. A business plan with those settings is Medium even though the vendor hosts it. If users can delete their own chats but no admin can set how long content is kept, it is not your own tenant: High. A vendor that trains on "de-identified" or "aggregated" content is still training on it (Severe) unless you have opted out.*

Rating: ______ Evidence: ____________________

### 3. Do our terms with the vendor cover the data we will send it?

<!-- rubric: data.contract_coverage -->
- **Low:** Only public data is involved, or a DPA and written no-training terms cover all data in scope.
- **Medium:** Terms cover the data in scope with minor gaps, such as unstated residency for internal data.
- **High:** Terms are silent or unclear on training, retention or subprocessors for confidential data, or no DPA is in place.
- **Severe:** Regulated data without the agreement it legally needs (for example PHI without a BAA), or terms that allow training on it.
<!-- /rubric -->

Rating: ______ Evidence: ____________________

*A DPA is a data processing agreement: the contract that says what the vendor may do with your data. A BAA is the equivalent agreement US health-care providers need for health data (PHI). Most small firms only need to find the vendor's DPA and its AI or data-use terms.*

### 4. Who sees what it produces before a person on your side has reviewed it?

<!-- rubric: people.audience -->
- **Low:** The requester alone, or a small named internal team.
- **Medium:** A whole department or the whole organization.
- **High:** People outside the organization reached through a known relationship or channel, such as clients, partners, or customers in an authenticated or support channel.
- **Severe:** The public, with no relationship or authentication, or output published openly.
<!-- /rubric -->

Rating: ______ Evidence: ____________________

### 5. How much do people trust the output before they check it?

<!-- rubric: people.reliance -->
- **Low:** Advisory. A person checks every output before it is used.
- **Medium:** Spot-checked. Output is used after a light or sampled review.
- **High:** Authoritative. Output is acted on without routine verification.
- **Severe:** Decision-driving. Output directly determines a decision or action.
<!-- /rubric -->

Rating: ______ Evidence: ____________________

### 6. If the output is wrong, who outside your own team is affected, and how badly?

<!-- rubric: people.decision_impact -->
- **Low:** No effect beyond minor inconvenience.
- **Medium:** Affects work quality or time; easily corrected before anyone relies on it.
- **High:** Affects a person's money, access, employment or legal position, or a client's decisions, contract or confidential information, and can be put right with effort.
- **Severe:** A consequential decision about a person (hiring, credit, health, legal advice, benefits) or a client that is hard to reverse, or any significant effect on minors or other vulnerable people.
<!-- /rubric -->

*Rate the effect if a wrong output gets past your normal review. A draft a consultant reviews and rewrites before the client sees it is Medium. A figure a client will rely on that nobody re-checks is High.*

Rating: ______ Evidence: ____________________

### 7. What is the most it is allowed to do?

<!-- rubric: capability.function -->
- **Low:** Assist or analyze.
- **Medium:** Recommend or influence.
- **High:** Take action, or operate autonomously within set limits.
- **Severe:** Operate without defined limits.
<!-- /rubric -->

Rating: ______ Evidence: ____________________

## Follow-up questions

Answer every follow-up whose trigger applies. Its ratings count toward the tier just like the seven.

**If question 1 is High or Severe, or the tool answers people outside your organization directly**, check for the "lethal trifecta": sensitive data, plus content from outside, plus a way to send data out.

- Does it read content that nobody in your organization wrote or checked, such as web pages, inbound email, or files clients send? Rate it:

<!-- rubric: capability.untrusted_input -->
- **Low:** None. Only what the requester types or internal content the organization controls.
- **Medium:** Documents or messages from known outside parties, such as client uploads or partner email.
- **High:** Open external content, such as web pages, inbound email, support tickets from any sender, or third-party tool output.
- **Severe:** Open external content that drives a tool able to act without a person approving each action.
<!-- /rubric -->

- Can it put content where someone outside the organization can see it: reply to them, send email or messages outside, post, open a link it was given, or show remote images? Yes / No: ______

If question 1 is High or above, it reads outside content (Medium or above) **and** it can put content outside, the tool is **Severe**, unless a setting breaks one of the legs. These settings break a leg; write any you rely on into the Conditions column, because turning one back on makes the tool Severe again:

| Setting | Breaks |
| --- | --- |
| Web search, browsing and opening links turned off | The way out, and outside content from the web |
| Link previews and remote images turned off in answers | The way out |
| Nothing leaves without a person approving it, and the person really reads it | The way out |
| Connectors to email, tickets or shared drives turned off | Outside content from those sources |
| Uploads limited to files written inside your organization, enforced by a setting | Outside content from uploads |
| Agent mode, actions and custom agents turned off | Actions that could send data out (also lowers question 7 and the autonomy follow-up). Memory kept for one user does not affect the trifecta; memory shared across users is a question 2 matter |

*Why images count:* an answer that loads an image from a web address can send data out inside that address, without anyone clicking anything.

A row does not apply when the tool cannot do that thing at all, shown by the vendor's documentation of the feature **and** a test you record: for remote images, ask the tool to show an image from a web address you control and keep a screenshot of the result. A leg counts as broken only when **every** row in the table that applies to the tool is closed for that leg (for example, browsing off but remote images still shown leaves a way out), and you can point to the setting or the vendor's terms for each. "We don't really use that feature" does not break it; if nobody can confirm, treat the leg as present and mark the tier provisional.

**If your plan has no setting for a path, the path is present.** Your options are a plan that has the setting, a narrower use (for example, no client material, which brings question 1 down), or a written, time-limited exception.

**If question 1 is below High** but the tool reads outside content and can put content outside, ask yourself whether question 1 is really right: check it against the examples in question 1. If nobody can confirm it, rate question 1 High and mark it provisional.

**If question 7 is High or Severe, or the tool is an agent**, also rate:

<!-- rubric: capability.autonomy -->
- **Low:** No autonomy. A person prompts each action.
- **Medium:** Scoped autonomy. A person approves every write.
- **High:** Autonomous within an allowlist. A person approves severe actions only.
- **Severe:** Fully autonomous with no human gate, or able to spawn sub-agents.
<!-- /rubric -->

<!-- rubric: capability.reversibility -->
- **Low:** Read-only. No change of state.
- **Medium:** Reversible writes, such as editing a document or retrying a task.
- **High:** Hard to reverse, such as sending an email or triggering a payment.
- **Severe:** Irreversible, such as deleting records, posting publicly or moving money.
<!-- /rubric -->

**If what it produces reaches clients, customers or meeting attendees**, even after someone on your side reviews it, also rate:

<!-- rubric: people.disclosure -->
- **Low:** No disclosure or consent obligation applies.
- **Medium:** A disclosure or consent is needed and is already in place.
- **High:** A disclosure or consent is needed and is not yet in place.
- **Severe:** The use contradicts a commitment already made, such as a contract clause or public statement that client data is not processed by AI.
<!-- /rubric -->

## Result

**Tier:** ______ This is the worst of every rating above, follow-ups included, or Severe if the lethal trifecta applies. It is provisional if any answer was unknown.

**If a condition lowers a rating** (for example, switching off automatic sharing), re-score with the condition and write both tiers: "Severe as first set up; High with automatic sharing off". The decision holds only while the condition does.

**What the owner usually does at this tier:**

| Tier | Usual decision |
| --- | --- |
| Low | Allow |
| Medium | Allow with conditions, such as "no client names in prompts" |
| High | The owner decides in writing before anyone uses it ("ask first"): Allow with conditions, or Banned |
| Severe | Banned, unless the owner grants a written, time-limited Exception. One case can be allowed without an exception; see "Regulated data your firm already handles" below |


**Regulated data your firm already handles.** A health practice or a financial adviser handles regulated data every day. A tool rated Severe *only* because of question 1 can be allowed with conditions, without an exception, when every one of these is true and written in the Conditions column:

- your firm already runs a written program for that data (for example HIPAA policies for a practice);
- the vendor has signed the agreement the law needs for that data (for example a business associate agreement) and its terms rule out training on it;
- no other rating is Severe, and the trifecta check found no outside content or no way out;
- the tool is limited to the records each task needs, and its retention is set;
- someone other than the person asking for the tool has read the agreement and checked the settings, and signs the row with the owner.

Review it every three months. If any item stops being true, the tool is Severe again and needs an exception. At Level 2 this is the designed path in the policy.

**Owner's decision** (Allow, Allow with conditions, Banned, or Exception): ____________________ **Conditions:** ____________________

**Copy the ratings, decision and conditions into the [inventory](inventory.md).**

<!-- licence-footer -->

---

*Handrail by [Keith Crawford](https://keithcrawford.me). Licensed [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). If you adapt this page, keep this line and say what you changed.*
