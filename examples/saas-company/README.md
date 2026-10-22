# Worked example: a SaaS company at Level 2

*Fictional organization. Licensed CC-BY-4.0.*

A 300-person B2B software company with a SOC 2 Type II report. Some customers are healthcare organizations, for whom it acts as a HIPAA business associate. An enterprise prospect has asked whether it aligns to ISO/IEC 42001, and engineering is shipping an AI support assistant and an AI feature over patient charts. The GRC analyst runs Level 2 for four AI use cases.

| Record | Tool | Tier | Why | Next step |
| --- | --- | --- | --- | --- |
| [SAAS-01](support-assistant.record.md) | Support reply assistant | High | Customer data, outside senders' tickets, customer impact; trifecta broken by design | Committee decision; close two gaps before go-live |
| [SAAS-02](sales-notetaker.record.md) | Sales meeting notetaker | Severe | Lethal trifecta: automatic recaps to outside attendees | Require host approval and consent, then reassess at High |
| [SAAS-03](coding-assistant.record.md) | Coding assistant | Medium | Internal code, no retention, nothing happens without the engineer | Department lead approves; review in six months |
| [SAAS-04](prior-auth-drafting.record.md) | Prior-authorization drafting | Severe | PHI is the only Severe rating; HIPAA program, agreements and every treatment in place | Committee with the CISO approves on the designed path; adversarial testing before go-live |

## What the prospect is told

"Every AI system we use or build has a recorded risk and impact assessment, required controls with owners, and a review date, aligned to ISO/IEC 42001 Annex A. We have not built a certified AI management system." See [what Level 2 evidences](../../docs/what-level-2-evidences.md).

<!-- licence-footer -->

---

*Handrail by [Keith Crawford](https://keithcrawford.me). Licensed [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). If you adapt this page, keep this line and say what you changed.*
