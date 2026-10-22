---
record_id: SAAS-04
version: 1
date: '2026-10-22'
tool: Prior-authorization drafting
vendor_or_builder: Built in-house by the product team
plan: Internal build on a commercial model API under a business associate agreement (zero data retention)
kind: internal build
purpose: Draft prior-authorization requests from a patient's chart for staff at healthcare customers to review and
  submit
requester: VP Product
business_owner: General manager, healthcare line
technical_owner: Product engineering lead
assessed_by: GRC analyst
third_party_model: true
profile: examples/saas-company/profile.yaml
ceilings_in_force:
  data_class: confidential
  autonomy: high
  training: no_training_on_non_public_data
  people_decisions: true
model_version: 0.6.0
model_sha256: unverified
upstream_version: AI Security Risk Workbook v3.0 (b775ec3)
architecture: human_facing_llm
scores:
  data.sensitivity: Severe
  data.persistence: Medium
  data.contract_coverage: Low
  people.audience: High
  people.reliance: Low
  people.decision_impact: High
  people.disclosure: Medium
  capability.function: Low
  capability.autonomy: Low
  capability.reversibility: Low
  capability.access: Medium
  capability.integration: High
  capability.untrusted_input: Medium
  capability.external_reach: Medium
provisional: []
confirmations:
- question: exfiltration_path
  by: Security engineer
  role: security review
  how: Drafts render as plain text with no link or image loading (tested with an image address the team controls);
    the feature sends nothing
  date: '2026-10-20'
- question: data.contract_coverage
  by: Privacy officer
  role: HIPAA program owner
  how: 'Model provider BAA and API terms read: business associate obligations, no training, zero retention, named
    entity and plan'
  date: '2026-10-20'
- question: data.persistence
  by: Security engineer
  role: security review
  how: 'Zero-retention terms read; logging configuration checked: 30 days, encrypted, PHI access controls'
  date: '2026-10-20'
- question: treatments
  by: Privacy officer
  role: HIPAA program owner
  how: Walked each of the eleven designed-path treatments in the staging environment and the contracts; evidence
    filed with the record
  date: '2026-10-21'
trifecta:
  applies: false
  exfiltration_path_exists: false
  sensitive_data: 'Yes: PHI'
  untrusted_input: 'Yes: records from other providers'
  exfiltration_path: 'None: plain-text output to the requesting staff member only; no links, images or outbound
    sends'
  broken_leg: Exfiltration leg absent, confirmed by test (see confirmations).
ceiling_cited: 'data_class: Restricted data (PHI); approved on the designed path, not by exception'
tier: Severe
route: designed_path
designed_path: phi
agentic: false
functions:
- llm-prompt-processing-text
- ai-response-generation-text
- rag-with-confidential-documents
- hr-financial-or-pii-system-access
controls:
- id: POS-01
  owner: Internal
  status: Identified
  control: Tool registration
- id: POS-02
  owner: Internal
  status: Identified
  control: Risk classification
- id: POS-03
  owner: Internal
  status: Pending decision
  control: Approval obtained
- id: POS-04
  owner: Internal
  status: Identified
  control: Policy alignment
- id: POS-05
  owner: Internal
  status: Identified
  control: Owner assignment
- id: POS-06
  owner: Internal
  status: Identified
  control: Vendor assessment
- id: POS-07
  owner: Internal
  status: Identified
  control: Compliance mapping
- id: POS-08
  owner: Internal
  status: Identified
  control: Data residency review
- id: SHA-01
  owner: Internal
  status: Identified
  control: Tool visibility
- id: SHA-02
  owner: Internal
  status: Identified
  control: Sanctioned status
- id: SHA-03
  owner: Internal
  status: Identified
  control: User access tracked
- id: SHA-04
  owner: Internal
  status: Identified
  control: Usage analytics
- id: OBS-01
  owner: Shared
  status: Identified
  control: Audit logging
- id: OBS-02
  owner: Shared
  status: Identified
  control: Log retention
- id: OBS-03
  owner: Shared
  status: Identified
  control: SIEM integration
- id: OBS-04
  owner: Shared
  status: Identified
  control: Alerting configured
- id: OBS-05
  owner: Shared
  status: Identified
  control: Performance and drift monitoring
- id: OBS-06
  owner: Shared
  status: Gap
  control: Red team and adversarial testing
- id: OBS-07
  owner: Shared
  status: Identified
  control: Bias and fairness testing
- id: DAT-01
  owner: Shared
  status: Identified
  control: DLP rules active
- id: DAT-02
  owner: Shared
  status: Identified
  control: PII detection
- id: DAT-03
  owner: Shared
  status: Identified
  control: Data classification
- id: DAT-04
  owner: Shared
  status: Identified
  control: Encryption in transit
- id: DAT-05
  owner: Shared
  status: Identified
  control: Encryption at rest
- id: DAT-06
  owner: Shared
  status: Identified
  control: Data masking
- id: DAT-07
  owner: Shared
  status: Identified
  control: Retention policies
- id: DAT-08
  owner: Shared
  status: Identified
  control: Training data opt-out
- id: DAT-10
  owner: Shared
  status: Identified
  control: Incident disclosure to users
- id: NHI-01
  owner: Internal
  status: Identified
  control: Service account scoping
- id: NHI-02
  owner: Internal
  status: Identified
  control: Secrets management
- id: NHI-03
  owner: Internal
  status: Identified
  control: Credential rotation
- id: NHI-05
  owner: Internal
  status: Identified
  control: Agent authentication
- id: RUN-01
  owner: Internal
  status: Identified
  control: Input validation
- id: RUN-02
  owner: Internal
  status: Identified
  control: Output filtering
- id: RUN-03
  owner: Internal
  status: Identified
  control: Rate limiting (per user)
- id: RUN-05
  owner: Internal
  status: Identified
  control: Content safety
- id: RUN-09
  owner: Internal
  status: Identified
  control: Fallback and graceful degradation
- id: SUP-01
  owner: Internal
  status: Identified
  control: Model provenance
- id: SUP-02
  owner: Internal
  status: Identified
  control: Model version pinning
- id: SUP-03
  owner: Internal
  status: Identified
  control: Model rollback procedure
- id: SUP-08
  owner: Internal
  status: Identified
  control: Third-party model assessment
- id: SUP-10
  owner: Internal
  status: Identified
  control: Vector store security
- id: SUP-11
  owner: Internal
  status: Identified
  control: System prompt protection
- id: SUP-12
  owner: Internal
  status: Identified
  control: Embedding integrity
findings:
- id: F-01
  severity: High
  finding: No adversarial testing yet against injected text in outside records.
  controls:
  - OBS-06
  owner: Security
  due: Before go-live
questions:
- to: Model provider
  question: Does your ISO/IEC 42001 certification, if any, cover the API used here?
  moves: None directly; recorded for the register
impact_assessment_required: true
decision: {}
---

# AI assessment record: Prior-authorization drafting

*Fictional worked example. Every source named below is illustrative; no real document was reviewed.*

## 1. Summary

A product feature that drafts prior-authorization requests from one patient's chart for staff at healthcare customers, who edit and submit them. The tier is Severe because the data is PHI, and that is the only Severe rating. The company runs a HIPAA program as a business associate, the lethal trifecta does not apply (no way out), the agreements are in place, and every designed-path treatment is identified, so it is approved on the designed path by the committee with the CISO, without an exception. One gap, adversarial testing, is due before go-live.

**Tier:** Severe **Dominant surface:** Data **Agentic:** no

**Routing:** decided by AI governance committee with the CISO; remaining risk accepted by Business unit head; decision within 30 working days; review quarterly.

## 2. Decision (completed by the approver)

| Decision | Conditions | Decided by | Date | Remaining risk accepted by | Exception reference | Next review |
| --- | --- | --- | --- | --- | --- | --- |
| | | | | | | |

## 3. What the tool is

| Field | Answer |
| --- | --- |
| Kind of request | Internal build |
| Technical owner | Product engineering lead |
| What it does | Draft prior-authorization requests from a patient's chart for staff at healthcare customers to review and submit |
| Data it reaches | The chart of the one patient named in the request, inside the customer's tenant: notes, orders, diagnoses, payer details (PHI) |
| Who uses it | Authorization staff at healthcare customers |
| Who sees its output | The staff member who requested the draft; they edit and submit it to the payer |
| Integrations and connectors | Chart data from the product's own database; no outbound connectors |
| Model provider behind it | A commercial model API under a business associate agreement |
| Plan | Internal build on a commercial model API under a business associate agreement (zero data retention) |

## 4. Scores

| Question | Rating | Basis | Source |
| --- | --- | --- | --- |
| Data sensitivity | Severe | Protected health information from healthcare customers' charts. | Product data map |
| Retention and training | Medium | The model provider keeps nothing (zero data retention). Prompts and drafts are logged for 30 days, encrypted, and treated as PHI. | Model provider business associate agreement and API terms, reviewed 2026-10-20; logging configuration |
| Contract coverage | Low | Business associate agreements are in place with the model provider and with every healthcare customer; no training on the data, in writing. | BAAs and model provider API terms, reviewed 2026-10-20 |
| Audience | High | Staff at customer organizations see the draft before anyone at the company does. | Product design |
| Reliance | Low | Staff edit 42% of drafts and every draft is submitted by a person. | Beta metrics export, 2026-10-19 |
| Decision impact | High | A wrong or weak request can delay a patient's access to care; it can be corrected and resubmitted. | Clinical advisor |
| Disclosure and consent | Medium | Customer contracts and the product documentation state that drafts are AI-assisted. | Customer terms, AI features section |
| Function | Low | Assist: drafts a request for a person who decides what to submit. | Product design |
| Autonomy | Low | A person starts each draft and submits it. | Product design |
| Reversibility | Low | Nothing is sent or changed by the feature. | Product design |
| Access | Medium | Reads the one chart named in the request, scoped in code to the requesting tenant and patient. | Code review; access tests |
| Integration | High | Direct read access to chart data in production. | Architecture note |
| Untrusted input | Medium | Charts include records faxed or sent by other providers (known outside parties). | Product data map |
| External reach | Medium | Calls one allowlisted model API; egress is logged. | Egress policy |

**Lethal trifecta:** does not apply. Sensitive data: Yes: PHI. Untrusted input: Yes: records from other providers. Exfiltration path: None: plain-text output to the requesting staff member only; no links, images or outbound sends. Broken leg: Exfiltration leg absent, confirmed by test (see confirmations).

**Ceilings in force:** the example profile (data_class confidential, autonomy high, training no_training_on_non_public_data, people_decisions True). **Crossed:** none.

**Conditions:** none.

## 5. Functions and the controls they require

Functions: `llm-prompt-processing-text`, `ai-response-generation-text`, `rag-with-confidential-documents`, `hr-financial-or-pii-system-access`.

| Control | Name | Owner | Status | Note |
| --- | --- | --- | --- | --- |
| POS-01 | Tool registration | Internal | Identified |  |
| POS-02 | Risk classification | Internal | Identified |  |
| POS-03 | Approval obtained | Internal | Pending decision | Met when the approver signs the decision |
| POS-04 | Policy alignment | Internal | Identified |  |
| POS-05 | Owner assignment | Internal | Identified |  |
| POS-06 | Vendor assessment | Internal | Identified | Model provider assessed; business associate agreement signed |
| POS-07 | Compliance mapping | Internal | Identified | HIPAA mapped; data-flow map on file |
| POS-08 | Data residency review | Internal | Identified |  |
| SHA-01 | Tool visibility | Internal | Identified |  |
| SHA-02 | Sanctioned status | Internal | Identified |  |
| SHA-03 | User access tracked | Internal | Identified |  |
| SHA-04 | Usage analytics | Internal | Identified |  |
| OBS-01 | Audit logging | Shared | Identified | Audit log of every chart read |
| OBS-02 | Log retention | Shared | Identified |  |
| OBS-03 | SIEM integration | Shared | Identified |  |
| OBS-04 | Alerting configured | Shared | Identified |  |
| OBS-05 | Performance and drift monitoring | Shared | Identified |  |
| OBS-06 | Red team and adversarial testing | Shared | Gap | No adversarial testing yet against injected text in outside records. |
| OBS-07 | Bias and fairness testing | Shared | Identified |  |
| DAT-01 | DLP rules active | Shared | Identified | DLP on prompts and drafts |
| DAT-02 | PII detection | Shared | Identified |  |
| DAT-03 | Data classification | Shared | Identified |  |
| DAT-04 | Encryption in transit | Shared | Identified | TLS to the model API |
| DAT-05 | Encryption at rest | Shared | Identified | Logs and caches encrypted at rest |
| DAT-06 | Data masking | Shared | Identified | Identifiers the payer does not need are masked |
| DAT-07 | Retention policies | Shared | Identified | 30-day retention, logs treated as PHI |
| DAT-08 | Training data opt-out | Shared | Identified | No training, in the agreement and the API terms |
| DAT-10 | Incident disclosure to users | Shared | Identified | Breach notice timelines in the customer BAAs |
| NHI-01 | Service account scoping | Internal | Identified | Access scoped to the requesting tenant and patient |
| NHI-02 | Secrets management | Internal | Identified |  |
| NHI-03 | Credential rotation | Internal | Identified |  |
| NHI-05 | Agent authentication | Internal | Identified |  |
| RUN-01 | Input validation | Internal | Identified |  |
| RUN-02 | Output filtering | Internal | Identified |  |
| RUN-03 | Rate limiting (per user) | Internal | Identified |  |
| RUN-05 | Content safety | Internal | Identified |  |
| RUN-09 | Fallback and graceful degradation | Internal | Identified |  |
| SUP-01 | Model provenance | Internal | Identified |  |
| SUP-02 | Model version pinning | Internal | Identified |  |
| SUP-03 | Model rollback procedure | Internal | Identified |  |
| SUP-08 | Third-party model assessment | Internal | Identified |  |
| SUP-10 | Vector store security | Internal | Identified |  |
| SUP-11 | System prompt protection | Internal | Identified |  |
| SUP-12 | Embedding integrity | Internal | Identified |  |

## 6. Agent threat model

The main path is text in a record from another provider that tries to steer the draft or pull in another patient's details. Patient-scoped access and staff review break that path today; adversarial testing will confirm it.

| Threat | What it looks like here | Controls |
| --- | --- | --- |
| Spoofing | A request names a patient outside the requester's tenant | Tenant and patient scoping in code |
| Tampering | Injected text in an outside record changes the draft | Staff review; adversarial testing due (OBS-06) |
| Repudiation | Nobody can show what was drafted | Audit log (OBS-01) |
| Information disclosure | Another patient's details appear in a draft | Patient-scoped retrieval; DLP |
| Denial of service | Bulk requests exhaust the model quota | Per-tenant rate limits |
| Elevation of privilege | The service account reads beyond the patient | Code-level scope (NHI-01) |

MAESTRO layers checked: 1, 2, 3, 7. OWASP: LLM01, LLM02. MITRE ATLAS: AML.T0051, AML.T0057.

## 7. Build documentation

Not required: not an internal build.

## 8. Findings

| ID | Severity | Finding | Controls | Owner | Due |
| --- | --- | --- | --- | --- | --- |
| F-01 | High | No adversarial testing yet against injected text in outside records. | OBS-06 | Security | Before go-live |

## 9. Questions

| To | Question | Rating it would move |
| --- | --- | --- |
| Model provider | Does your ISO/IEC 42001 certification, if any, cover the API used here? | None directly; recorded for the register |

## 10. Impact assessment

**HARM statement:** If the drafting feature is wrong, manipulated by text in an outside record, or over-authorized, then a weak or wrong request, or another patient's information, could reach a payer, resulting in delayed care for the patient and a reportable breach for the customer and the company.

| Question | Answer |
| --- | --- |
| Who is affected, and are any of them vulnerable? | Patients of healthcare customers, some of them seriously ill. |
| How do they rely on the output? | They do not see it; staff review and submit it on their behalf. |
| What harm could they suffer, and how reversible is it? | Delayed authorization (reversible on resubmission); disclosure of PHI (not reversible). |
| How will they know AI was involved, and how can they question the result? | Customers disclose AI-assisted drafting under their notices; patients appeal through the payer as usual. |
| What reduces the harm, and who owns each measure? | Patient-scoped access (engineering); staff review with edit-rate monitoring (customer success); adversarial testing before go-live (security). |

## 11. Verification after go-live

Not started: the tool is not approved yet. After go-live, each control in section 5 is marked Pass or Fail here with its evidence.

## 12. Sources

- Product data map
- Model provider business associate agreement and API terms, reviewed 2026-10-20; logging configuration
- BAAs and model provider API terms, reviewed 2026-10-20
- Product design
- Beta metrics export, 2026-10-19
- Clinical advisor
- Customer terms, AI features section
- Code review; access tests
- Architecture note
- Egress policy

All sources are illustrative. Nothing in this record was assumed without a named confirmer.

<!-- licence-footer -->

---

*Handrail by [Keith Crawford](https://keithcrawford.me). Licensed [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). If you adapt this page, keep this line and say what you changed.*
