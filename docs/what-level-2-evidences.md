# What Level 2 evidences for ISO/IEC 42001 and SOC 2

*For a team asked by a customer or prospect whether it "aligns to ISO 42001". References are clause and control numbers with short titles; you need your own copy of the standard for the requirements themselves.*

## The honest answer

Level 2 gives you operational controls for AI that map to much of ISO/IEC 42001 Annex A and to parts of clauses 5 to 8. It does not give you the AI management system around them: a defined scope, objectives, a Statement of Applicability, internal audit, management review and corrective action. Those are Level 3.

A fair way to put it to a prospect: "Our AI governance covers policy, roles, an inventory, risk and impact assessment of each AI use case, supplier checks, controls and incident handling, aligned to ISO/IEC 42001 Annex A. We have not built a certified management system."

## What Level 2 covers

| Level 2 artifact | ISO/IEC 42001 | SOC 2 criteria (IDs) |
| --- | --- | --- |
| [AI use policy](../kit/policy.md) | 5.2 AI policy; A.2.2 AI policy; A.2.3 Alignment with other organizational policies | CC1.1, CC5.3 |
| [Roles and responsibilities](../kit/roles.md), [charter](../kit/charter.md) | 5.1 Leadership and commitment; 5.3 Roles, responsibilities and authorities; A.3.2 AI roles and responsibilities | CC1.2, CC1.3 |
| [Staff briefing](../kit/staff-briefing.md) | 7.3 Awareness | CC1.4, CC2.2 |
| [AI register](../kit/ai-register.xlsx) | A.4.2 Resource documentation; 7.5 Documented information | CC3.2 |
| [Assessment record](../kit/assessment-record.md) and [scoring rubric](../kit/scoring-rubric.md) | 6.1.2 AI risk assessment; 8.2 AI risk assessment; A.9.4 Intended use of the AI system | CC3.2 |
| Required controls and findings in each record | Contributes to 6.1.3 AI risk treatment and 8.3 AI risk treatment (no Statement of Applicability yet) | CC5.1, CC5.2 |
| Impact assessment section of the record | 6.1.4 AI system impact assessment; 8.4 AI system impact assessment; A.5.2 AI system impact assessment process; A.5.3 Documentation of AI system impact assessments; A.5.4 Assessing AI system impact on individuals or groups of individuals | — |
| [Vendor terms check](../kit/vendor-terms-check.md) | A.10.3 Suppliers | CC9.2 |
| Data rules in the policy | A.4.3 Data resources; A.7.3 Acquisition of data; A.7.5 Data provenance | C1.1 |
| [Client disclosure](../kit/client-disclosure.md) | A.8.2 System documentation and information for users; A.8.5 Information for interested parties | CC2.3 |
| [Incident runbook](../kit/incident-runbook.md) | A.8.4 Communication of incidents | CC7.3, CC7.4, CC7.5 |
| [Review calendar](../kit/review-calendar.md) | 9.1 Monitoring, measurement, analysis and evaluation | CC4.1 |
| Build documentation in the record (internal builds) | A.6.2.2 AI system requirements and specification; A.6.2.4 AI system verification and validation; A.6.2.7 AI system technical documentation | CC8.1 |
| Verification after go-live | A.6.2.6 AI system operation and monitoring | CC4.1 |

## What Level 2 does not cover

| ISO/IEC 42001 | Why it is outside Level 2 |
| --- | --- |
| 4.1, 4.2, 4.3 (context, interested parties, scope) | Level 2 does not define the boundary of a management system |
| 6.2 AI objectives and planning to achieve them | No measurable AI objectives |
| 6.1.3 AI risk treatment, Statement of Applicability | Controls are chosen per use case; there is no organization-wide statement of which Annex A controls apply and why |
| 9.2 Internal audit, 9.3 Management review | No audit program or management review cycle |
| 10.1, 10.2 (improvement, nonconformity and corrective action) | Findings are tracked, but not as a corrective-action process |
| A.3.3 Reporting of concerns | No channel for raising AI concerns (planned) |
| A.5.5 Assessing societal impacts of AI systems | The impact assessment covers people and clients affected, not wider society |
| A.6.1.2, A.6.1.3 (objectives and processes for responsible development) | Builder processes beyond a per-system checklist |
| A.10.4 Customers | Responsibilities to your own customers as an AI provider |

The control catalog in [data/controls.yaml](../data/controls.yaml) has a crosswalk to Annex A for each control in [data/crosswalks/iso42001.yaml](../data/crosswalks/iso42001.yaml).

<!-- licence-footer -->

---

*Handrail by [Keith Crawford](https://keithcrawford.me). Licensed [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). If you adapt this page, keep this line and say what you changed.*
