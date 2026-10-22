# AI inventory: Example Advisory

*Fictional worked example. The same rows, with every column, are in [inventory.csv](inventory.csv). Columns left out here (used by, used for, autonomy, reversibility, provisional, exception) are blank or as the CSV shows.*

| ID | Tool and plan | Information that goes in | Sensitivity | Retention | Contract | Audience | Reliance | Impact | Function | Outside content | Disclosure | Trifecta | Tier | Tier as first set up | Owner's decision | Conditions | Next review |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CP-01 | Chat assistant, personal accounts (two consultants) | Client strategy notes, sometimes client customer lists | High | Severe | Severe | Low | Medium | Medium | Low | High | High | Applies | Severe |  | Banned | Not for any work. Replaced by the firm's business plan of the same tool (CP-05) | 2027-01 |
| CP-02 | Office-suite assistant, business plan | All firm and client documents, and inbound email | High | Medium | Low | Low | Low | Medium | Low | High | Medium | Broken | High | Severe | Allow with conditions | Web search and web content in answers turned off in the admin center; the assistant drafts but sends nothing; remote images and links are not loaded in its answers (admin setting checked 2026-10-20). Every client-facing draft is reviewed before sending. Owner decided in writing 2026-10-20 | 2027-04 |
| CP-03 | Video-call notetaker, business plan | Whatever is said on calls | High | Medium | Low | Low | Medium | Medium | Low | Medium | Medium | Broken | High | Severe | Allow with conditions | Automatic sharing of summaries switched off; the host reviews before sharing; recording announced and consent asked at the start; retention set to 90 days by the admin | 2027-04 |
| CP-04 | Writing assistant (plan not confirmed) | Client deliverables | High | Severe (u) | Severe (u) | Low | Low | Medium | Low | Low | Medium | No | Severe |  | Banned | Paused for client work until the plan and its training terms are confirmed. Trifecta: no outside content (it only polishes the firm's own drafts) | When the plan is confirmed |
| CP-05 | Chat assistant, business plan | Client strategy notes and financial statements under NDA | High | Medium | Low | Low | Medium | Medium | Low | Medium | Medium | Broken | High | Severe | Allow with conditions | Web browsing, connectors and link previews turned off in the workspace admin settings (checked 2026-10-21); remote images do not load in answers (vendor documentation, and a recorded test with an image address the firm controls, 2026-10-21). Account numbers redacted from statements before upload; client customer lists stay out. With browsing on it would be Severe (lethal trifecta) | 2027-04 |

## How three of the rows were scored

**CP-03, the notetaker.** As first set up, it emailed a summary to every attendee automatically, including clients. That made audience High and function "take action", and the follow-up questions found the lethal trifecta: client information, outside speakers, and output sent straight back to them. Severe. The owner switched automatic sharing off and had hosts review summaries before sharing them, which broke the outbound leg. The row keeps both tiers, so anyone can see that switching sharing back on makes it Severe again.

**CP-02 and CP-05, the office-suite and chat assistants.** Both read outside content (inbound email, files clients send) and handle client material. With web search, link previews or connectors on, each could put that material where an outsider can see it, which is the lethal trifecta. The firm turned those settings off, checked them in the admin console, and wrote them into the conditions.

**CP-04, the writing assistant.** Nobody knew whether the three consultants were on a free or business plan. Under the "unknown is worst" rule, retention and training, and contract coverage, were both rated Severe and marked "(u)". The tier is provisional until someone checks. If the plan turns out to be a business plan with no training, the likely outcome is High with conditions, like CP-05.

<!-- licence-footer -->

---

*Handrail by [Keith Crawford](https://keithcrawford.me). Licensed [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). If you adapt this page, keep this line and say what you changed.*
