---
record_id: SAAS-03
version: 1
date: '2026-10-22'
tool: Coding assistant
vendor_or_builder: A coding-assistant vendor
plan: Business plan, completions and chat only (agent mode disabled by policy)
kind: vendor product
purpose: Code completion and chat for engineers on application repositories
requester: VP Engineering
business_owner: VP Engineering
technical_owner: Developer platform lead
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
architecture: human_facing_llm
scores:
  data.sensitivity: Medium
  data.persistence: Low
  data.contract_coverage: Low
  people.audience: Low
  people.reliance: Medium
  people.decision_impact: Low
  people.disclosure: Low
  capability.function: Low
  capability.autonomy: Low
  capability.reversibility: Low
  capability.access: Low
  capability.integration: Medium
  capability.untrusted_input: Medium
  capability.external_reach: Medium
provisional: []
confirmations: []
trifecta:
  applies: false
  exfiltration_path_exists: false
  sensitive_data: 'No: Internal code only'
  untrusted_input: 'Some: third-party code'
  exfiltration_path: 'None: agent mode and web fetching are off; suggestions stay in the editor'
  broken_leg: Sensitive-data leg absent.
ceiling_cited: null
tier: Medium
route: standard
designed_path: null
agentic: false
functions:
- llm-prompt-processing-text
- ai-response-generation-text
- code-repository-read-access
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
- id: OBS-05
  owner: Shared
  status: Identified
  control: Performance and drift monitoring
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
- id: RUN-01
  owner: Vendor
  status: Identified
  control: Input validation
- id: RUN-02
  owner: Vendor
  status: Identified
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
  status: Unknown
  control: System prompt protection
findings: []
questions:
- to: Vendor
  question: Does your ISO/IEC 42001 certification, if any, cover the coding assistant on the Business plan?
  moves: None directly; recorded for the register
impact_assessment_required: false
decision: {}
---

# AI assessment record: Coding assistant

*Fictional worked example. Every source named below is illustrative; no real document was reviewed.*

## 1. Summary

A vendor coding assistant on the Business plan, limited to completions and chat on repositories classified Internal. It is Medium: Internal code, no retention, no training, and nothing happens without the engineer. Switching on agent mode, or using it on a repository classified Confidential, needs a reassessment.

**Tier:** Medium **Dominant surface:** Capability, Data, People **Agentic:** no

**Routing:** decided by Department lead with security review; remaining risk accepted by Business owner of the use case; decision within 5 working days; review every six months.

## 2. Decision (completed by the approver)

| Decision | Conditions | Decided by | Date | Remaining risk accepted by | Exception reference | Next review |
| --- | --- | --- | --- | --- | --- | --- |
| | | | | | | |

## 3. What the tool is

| Field | Answer |
| --- | --- |
| Kind of request | Vendor product |
| Technical owner | Developer platform lead |
| What it does | Code completion and chat for engineers on application repositories |
| Data it reaches | Files open in the editor, from repositories classified Internal |
| Who uses it | Engineers |
| Who sees its output | The engineer using it |
| Integrations and connectors | IDE extension; agent mode off |
| Model provider behind it | Named in the vendor's subprocessor list |
| Plan | Business plan, completions and chat only (agent mode disabled by policy) |

## 4. Scores

| Question | Rating | Basis | Source |
| --- | --- | --- | --- |
| Data sensitivity | Medium | Used only on repositories the company classifies as Internal: application code with no secrets or core IP. Secret scanning blocks commits with credentials. | Repository classification register; secret-scanning configuration |
| Retention and training | Low | On the Business plan, prompts and suggestions are not retained after the response. | Vendor product-specific terms for the Business plan, reviewed 2026-10-17 |
| Contract coverage | Low | DPA in place; no training on Business customers' code, in writing. | Vendor DPA and product terms, reviewed 2026-10-17 |
| Audience | Low | Suggestions are seen only by the engineer using them. | Requester |
| Reliance | Medium | Engineers accept suggestions after a glance; code review catches some errors later. | Engineering lead |
| Decision impact | Low | Wrong suggestions affect internal work and are caught in review and tests. | Engineering lead |
| Disclosure and consent | Low | No disclosure obligation applies. | Legal |
| Function | Low | Assists: suggests code an engineer chooses to use. | Admin settings: agent mode off |
| Autonomy | Low | A person accepts each suggestion. | Admin settings |
| Reversibility | Low | No changes are made without the engineer. | Admin settings |
| Access | Low | Reads the files open in the editor. | Vendor documentation |
| Integration | Medium | IDE extension connected to the vendor's API. | Vendor documentation |
| Untrusted input | Medium | Third-party code from pinned, reviewed dependencies (known outside parties). The repositories have no public issue tracker or outside contributors; agent mode and web fetching are off. | Engineering lead; repository settings |
| External reach | Medium | Calls the vendor's allowlisted API. | Egress policy |

**Lethal trifecta:** does not apply. Sensitive data: No: Internal code only. Untrusted input: Some: third-party code. Exfiltration path: None: agent mode and web fetching are off; suggestions stay in the editor. Broken leg: Sensitive-data leg absent.

**Ceilings in force:** the example profile (data_class confidential, autonomy high, training no_training_on_non_public_data, people_decisions True). **Crossed:** none.

**Conditions:** none.

## 5. Functions and the controls they require

Functions: `llm-prompt-processing-text`, `ai-response-generation-text`, `code-repository-read-access`.

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
| OBS-05 | Performance and drift monitoring | Shared | Identified |  |
| DAT-03 | Data classification | Shared | Identified |  |
| DAT-04 | Encryption in transit | Shared | Identified |  |
| DAT-05 | Encryption at rest | Shared | Identified |  |
| DAT-07 | Retention policies | Shared | Identified |  |
| DAT-08 | Training data opt-out | Shared | Identified |  |
| DAT-10 | Incident disclosure to users | Shared | Identified |  |
| NHI-01 | Service account scoping | Internal | Identified |  |
| NHI-02 | Secrets management | Internal | Identified |  |
| NHI-03 | Credential rotation | Internal | Identified |  |
| RUN-01 | Input validation | Vendor | Identified |  |
| RUN-02 | Output filtering | Vendor | Identified |  |
| RUN-03 | Rate limiting (per user) | Vendor | Identified |  |
| RUN-05 | Content safety | Vendor | Identified |  |
| RUN-09 | Fallback and graceful degradation | Vendor | Identified |  |
| SUP-01 | Model provenance | Vendor | Identified |  |
| SUP-02 | Model version pinning | Vendor | Identified |  |
| SUP-03 | Model rollback procedure | Vendor | Identified |  |
| SUP-08 | Third-party model assessment | Vendor | Identified |  |
| SUP-11 | System prompt protection | Vendor | Unknown | Not applicable to a vendor-hosted assistant without a custom system prompt; confirm. |

## 6. Agent threat model

Not required: the tool is not agentic.

## 7. Build documentation

Not required: not an internal build.

## 8. Findings

None.

## 9. Questions

| To | Question | Rating it would move |
| --- | --- | --- |
| Vendor | Does your ISO/IEC 42001 certification, if any, cover the coding assistant on the Business plan? | None directly; recorded for the register |

## 10. Impact assessment

Not required: no People rating is High or above and the lethal trifecta does not apply.

## 11. Verification after go-live

Not started: the tool is not approved yet. After go-live, each control in section 5 is marked Pass or Fail here with its evidence.

## 12. Sources

- Repository classification register; secret-scanning configuration
- Vendor product-specific terms for the Business plan, reviewed 2026-10-17
- Vendor DPA and product terms, reviewed 2026-10-17
- Requester
- Engineering lead
- Legal
- Admin settings: agent mode off
- Admin settings
- Vendor documentation
- Engineering lead; repository settings
- Egress policy

All sources are illustrative. Nothing in this record was assumed without a named confirmer.

<!-- licence-footer -->

---

*Handrail by [Keith Crawford](https://keithcrawford.me). Licensed [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). If you adapt this page, keep this line and say what you changed.*
