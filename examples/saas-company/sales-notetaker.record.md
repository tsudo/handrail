---
record_id: SAAS-02
version: 1
date: '2026-10-22'
tool: Sales meeting notetaker
vendor_or_builder: A meeting-assistant vendor
plan: Business plan
kind: vendor product
purpose: Record and summarize sales calls and email a recap to every attendee
requester: VP Sales
business_owner: VP Sales
technical_owner: Sales operations manager
assessed_by: GRC analyst
third_party_model: false
profile: examples/saas-company/profile.yaml
ceilings_in_force:
  data_class: confidential
  autonomy: high
  training: no_training_on_non_public_data
  people_decisions: true
model_version: 0.6.0
model_sha256: unverified
upstream_version: AI Security Risk Workbook v3.0 (b775ec3)
architecture: machine_facing_llm
scores:
  data.sensitivity: High
  data.persistence: High
  data.contract_coverage: Medium
  people.audience: High
  people.reliance: Medium
  people.decision_impact: Medium
  people.disclosure: High
  capability.function: High
  capability.autonomy: High
  capability.reversibility: High
  capability.access: Medium
  capability.integration: Medium
  capability.untrusted_input: Medium
  capability.external_reach: Medium
provisional: []
confirmations: []
trifecta:
  applies: true
  exfiltration_path_exists: true
  sensitive_data: 'Yes: deal and pricing information'
  untrusted_input: 'Yes: what external attendees say'
  exfiltration_path: Recaps are emailed automatically to attendees, who are the authors of the untrusted input
  broken_leg: None as configured.
ceiling_cited: null
tier: Severe
route: standard
designed_path: null
agentic: true
functions:
- llm-prompt-processing-text
- ai-response-generation-text
- automated-messaging-and-email-send
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
- id: SHA-05
  owner: Internal
  status: Identified
  control: Personal-account blocking
- id: OBS-01
  owner: Shared
  status: Identified
  control: Audit logging
- id: OBS-02
  owner: Shared
  status: Identified
  control: Log retention
- id: OBS-04
  owner: Shared
  status: Identified
  control: Alerting configured
- id: OBS-05
  owner: Shared
  status: Identified
  control: Performance and drift monitoring
- id: OBS-08
  owner: Shared
  status: Identified
  control: Agent behavior monitoring
- id: DAT-04
  owner: Shared
  status: Identified
  control: Encryption in transit
- id: DAT-05
  owner: Shared
  status: Identified
  control: Encryption at rest
- id: DAT-07
  owner: Shared
  status: Unknown
  control: Retention policies
- id: DAT-08
  owner: Shared
  status: Identified
  control: Training data opt-out
- id: DAT-10
  owner: Shared
  status: Gap
  control: Incident disclosure to users
- id: NHI-06
  owner: Internal
  status: Identified
  control: Intent validation
- id: NHI-07
  owner: Internal
  status: Identified
  control: Tool and function authorization
- id: NHI-09
  owner: Internal
  status: Gap
  control: Autonomous action limits
- id: RUN-01
  owner: Vendor
  status: Identified
  control: Input validation
- id: RUN-02
  owner: Vendor
  status: Gap
  control: Output filtering
- id: RUN-03
  owner: Vendor
  status: Identified
  control: Rate limiting (per user)
- id: RUN-05
  owner: Vendor
  status: Identified
  control: Content safety
- id: RUN-09
  owner: Vendor
  status: Identified
  control: Fallback and graceful degradation
- id: SUP-01
  owner: Vendor
  status: Identified
  control: Model provenance
- id: SUP-02
  owner: Vendor
  status: Identified
  control: Model version pinning
- id: SUP-03
  owner: Vendor
  status: Identified
  control: Model rollback procedure
- id: SUP-08
  owner: Vendor
  status: Identified
  control: Third-party model assessment
- id: SUP-11
  owner: Vendor
  status: Identified
  control: System prompt protection
findings:
- id: F-01
  severity: High
  finding: No filtering of recap content before it is emailed.
  controls:
  - RUN-02
  owner: Business owner
  due: Before approval
- id: F-02
  severity: High
  finding: Outbound email needs no approval.
  controls:
  - NHI-09
  owner: Security
  due: Before approval
- id: F-03
  severity: High
  finding: No process to tell attendees about an AI incident.
  controls:
  - DAT-10
  owner: Business owner
  due: Before approval
questions:
- to: Vendor
  question: Does your ISO/IEC 42001 certification, if any, cover this product, and can recap emails require host
    approval before sending?
  moves: Function
- to: Vendor
  question: Which model provider processes recordings and transcripts, under what terms?
  moves: Contract coverage
impact_assessment_required: true
decision: {}
---

# AI assessment record: Sales meeting notetaker

*Fictional worked example. Every source named below is illustrative; no real document was reviewed.*

## 1. Summary

A vendor notetaker that records sales calls and emails a recap to every attendee automatically. It is Severe because it completes the lethal trifecta: it holds deal information, takes in what outside attendees say, and sends output back to them without review. Two configuration changes bring it to High: require the host to approve recaps before they are sent, and ask external attendees for consent at the start of each call.

**Tier:** Severe **Dominant surface:** (trifecta) **Agentic:** yes

**Routing:** decided by CISO and committee with an executive sponsor; remaining risk accepted by Named executive; decision within 30 working days; review monthly.

## 2. Decision (completed by the approver)

| Decision | Conditions | Decided by | Date | Remaining risk accepted by | Exception reference | Next review |
| --- | --- | --- | --- | --- | --- | --- |
| | | | | | | |

## 3. What the tool is

| Field | Answer |
| --- | --- |
| Kind of request | Vendor product |
| Technical owner | Sales operations manager |
| What it does | Record and summarize sales calls and email a recap to every attendee |
| Data it reaches | Audio, video and transcripts of sales calls; calendar entries; CRM contact records |
| Who uses it | Sales reps |
| Who sees its output | Every attendee, including prospects, by automatic email |
| Integrations and connectors | Calendar and CRM connectors |
| Model provider behind it | Not stated in the vendor's terms; asked (section 9) |
| Plan | Business plan |

## 4. Scores

| Question | Rating | Basis | Source |
| --- | --- | --- | --- |
| Data sensitivity | High | Calls cover prospects' plans, pricing and deal terms, and names and contact details of attendees. | Requester |
| Retention and training | High | Recordings and transcripts are stored by the vendor for the life of the account unless deleted. | Vendor terms of service for the Business plan, section 7, reviewed 2026-10-19 |
| Contract coverage | Medium | DPA in place and no training on customer content in writing; data residency not stated. | Vendor DPA and AI terms, reviewed 2026-10-19 |
| Audience | High | Recaps are emailed automatically to every attendee, including prospects, before anyone reviews them. | Admin settings screenshot |
| Reliance | Medium | Prospects and reps use recaps as the record of what was agreed. | Requester |
| Decision impact | Medium | A wrong recap can misstate terms to a prospect; corrected by a follow-up email. | Sales lead |
| Disclosure and consent | High | The bot joins announced by name, but nobody asks external attendees for consent to recording. | Two call recordings reviewed |
| Function | High | Takes action: emails recaps without approval. | Admin settings screenshot |
| Autonomy | High | Sends automatically within a narrow scope: recaps to that meeting's attendees. | Vendor documentation |
| Reversibility | High | An email, once sent, cannot be recalled. | Vendor documentation |
| Access | Medium | Reads and joins every meeting on connected calendars. | OAuth scopes granted |
| Integration | Medium | Calendar and CRM sync through the vendor's connectors. | Admin console |
| Untrusted input | Medium | Transcribes what external attendees say. | Vendor documentation |
| External reach | Medium | Vendor-hosted; sends email to attendee addresses. | Vendor documentation |

**Lethal trifecta:** applies. Sensitive data: Yes: deal and pricing information. Untrusted input: Yes: what external attendees say. Exfiltration path: Recaps are emailed automatically to attendees, who are the authors of the untrusted input. Broken leg: None as configured.

**Ceilings in force:** the example profile (data_class confidential, autonomy high, training no_training_on_non_public_data, people_decisions True). **Crossed:** none.

**Conditions:** none.

## 5. Functions and the controls they require

Functions: `llm-prompt-processing-text`, `ai-response-generation-text`, `automated-messaging-and-email-send`.

| Control | Name | Owner | Status | Note |
| --- | --- | --- | --- | --- |
| POS-01 | Tool registration | Internal | Identified |  |
| POS-02 | Risk classification | Internal | Identified |  |
| POS-03 | Approval obtained | Internal | Pending decision | Met when the approver signs the decision |
| POS-04 | Policy alignment | Internal | Identified |  |
| POS-05 | Owner assignment | Internal | Identified |  |
| POS-06 | Vendor assessment | Internal | Identified |  |
| POS-08 | Data residency review | Internal | Identified |  |
| SHA-01 | Tool visibility | Internal | Identified |  |
| SHA-02 | Sanctioned status | Internal | Identified |  |
| SHA-03 | User access tracked | Internal | Identified |  |
| SHA-04 | Usage analytics | Internal | Identified |  |
| SHA-05 | Personal-account blocking | Internal | Identified |  |
| OBS-01 | Audit logging | Shared | Identified |  |
| OBS-02 | Log retention | Shared | Identified |  |
| OBS-04 | Alerting configured | Shared | Identified |  |
| OBS-05 | Performance and drift monitoring | Shared | Identified |  |
| OBS-08 | Agent behavior monitoring | Shared | Identified |  |
| DAT-04 | Encryption in transit | Shared | Identified |  |
| DAT-05 | Encryption at rest | Shared | Identified |  |
| DAT-07 | Retention policies | Shared | Unknown | Retention can be shortened in settings; current value not confirmed. |
| DAT-08 | Training data opt-out | Shared | Identified |  |
| DAT-10 | Incident disclosure to users | Shared | Gap | No process to tell attendees about an AI incident. |
| NHI-06 | Intent validation | Internal | Identified |  |
| NHI-07 | Tool and function authorization | Internal | Identified |  |
| NHI-09 | Autonomous action limits | Internal | Gap | Outbound email needs no approval. |
| RUN-01 | Input validation | Vendor | Identified |  |
| RUN-02 | Output filtering | Vendor | Gap | No filtering of recap content before it is emailed. |
| RUN-03 | Rate limiting (per user) | Vendor | Identified |  |
| RUN-05 | Content safety | Vendor | Identified |  |
| RUN-09 | Fallback and graceful degradation | Vendor | Identified |  |
| SUP-01 | Model provenance | Vendor | Identified |  |
| SUP-02 | Model version pinning | Vendor | Identified |  |
| SUP-03 | Model rollback procedure | Vendor | Identified |  |
| SUP-08 | Third-party model assessment | Vendor | Identified |  |
| SUP-11 | System prompt protection | Vendor | Identified |  |

## 6. Agent threat model

The main path is content spoken on a call being written into a recap that the tool then sends: a prospect can steer what is recorded, and the tool sends it back to them without review. Requiring host approval breaks the outbound leg.

| Threat | What it looks like here | Controls |
| --- | --- | --- |
| Spoofing | A guest joins under a prospect's name | Host admits guests |
| Tampering | Something said on the call steers the recap | None as configured; host approval would catch it |
| Repudiation | A prospect disputes what the recap said was agreed | Recording retained; recap is not the contract |
| Information disclosure | Internal notes or pricing reach a prospect in a recap | None as configured (RUN-02 gap) |
| Denial of service | Not material for this tool |  |
| Elevation of privilege | The bot joins meetings beyond sales calls | Calendar scope limited to sales reps |

MAESTRO layers checked: 1, 2, 3, 7. OWASP: LLM02, LLM06, ASI09. MITRE ATLAS: AML.T0051.

## 7. Build documentation

Not required: not an internal build.

## 8. Findings

| ID | Severity | Finding | Controls | Owner | Due |
| --- | --- | --- | --- | --- | --- |
| F-01 | High | No filtering of recap content before it is emailed. | RUN-02 | Business owner | Before approval |
| F-02 | High | Outbound email needs no approval. | NHI-09 | Security | Before approval |
| F-03 | High | No process to tell attendees about an AI incident. | DAT-10 | Business owner | Before approval |

## 9. Questions

| To | Question | Rating it would move |
| --- | --- | --- |
| Vendor | Does your ISO/IEC 42001 certification, if any, cover this product, and can recap emails require host approval before sending? | Function |
| Vendor | Which model provider processes recordings and transcripts, under what terms? | Contract coverage |

## 10. Impact assessment

**HARM statement:** If the notetaker is wrong, manipulated by something said on a call, or over-authorized to send, then a recap misstating pricing, or containing internal notes, could reach a prospect, resulting in a misunderstanding about deal terms for the prospect and a disclosure of internal strategy for the company.

| Question | Answer |
| --- | --- |
| Who is affected, and are any of them vulnerable? | Prospects' staff on the call. No vulnerable groups. |
| How do they rely on the output? | They treat the recap as a record of what was agreed. |
| What harm could they suffer, and how reversible is it? | Misstated terms (correctable); being recorded without consent (not reversible). |
| How will they know AI was involved, and how can they question the result? | The bot is named on the call; recaps carry a footer naming the tool. Consent is not yet asked. |
| What reduces the harm, and who owns each measure? | Host approval before sending (sales operations); consent script at call start (sales lead); shorter retention (IT). |

## 11. Verification after go-live

Not started: the tool is not approved yet. After go-live, each control in section 5 is marked Pass or Fail here with its evidence.

## 12. Sources

- Requester
- Vendor terms of service for the Business plan, section 7, reviewed 2026-10-19
- Vendor DPA and AI terms, reviewed 2026-10-19
- Admin settings screenshot
- Sales lead
- Two call recordings reviewed
- Vendor documentation
- OAuth scopes granted
- Admin console

All sources are illustrative. Nothing in this record was assumed without a named confirmer.

<!-- licence-footer -->

---

*Handrail by [Keith Crawford](https://keithcrawford.me). Licensed [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). If you adapt this page, keep this line and say what you changed.*
