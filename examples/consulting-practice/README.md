# Worked example: a consulting practice at Level 1

*Fictional organization. Licensed CC-BY-4.0.*

Example Advisory is a five-person management consulting practice. Client strategy documents, client customer lists shared under NDA and draft deliverables pass through the AI tools the team uses. A client asked "do you use AI on our work?", and the founder asked the office manager to "get us covered". This is what Level 1 produced: an afternoon for the first pass, and the remaining vendor questions within 30 days.

## The four documents, plus one

| Document | File |
| --- | --- |
| Policy, with the approved and banned list, data rules and the owner | [policy.md](policy.md) |
| Inventory with quick scores and the owner's decisions | [inventory.xlsx](inventory.xlsx), also as [Markdown](inventory.md) and [CSV](inventory.csv) |
| Vendor terms checks | [vendor-terms-checks.md](vendor-terms-checks.md) |
| Incident card | [incident-card.md](incident-card.md) |
| Client disclosure (AI output reaches clients) | [client-disclosure.md](client-disclosure.md) |

## What the scores showed

| ID | Tool | Tier | Decision | Why |
| --- | --- | --- | --- | --- |
| CP-01 | Chat assistant, personal accounts | Severe | Banned | Consumer terms allow training and there is no DPA |
| CP-02 | Office-suite assistant, business plan | High | Allow with conditions | Client material makes it High. It reads inbound email, so web search and sending stay off; with them on it would be Severe (lethal trifecta) |
| CP-03 | Video-call notetaker, business plan | High | Allow with conditions | Automatic sharing switched off; recording announced. With sharing on, it was Severe (lethal trifecta) |
| CP-04 | Writing assistant, plan unknown | Severe (provisional) | Banned for client work | Training and retention unknown until the plan is confirmed |
| CP-05 | Chat assistant, business plan | High | Allow with conditions | Replaces CP-01. Client files make it High; browsing, connectors and link previews stay off, or it would be Severe |

## The answer to the client

"Yes. We use an office-suite assistant, a chat assistant and a meeting notetaker, all on business terms that do not let the vendors train on your information, and a person on our team reviews everything we deliver. We stopped using personal AI accounts for client work. Your customer lists do not go into AI tools without your written agreement. We tell you before we record a call."

<!-- licence-footer -->

---

*Handrail by [Keith Crawford](https://keithcrawford.me). Licensed [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). If you adapt this page, keep this line and say what you changed.*
