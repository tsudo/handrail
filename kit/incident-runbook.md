# AI incident runbook (Level 2)

*Replaces the Level 1 incident card. Fit it into your existing incident process; this covers what is specific to AI.*

## What counts as an AI incident

- Information reached an AI tool or vendor it should not have.
- An AI tool sent, posted, changed or deleted something nobody approved.
- An AI tool was manipulated by content it read (prompt injection), or behaved outside its purpose.
- Someone was harmed by acting on AI output.
- A vendor reported a breach or a change affecting our data.

Use the words carefully. An event is not a breach until the facts say so; legal or privacy decides when notification duties apply.

## 1. Contain (first hour)

| Step | Who |
| --- | --- |
| Disable the tool, revoke its tokens or service accounts, or disconnect the integration | Whoever is on the roles sheet for "disable a tool" |
| Preserve logs, prompts, outputs and screenshots | Security |
| Open an incident record and note the time | Security |

## 2. Assess (first day)

- What information was involved, and how sensitive is it (use the data classes in the scoring rubric)?
- Who is affected: people, clients, customers?
- Did the tool act on its own? What did it send or change, and can it be undone?
- Was this prompt injection? Find the content that carried it.

## 3. Notify

| Who | When | Decided by |
| --- | --- | --- |
| Program owner and executive sponsor | Same day | Security |
| Clients or customers | Per their contracts; often 24 to 72 hours | Legal or privacy |
| Regulators | Only where law requires, on legal's advice | Legal or privacy |
| The vendor | When their action is needed (deletion, investigation) | Security |

## 4. Recover and learn

- Fix the cause; reassess the use case before it is switched back on.
- Add a finding to the assessment record and the AI register, with an owner and due date.
- Update the policy, the controls or the disclosure wording if they were part of the cause.
- Report in the next committee summary.

<!-- licence-footer -->

---

*Handrail by [Keith Crawford](https://keithcrawford.me). Licensed [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). If you adapt this page, keep this line and say what you changed.*
