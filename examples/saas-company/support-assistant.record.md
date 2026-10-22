---
record_id: SAAS-01
version: 1
date: '2026-10-22'
tool: Support reply assistant
vendor_or_builder: Built in-house by the support engineering team
plan: Internal build on a commercial model API (zero data retention agreement)
kind: internal build
purpose: Draft replies to customer support tickets for an agent to edit and send
requester: Head of Support
business_owner: VP Customer Success
technical_owner: Support engineering lead
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
architecture: agentic
scores:
  data.sensitivity: High
  data.persistence: Medium
  data.contract_coverage: Low
  people.audience: Low
  people.reliance: Low
  people.decision_impact: High
  people.disclosure: Medium
  capability.function: Low
  capability.autonomy: Low
  capability.reversibility: Low
  capability.access: Medium
  capability.integration: High
  capability.untrusted_input: High
  capability.external_reach: Medium
provisional: []
confirmations:
- question: trifecta
  by: Support operations manager
  role: runs the agent workflow
  how: 'Pilot metrics export reviewed: every reply sent by an agent, 31% edited, 9% discarded'
  date: '2026-10-18'
trifecta:
  applies: false
  exfiltration_path_exists: true
  sensitive_data: 'Yes: customer account data'
  untrusted_input: 'Yes: tickets from any sender'
  exfiltration_path: Replies go back to the ticket's sender
  broken_leg: 'Exfiltration path broken: every reply is sent by a person after review, and the review is real (31%
    edit rate over four weeks, pilot metrics export). The scoped lookup would break the data leg as well once the
    open question in section 9 is answered.'
ceiling_cited: null
tier: High
route: standard
designed_path: null
agentic: true
functions:
- llm-prompt-processing-text
- ai-response-generation-text
- enterprise-data-queries-read-only
- internal-documentation-retrieval
- tool-and-function-calling-by-ai-agents
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
- id: OBS-08
  owner: Shared
  status: Identified
  control: Agent behavior monitoring
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
- id: NHI-04
  owner: Internal
  status: Identified
  control: Short-lived tokens
- id: NHI-05
  owner: Internal
  status: Identified
  control: Agent authentication
- id: NHI-06
  owner: Internal
  status: Gap
  control: Intent validation
- id: NHI-07
  owner: Internal
  status: Identified
  control: Tool and function authorization
- id: NHI-10
  owner: Internal
  status: Identified
  control: Agentic boundary controls
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
- id: RUN-04
  owner: Internal
  status: Identified
  control: Rate limiting (per workload)
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
  status: Unknown
  control: System prompt protection
findings:
- id: F-01
  severity: High
  finding: No adversarial testing yet against injected ticket content.
  controls:
  - OBS-06
  owner: Security
  due: Before go-live
- id: F-02
  severity: High
  finding: No intent validation on tool calls; relies on the code-level scope.
  controls:
  - NHI-06
  owner: Security
  due: Before go-live
questions:
- to: Engineering owner
  question: Can the lookup be called with a customer ID other than the ticket's authenticated customer, through
    any path?
  moves: Access
impact_assessment_required: true
decision: {}
---

# AI assessment record: Support reply assistant

*Fictional worked example. Every source named below is illustrative; no real document was reviewed.*

## 1. Summary

An in-house assistant that drafts support replies from the ticket, the help center and the requesting customer's account record. Agents edit and send every reply. It is High because it handles customer account data under contract, reads tickets from any sender, and a wrong answer about billing or account security affects the customer. The lethal trifecta is broken by design twice. Two control gaps (adversarial testing, intent validation) are due before go-live.

**Tier:** High **Dominant surface:** Capability, Data, People **Agentic:** yes

**Routing:** decided by AI governance committee; remaining risk accepted by Business unit head; decision within 10 working days; review quarterly.

## 2. Decision (completed by the approver)

| Decision | Conditions | Decided by | Date | Remaining risk accepted by | Exception reference | Next review |
| --- | --- | --- | --- | --- | --- | --- |
| | | | | | | |

## 3. What the tool is

| Field | Answer |
| --- | --- |
| Kind of request | Internal build |
| Technical owner | Support engineering lead |
| What it does | Draft replies to customer support tickets for an agent to edit and send |
| Data it reaches | The ticket, the help center, and the requesting customer's account record in the CRM |
| Who uses it | Support agents |
| Who sees its output | The agent handling the ticket; the customer sees only what the agent sends |
| Integrations and connectors | CRM read API (scoped in code), ticketing system |
| Model provider behind it | A commercial model API under a zero data retention agreement |
| Plan | Internal build on a commercial model API (zero data retention agreement) |

## 4. Scores

| Question | Rating | Basis | Source |
| --- | --- | --- | --- |
| Data sensitivity | High | Reads the ticket and the requesting customer's account record: names, contact details, plan and billing status, held under customer contracts. The ticket form does not ask for card data and masks card numbers on entry. | Engineering owner; masking rule seen in configuration |
| Retention and training | Medium | Prompts and outputs are logged in the company's own logging stack for 30 days. The model provider retains nothing under a zero data retention agreement. | Model provider data processing addendum, section 4, reviewed 2026-10-20 |
| Contract coverage | Low | DPA in place with the model provider; training on API data excluded in writing. | Model provider DPA and API data-use terms, reviewed 2026-10-20 |
| Audience | Low | Drafts are seen only by the support agent handling the ticket, who edits and sends them. | Engineering owner; workflow demonstrated |
| Reliance | Low | Agents edit 31% of drafts and discard 9% over the four-week pilot, so the review is real. | Pilot metrics export, 2026-10-18 |
| Decision impact | High | A wrong reply about billing, refunds or account security can cost a customer money or access, and can be corrected with effort. | Support lead |
| Disclosure and consent | Medium | The help-center terms already state that support may use AI-assisted drafting reviewed by staff. | Help-center terms, section 6 |
| Function | Low | Assist: drafts a reply for the agent, who decides what to send. It cannot send, refund or change anything. | Engineering owner; tool manifest |
| Autonomy | Low | Every reply is sent by a person. | Workflow demonstrated |
| Reversibility | Low | Read-only lookups; drafts are not sent by the tool. | Tool manifest |
| Access | Medium | The CRM service account can read every customer record; the tool's lookup is scoped in code to the ticket's authenticated customer. | Service account policy; code review |
| Integration | High | Direct API access to the CRM and the ticketing system. | Architecture note |
| Untrusted input | High | Reads tickets from any sender, including email-to-ticket intake. | Engineering owner |
| External reach | Medium | Calls one allowlisted model API; egress is logged. | Egress policy |

**Lethal trifecta:** does not apply. Sensitive data: Yes: customer account data. Untrusted input: Yes: tickets from any sender. Exfiltration path: Replies go back to the ticket's sender. Broken leg: Exfiltration path broken: every reply is sent by a person after review, and the review is real (31% edit rate over four weeks, pilot metrics export). The scoped lookup would break the data leg as well once the open question in section 9 is answered.

**Ceilings in force:** the example profile (data_class confidential, autonomy high, training no_training_on_non_public_data, people_decisions True). **Crossed:** none.

**Conditions:** none.

## 5. Functions and the controls they require

Functions: `llm-prompt-processing-text`, `ai-response-generation-text`, `enterprise-data-queries-read-only`, `internal-documentation-retrieval`, `tool-and-function-calling-by-ai-agents`.

| Control | Name | Owner | Status | Note |
| --- | --- | --- | --- | --- |
| POS-01 | Tool registration | Internal | Identified |  |
| POS-02 | Risk classification | Internal | Identified |  |
| POS-03 | Approval obtained | Internal | Pending decision | Met when the approver signs the decision |
| POS-04 | Policy alignment | Internal | Identified |  |
| POS-05 | Owner assignment | Internal | Identified |  |
| POS-06 | Vendor assessment | Internal | Identified | Model provider assessed: DPA, zero data retention and no-training terms reviewed 2026-10-20 |
| POS-08 | Data residency review | Internal | Identified |  |
| SHA-01 | Tool visibility | Internal | Identified |  |
| SHA-02 | Sanctioned status | Internal | Identified |  |
| SHA-03 | User access tracked | Internal | Identified |  |
| SHA-04 | Usage analytics | Internal | Identified |  |
| OBS-01 | Audit logging | Shared | Identified |  |
| OBS-02 | Log retention | Shared | Identified |  |
| OBS-03 | SIEM integration | Shared | Identified |  |
| OBS-04 | Alerting configured | Shared | Identified |  |
| OBS-05 | Performance and drift monitoring | Shared | Identified |  |
| OBS-06 | Red team and adversarial testing | Shared | Gap | No adversarial testing yet against injected ticket content. |
| OBS-08 | Agent behavior monitoring | Shared | Identified |  |
| DAT-01 | DLP rules active | Shared | Identified |  |
| DAT-02 | PII detection | Shared | Identified |  |
| DAT-03 | Data classification | Shared | Identified |  |
| DAT-04 | Encryption in transit | Shared | Identified |  |
| DAT-05 | Encryption at rest | Shared | Identified |  |
| DAT-07 | Retention policies | Shared | Identified |  |
| DAT-08 | Training data opt-out | Shared | Identified |  |
| DAT-10 | Incident disclosure to users | Shared | Identified |  |
| NHI-01 | Service account scoping | Internal | Identified |  |
| NHI-02 | Secrets management | Internal | Identified |  |
| NHI-03 | Credential rotation | Internal | Identified |  |
| NHI-04 | Short-lived tokens | Internal | Identified |  |
| NHI-05 | Agent authentication | Internal | Identified |  |
| NHI-06 | Intent validation | Internal | Gap | No intent validation on tool calls; relies on the code-level scope. |
| NHI-07 | Tool and function authorization | Internal | Identified |  |
| NHI-10 | Agentic boundary controls | Internal | Identified |  |
| RUN-01 | Input validation | Internal | Identified |  |
| RUN-02 | Output filtering | Internal | Identified |  |
| RUN-03 | Rate limiting (per user) | Internal | Identified |  |
| RUN-04 | Rate limiting (per workload) | Internal | Identified |  |
| RUN-05 | Content safety | Internal | Identified |  |
| RUN-09 | Fallback and graceful degradation | Internal | Identified |  |
| SUP-01 | Model provenance | Internal | Identified |  |
| SUP-02 | Model version pinning | Internal | Identified |  |
| SUP-03 | Model rollback procedure | Internal | Identified |  |
| SUP-08 | Third-party model assessment | Internal | Identified |  |
| SUP-10 | Vector store security | Internal | Identified |  |
| SUP-11 | System prompt protection | Internal | Unknown | System prompt extraction not yet tested. |

## 6. Agent threat model

The main path is prompt injection through a ticket: a sender writes instructions into the ticket asking the assistant to include another customer's details or wrong refund terms. The scoped lookup and agent review break that path today; adversarial testing will confirm it.

| Threat | What it looks like here | Controls |
| --- | --- | --- |
| Spoofing | A ticket claims to come from another customer | Lookup bound to the ticket's authenticated customer |
| Tampering | Injected text in a ticket changes the draft | Agent review; adversarial testing due (OBS-06) |
| Repudiation | Nobody can show what the assistant drafted | Prompt and output logging (OBS-01) |
| Information disclosure | Another customer's details appear in a draft | Scoped lookup; agent review |
| Denial of service | Floods of tickets exhaust the model quota | Per-workload rate limit |
| Elevation of privilege | The CRM service account reads every record | Code-level scope; intent validation due (NHI-06) |

MAESTRO layers checked: 1, 2, 3, 7. OWASP: LLM01, LLM02, LLM06, ASI01, ASI02. MITRE ATLAS: AML.T0051, AML.T0053, AML.T0057.

## 7. Build documentation

| Item | Status |
| --- | --- |
| Requirements and intended use written down | Yes: design document, approved 2026-09-30 |
| Model and version pinned | Yes: pinned in configuration; upgrades go through the release process |
| Data sources and their rights recorded | Yes: tickets, help center, CRM account record; covered by customer terms |
| Evaluation and red-team results on file | Evaluation set on file; adversarial testing not yet done (finding F-01) |
| Logging in place and where logs go | Prompts and outputs to the company's logging stack, 30 days |
| Rollback plan | Feature flag turns drafting off per team |

## 8. Findings

| ID | Severity | Finding | Controls | Owner | Due |
| --- | --- | --- | --- | --- | --- |
| F-01 | High | No adversarial testing yet against injected ticket content. | OBS-06 | Security | Before go-live |
| F-02 | High | No intent validation on tool calls; relies on the code-level scope. | NHI-06 | Security | Before go-live |

## 9. Questions

| To | Question | Rating it would move |
| --- | --- | --- |
| Engineering owner | Can the lookup be called with a customer ID other than the ticket's authenticated customer, through any path? | Access |

## 10. Impact assessment

**HARM statement:** If the support assistant is wrong, manipulated by an injected ticket, or over-authorized in the CRM, then wrong billing or account-security guidance, or another customer's account details, could reach a customer, resulting in financial loss or account exposure for that customer, and contract breach, notification duties and lost trust for the company.

| Question | Answer |
| --- | --- |
| Who is affected, and are any of them vulnerable? | Customers' account administrators and end users. No minors; some small-business customers depend on the product for payroll. |
| How do they rely on the output? | They receive the reply after an agent edits it; most act on it directly. |
| What harm could they suffer, and how reversible is it? | Wrong refund or billing guidance (reversible with effort); exposure of another customer's data (not reversible). |
| How will they know AI was involved, and how can they question the result? | Help-center terms disclose AI-assisted drafting; every reply invites a follow-up to a person. |
| What reduces the harm, and who owns each measure? | Scoped lookup (engineering); agent review with edit-rate monitoring (support lead); adversarial testing before go-live (security). |

## 11. Verification after go-live

Not started: the tool is not approved yet. After go-live, each control in section 5 is marked Pass or Fail here with its evidence.

## 12. Sources

- Engineering owner; masking rule seen in configuration
- Model provider data processing addendum, section 4, reviewed 2026-10-20
- Model provider DPA and API data-use terms, reviewed 2026-10-20
- Engineering owner; workflow demonstrated
- Pilot metrics export, 2026-10-18
- Support lead
- Help-center terms, section 6
- Engineering owner; tool manifest
- Workflow demonstrated
- Tool manifest
- Service account policy; code review
- Architecture note
- Engineering owner
- Egress policy

All sources are illustrative. Nothing in this record was assumed without a named confirmer.

<!-- licence-footer -->

---

*Handrail by [Keith Crawford](https://keithcrawford.me). Licensed [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). If you adapt this page, keep this line and say what you changed.*
