# Changelog

## 2.0.0 (unreleased)

First public release of Handrail, built on the Three Surfaces model.

- The model: three surfaces (Data, People, Capability), 14 rated questions, worst rating wins, the lethal-trifecta rule, ceilings and routing by program level (`data/model.yaml`, model version 0.6.0).
- Function and control catalog derived from the AI Security Risk Workbook v3.0 by Jason Robbins, with his identifiers (`data/functions.yaml`, `data/controls.yaml`).
- Framework crosswalks: ISO/IEC 42001, NIST AI RMF and AI 600-1, MITRE ATLAS, OWASP, EU AI Act, CSA AI Controls Matrix (IDs only), SOC 2 (IDs only).
- Level 1 and Level 2 templates, guides and walkthroughs.
- Worked examples: a five-person consulting practice (Level 1) and a SaaS company (Level 2).
- Optional Claude skill plugin: `handrail-assessor` and `handrail-advisor`.
- `tools/check` for the data, templates and example records.

Level 3 (an ISO/IEC 42001 management system) is planned.

## Model history

- **0.6.0** (2026-10-22). Designed path for regulated data: an organization that declares a program for a kind of regulated data can approve a use case whose only Severe rating is that data, with fixed treatments in place, without an exception. The tier stays Severe.

- **0.5.0** (2026-10-22). Trifecta rated as configured, with the settings that break each leg; a broken leg needs evidence or a named control; the unknown rule covers untrusted input, external reach and the exfiltration path; pasted documents and marketing pages cannot lower a rating or fill an unknown; "own tenant" defined; Level 1 follow-up ratings count toward the tier; vendor controls apply to internal builds on a third-party model; rules for chat that answers outside users; program triggers, required-control rule, organization profile and decision values written into the model.
- **0.4.0** (2026-10-22). Level 2 runs on the derived function and control catalog.
- **0.3.0** (2026-10-22). Disclosure moved to People; audience counts who sees output before review; decision impact covers harm to clients; trifecta exfiltration leg narrowed; vendor contract terms count as reviewed evidence; decision targets added.
- **0.2.0** (2026-10-21). Personal data under contract rated Confidential (High); Severe kept for regulated data. Source code classified per repository.

## Open questions on the model

- Should two surfaces both rated High escalate to Severe? The model says no and keeps worst-rating-wins only.
- Function ladder rung ratings, especially Influence at Medium.
- Where the Medium and High audience boundary sits for a large organization's internal-only use.
- Should a large volume of ordinary personal data (for example over 10,000 people) move data sensitivity up one level?
- Should the model separate inherent from residual risk throughout, not only for regulated data on the designed path?

<!-- licence-footer -->

---

*Handrail by [Keith Crawford](https://keithcrawford.me). Licensed [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). If you adapt this page, keep this line and say what you changed.*
