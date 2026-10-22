# Level 2: route and control

For organizations with more than one decision-maker, customers asking how AI is governed, or AI built into their own product. Level 2 keeps everything from [Level 1](level-1.md) and adds named roles, an intake route, an assessment record for each use case, a register, a review calendar and an incident runbook.

The worked example is a [SaaS company](../examples/saas-company/README.md) assessing a support assistant it is building, a sales meeting notetaker and a coding assistant.

## Step 1: Set up the program (one to two weeks, mostly waiting for people)

1. Fill the [roles sheet](../kit/roles.md) with names. Decide who approves at each tier.
2. Write your [organization profile](../kit/profile.yaml): program owner, who decides and accepts risk at each tier, decision targets, ceilings and the triggers from Step 2. Ceilings only tighten: set one stricter than the default to make it a control. The assessor skill reads this file; the [SaaS example's profile](../examples/saas-company/profile.yaml) shows one filled in.
3. If High decisions go to a committee, adopt the [charter](../kit/charter.md).
4. Complete the Level 2 sections of the [policy](../kit/policy.md): tiers, routing and decision targets, matching the profile.
5. Set up the [AI register](../kit/ai-register.xlsx). Move your Level 1 inventory into its first sheet.
6. Publish the [intake form](../kit/intake-form.md) and the [staff briefing](../kit/staff-briefing.md), and record acknowledgments on the register's Acknowledgments sheet.

## Step 2: Check which triggers apply

The definitions are in `triggers` in [data/model.yaml](../data/model.yaml). Record the ones you know now in your profile; add HIGH and AGENT after Step 3, once tools are assessed.

| Trigger | Applies when | Adds |
| --- | --- | --- |
| BUILD | You develop, fine-tune or ship AI | The build-documentation section of each record |
| HIGH | Any use case is rated High or Severe | Committee or senior decisions; quarterly reviews |
| AGENT | Any use case is agentic | The agent threat model section of each record |
| PEOPLE | AI output reaches customers, clients or the public, or informs decisions about people | Disclosure wording; an impact assessment for any use case with a People question High or above, or where the lethal trifecta applies |
| REG | Restricted data (health, payment, government IDs, biometrics, data about minors, privileged material) reaches an AI tool | Stricter data rules in the policy; legal review; check the agreement each vendor needs, such as a BAA for health data |
| EU | AI is offered to or used on people in the EU | See "EU AI Act" below |

## Step 3: Assess each use case (two to four hours each)

Copy the [assessment record](../kit/assessment-record.md) for each tool and purpose.

1. **Work out the kind of request.** A vendor product starts from the vendor's published terms. An AI feature added to a product you already use starts from the existing record: what changed, is it on by default, does the contract cover it? An internal build starts from the engineering owner's answers on the intake form, including whether data goes to a third-party model or AI API.
2. **Score all fourteen questions** with the [scoring rubric](../kit/scoring-rubric.md), for the tool as it is configured. Give each rating its basis and source.
3. **Check the lethal trifecta and your ceilings.** A leg counts as broken only with a document or a control you can point to.
4. **List the functions the tool performs** using the names in [data/functions.yaml](../data/functions.yaml). The required controls follow from them, plus the vendor controls for anything bought or built on a third-party model; mark each control's owner and status.
5. **Add the agent threat model** if the tool is agentic, and the build checklist if it is an internal build.
6. **Write findings** for every Gap, and up to four questions for anything that would move a rating.
7. **Add the impact assessment** if any People question is High or above, or the trifecta applies.

Keep your records in one folder and run `python tools/check --records <folder>`: it confirms each tier, the required controls, that every Gap has a finding, and that the agentic and impact-assessment flags match the scores.

The optional `handrail-assessor` skill in [plugin/](../plugin/README.md) can draft a record from your answers and the vendor's documents.

## Step 4: Route and decide

**Regulated data on the designed path.** If your organization runs a program for a kind of regulated data, such as PHI under HIPAA, declare it in your profile (`regulated_data_paths`). A use case whose only Severe rating is that data, with the lethal trifecta not applying, the required agreement in place, no training on the data, and every treatment control in `regulated_data_path` in [data/model.yaml](../data/model.yaml) Identified and confirmed in place by someone other than the requester, is approved on the designed path by the committee with the CISO, without an exception. The record keeps the tier Severe and sets `route: designed_path`. The [SaaS example](../examples/saas-company/README.md) shows one.

The tier sends the record to the person or committee the policy names, with a decision target: 2, 5, 15 or 30 working days for Low, Medium, High and Severe. The approver completes the decision section. The program owner updates the register and opens any exception.

## Step 5: Verify and review

Once a tool is live, walk the verification section of its record. Review each use case on the [review calendar](../kit/review-calendar.md), and early when a vendor changes its terms, a connector is added, or something goes wrong. Replace the Level 1 incident card with the [incident runbook](../kit/incident-runbook.md).

## EU AI Act

If the EU trigger applies, record it in the register against each affected use case and take one question to legal counsel: for this system, are you a provider, a deployer, or both? Your obligations depend on the answer and on whether the system is high-risk under the Act. A fuller EU guide is planned.

## When customers ask about ISO/IEC 42001

See [what Level 2 evidences](what-level-2-evidences.md): which clauses and Annex A controls Level 2 supports, and what it does not cover yet.

## When customers send a security questionnaire or ask about SOC 2

The [master crosswalk](crosswalk.md) ([spreadsheet](../kit/crosswalk.xlsx)) lists every control with its SOC 2, ISO/IEC 42001, NIST AI RMF, OWASP, MITRE ATLAS, EU AI Act and CSA AI Controls Matrix references. Filter its By framework sheet by a SOC 2 criterion to see which AI controls support it; the assessment records that list those controls hold the evidence.

<!-- licence-footer -->

---

*Handrail by [Keith Crawford](https://keithcrawford.me). Licensed [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). If you adapt this page, keep this line and say what you changed.*
