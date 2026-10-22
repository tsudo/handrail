---
# Licensed Apache-2.0 (LICENSE-code). Copyright 2026 Jason Robbins; modifications copyright 2026 Keith Crawford.
# Modified from the record format of the ai-tool-risk-assessment skill in the AI Security Risk Workbook v3.0
# by Jason Robbins. Changes: rescored on the Three Surfaces model (fourteen ratings, People surface, lethal
# trifecta), YAML front matter replaces JSON, impact assessment added, sections renumbered. See NOTICE.
# Three Surfaces assessment record (Level 2). Save a copy as <tool>.record.md.
# The YAML block is what tools/check reads; the sections below are what people read.
record_id: TS-YYYY-NNN
version: 1
date: YYYY-MM-DD
tool: "[Tool name]"
vendor_or_builder: "[Vendor, or internal team]"
plan: "[Plan or edition]"
kind: vendor product          # vendor product | vendor-added feature | internal build
purpose: "[What it will be used for]"
requester: "[Name, role]"
business_owner: "[Name, role]"
technical_owner: "[Name, role]"   # who runs it day to day (POS-05)
assessed_by: "[Name, role]"
third_party_model: false      # true when an internal build sends data to a third-party model or AI API
architecture: human_facing_llm   # human_facing_llm | machine_facing_llm | agentic | mcp_connected | edge_sovereign
profile: default              # organization profile used, or "default" (model.yaml defaults)
ceilings_in_force: {}         # from the profile, or the model.yaml defaults; looser values are ignored
model_version: 0.5.0
model_sha256: unverified      # SHA-256 of data/model.yaml, or "unverified"
upstream_version: "AI Security Risk Workbook v3.0 (b775ec3)"   # catalog source checked against
scores:                       # Low | Medium | High | Severe, worst plausible when unknown
  data.sensitivity: 
  data.persistence: 
  data.contract_coverage: 
  people.audience: 
  people.reliance: 
  people.decision_impact: 
  people.disclosure: 
  capability.function: 
  capability.autonomy: 
  capability.reversibility: 
  capability.access: 
  capability.integration: 
  capability.untrusted_input: 
  capability.external_reach: 
provisional: []               # questions resting on an unknown or unconfirmed answer
confirmations: []             # answers confirmed by a named person: {question, by, role, how, date}
                              # required for "trifecta" when a leg is broken, and for "data.sensitivity"
                              # below High when the other two legs are present
trifecta:
  applies: false
  exfiltration_path_exists: true  # false only with a confirmations entry for exfiltration_path
  sensitive_data: 
  untrusted_input: 
  exfiltration_path: 
  broken_leg: 
ceiling_cited:
tier:
route: standard               # standard | exception | designed_path (regulated data only; see regulated_data_path in data/model.yaml)
designed_path:                # the profile's regulated_data_paths id, when route is designed_path; needs
                              # confirmations for data.contract_coverage, data.persistence and treatments
tier_as_configured:           # only when a condition lowered the tier: the tier without it
conditions: []                # settings or rules the tier depends on
agentic: false
functions: []                 # ids from data/functions.yaml
controls: []                  # every required control: {id, owner, status, control}
findings: []                  # {id, severity, finding, controls: [ids], owner, due}
questions: []                 # up to four, plus any trifecta questions: {to, question, moves}
impact_assessment_required: false
decision: {}                  # left blank at issue; completed by the approver
---

# AI assessment record: [Tool name] for [purpose]

*Template. The YAML block above holds the data; fill it first, then write the sections below in plain sentences. Write in the third person: "the organization", "the vendor", "the tool". Every statement names its source. This record assesses; it never decides. The decision section stays blank until the approver completes it.*

## 1. Summary

One paragraph a business owner can read cold: what the tool does and what it reaches, what set the tier, what the evidence showed, and what is still open.

**Tier:** [tier] [provisional, if any question rests on an unknown] **Dominant surface:** [Data / People / Capability] **Agentic:** [yes / no]

**Routing:** [who decides, who accepts the remaining risk, decision target, review frequency, from the policy]

## 2. Decision (completed by the approver)

| Decision | Conditions | Decided by | Date | Remaining risk accepted by | Exception reference | Next review |
| --- | --- | --- | --- | --- | --- | --- |
| [Proceed / Proceed with conditions / Hold pending open items / Do not proceed / Escalate] | | | | | | |

## 3. What the tool is

Sources for these answers go in section 12.

| Field | Answer |
| --- | --- |
| Kind of request | [Vendor product / Vendor-added feature / Internal build] |
| Technical owner | |
| What it does | |
| Data it reaches | |
| Who uses it | |
| Who sees its output | |
| Integrations and connectors | |
| Model provider behind it | |
| Plan, and which controls the plan includes | |

## 4. Scores

The fourteen questions are in the scoring rubric (`kit/scoring-rubric.md`), copied from `data/model.yaml`. Give each rating with the fact that put it there and where that fact came from (intake form, the requester, the owner, a reviewed document with its section and date, or "unknown").

| Question | Rating | Basis | Source |
| --- | --- | --- | --- |
| Data sensitivity | | | |
| Retention and training | | | |
| Contract coverage | | | |
| Audience | | | |
| Reliance | | | |
| Decision impact | | | |
| Disclosure and consent | | | |
| Function | | | |
| Autonomy | | | |
| Reversibility | | | |
| Access | | | |
| Integration | | | |
| Untrusted input | | | |
| External reach | | | |

**Lethal trifecta:** [Sensitive data? Untrusted input? Exfiltration path? Which leg is broken by design, with evidence, or "none".]

**Ceilings in force:** [from the profile, or "model defaults"]. **Crossed:** [which, or "none".]

**Conditions:** [any setting or rule the tier depends on, and the tier without it.]

## 5. Functions and the controls they require

List every function the tool performs, using the names in [data/functions.yaml](../data/functions.yaml). The required controls are the union of each function's controls, plus the controls every tool needs (POS-01 to POS-05, SHA-01, SHA-02), plus POS-06 and SHA-05 whenever a third party supplies the AI: anything bought, and any internal build that sends data to a third-party model or AI API. Run `python tools/check --records <folder>` to confirm the set.

| Control | Name | Owner (Vendor / Internal / Shared / Unassigned) | Status (Identified / Gap / Unknown / Not applicable / Pending decision) | Control that meets it, and evidence |
| --- | --- | --- | --- |
| | | | |

A vendor statement that names the control and how it works counts as Identified ("prompts deleted after 30 days on the Business plan"). A vague one ("enterprise-grade security") is Unknown. A control the decision itself satisfies, such as POS-03 approval, is Pending decision until the approver signs. Every Gap has a finding.

## 6. Threat model (when agentic, or when untrusted input reaches people outside)

Required when the agentic flag is set, and when untrusted input is Medium or above and output reaches people outside the organization, even if the tool is not agentic.

One paragraph on how the tool could be misused and the one or two paths that matter most. Then one row for each of the six STRIDE threat types, a standard way to make sure no kind of attack is skipped:

| Threat | What it looks like here | Controls |
| --- | --- | --- |
| Spoofing | | |
| Tampering | | |
| Repudiation | | |
| Information disclosure | | |
| Denial of service | | |
| Elevation of privilege | | |

MAESTRO layers checked: 1 (foundation models), 2 (data operations), 3 (agent frameworks), 7 (multi-agent orchestration). OWASP Agentic Top 10 entries in play: [IDs]. MITRE ATLAS techniques: [IDs from data/atlas-ids.yaml].

## 7. Build documentation (internal builds only)

| Item | Status |
| --- | --- |
| Requirements and intended use written down | |
| Model and version pinned | |
| Data sources and their rights recorded | |
| Evaluation and red-team results on file | |
| Logging in place and where logs go | |
| Rollback plan | |

## 8. Findings

| ID | Severity | Finding | Controls | Owner | Due (Now / Before approval / Before go-live / At next review) |
| --- | --- | --- | --- | --- | --- |

## 9. Questions

Up to four, each one only if the answer would move a rating, plus any trifecta question still open (those are never dropped for the limit). Always ask a vendor whether it holds ISO/IEC 42001 certification covering this product.

| To | Question | Rating it would move |
| --- | --- | --- |

## 10. Impact assessment (when required)

Required when any People question is High or above, or when the lethal trifecta applies.

**HARM statement:** If [the tool] is wrong, manipulated, or over-authorized, then [specific harm] could occur to [the people or clients affected], resulting in [impact on them and on the organization].

| Question | Answer |
| --- | --- |
| Who is affected, and are any of them vulnerable (for example minors)? | |
| How do they rely on the output? | |
| What harm could they suffer, and how reversible is it? | |
| How will they know AI was involved, and how can they question the result? | |
| What reduces the harm, and who owns each measure? | |

## 11. Verification after go-live

Walk this list once the tool is live. Mark each required control Pass or Fail with the evidence collected.

| Control | What to check | Evidence | Pass / Fail | Date | Checked by |
| --- | --- | --- | --- | --- | --- |

## 12. Sources

Every document and page used, with date. Anything not reviewed, and anything assumed with who confirms it.
