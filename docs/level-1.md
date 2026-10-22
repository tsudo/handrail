# Level 1: know and decide

*The level wording inside the rubric blocks on this page comes from `data/model.yaml`; for six questions and the data classes it is adapted from the AI Security Risk Workbook v3.0 by Jason Robbins and stays Apache-2.0. See NOTICE.*

For small teams that buy AI tools rather than build them. You end up with four documents, five if anything AI produces reaches your clients.

**Plan on about four hours for four tools, each used for one purpose.** The times below are for that. Each extra row (a tool used for a second purpose, or a fifth tool) adds about 30 minutes. Three things wait until within 30 days: the last two vendor questions (who else gets your data, and where it is stored), the switch-off steps on the incident card, and the staff briefing. None changes a rating.

A filled-in version for a [five-person consulting practice](../examples/consulting-practice/README.md) is there if you want to see one. Unfamiliar words are in the [glossary](glossary.md).

| Step | Time for four tools |
| --- | --- |
| 0. Read this page and skim the worksheet | 10 minutes |
| 1. Name the owner | 5 minutes |
| 2. List every AI tool | 30 minutes |
| 3. Check each vendor's terms, questions 1 to 3 | 70 minutes (15 per tool; 20 for an AI feature inside software you already pay for, which has its own terms) |
| 4. Score each tool, checking settings in each admin console | 60 minutes (15 per tool) |
| 5. Decide | 20 minutes (5 per tool) |
| 6. Write the policy, starting from the example | 20 minutes |
| 7. Incident card: who to call | 10 minutes |
| 8. Client disclosure, if AI output reaches clients | 15 minutes |
| **Total** | **about 4 hours** |

## Step 1: Name the owner

Pick one person who decides whether an AI tool is allowed and on what terms, and a backup. Write both names in section 3 of the [policy](../kit/policy.md).

## Step 2: List every AI tool

Fill one row of the [inventory](../kit/inventory.xlsx) per tool and purpose. The spreadsheet has drop-down lists and works out the tier for you; the [Markdown version](../kit/inventory.md) has the same columns. Ask everyone; don't guess. Include:

- standalone AI tools, and which plan each is on (free, personal, business);
- AI features inside software you already pay for: meeting notetakers, writing assistants, "copilot" buttons in email and documents;
- personal accounts people use for work.

A tool used two ways, such as a chat assistant for internal research and for client drafts, gets two rows.

## Step 3: Check each vendor's terms, questions 1 to 3 (15 minutes per tool)

For each tool, answer questions 1 to 3 of the [vendor terms check](../kit/vendor-terms-check.md): training, retention and the data processing agreement. Those three set two of your ratings. The [plan-tiers guide](plan-tiers.md) says where vendors usually put each answer. Questions 4 and 5 can wait up to 30 days.

## Step 4: Score each tool (15 minutes per tool)

Use the [quick-score worksheet](../kit/quick-score-worksheet.md): seven questions, plus follow-ups when a tool handles confidential information, can act on its own, answers people outside your organization, or produces output that reaches clients. Rate each tool as it is set up today, and check the settings the worksheet asks about in the tool's admin console as you go. The worst rating, follow-ups included, is the tool's tier. If you will use the client disclosure in Step 8, rate Disclosure High for now and update it in Step 8. Copy the ratings into the inventory.

<!-- rubric: data.sensitivity -->
- **Low:** Public information only.
- **Medium:** Internal business information that is not sensitive.
- **High:** Confidential information such as strategy, proprietary code, or customer and employee personal data held under contract.
- **Severe:** Regulated information such as health data, payment or financial account data, government IDs, biometrics, data about minors, or privileged client material.
<!-- /rubric -->

*Above: the first question, as an example. Client material under an NDA is Confidential, so a tool that handles it starts at High on this question.*

## Step 5: Decide (5 minutes per tool)

The owner decides each tool once, by tier, and records one of four decisions: Allow, Allow with conditions, Banned, or Exception.

| Tier | Usual decision |
| --- | --- |
| Low | Allow |
| Medium | Allow with conditions |
| High | Ask first: the owner decides in writing before anyone uses it: Allow with conditions, or Banned |
| Severe | Banned, unless the owner grants a written, time-limited Exception. One case can be allowed without an exception; see "Regulated data your firm already handles" below |


**Regulated data your firm already handles.** A health practice or a financial adviser handles regulated data every day. A tool rated Severe *only* because of question 1 can be allowed with conditions, without an exception, when every one of these is true and written in the Conditions column:

- your firm already runs a written program for that data (for example HIPAA policies for a practice);
- the vendor has signed the agreement the law needs for that data (for example a business associate agreement) and its terms rule out training on it;
- no other rating is Severe, and the trifecta check found no outside content or no way out;
- the tool is limited to the records each task needs, and its retention is set;
- someone other than the person asking for the tool has read the agreement and checked the settings, and signs the row with the owner.

Review it every three months. If any item stops being true, the tool is Severe again and needs an exception. At Level 2 this is the designed path in the policy.

Write the decision and any conditions in the inventory. A High tool is decided once per tool and purpose; after that, everyday use under the conditions needs no further asking.

**If a condition lowers a rating**, such as switching off automatic sharing or web browsing, score the tool again with the condition and keep both tiers in the inventory ("Tier as first set up"). Do this whenever the tier depends on a setting, even one that was already off when you checked. The decision holds only while the condition does.

## Step 6: Write the policy (30 minutes)

Fill the Level 1 sections of the [policy](../kit/policy.md). The approved and banned list comes straight from the inventory. Starting from the [example policy](../examples/consulting-practice/policy.md) is faster.

## Step 7: Prepare for something going wrong (10 minutes now)

Fill the contacts on the [incident card](../kit/incident-card.md) now. Add how to switch off each tool within 30 days; the card says where the switch usually is.

## Step 8: If AI output reaches clients (15 minutes)

Use the [client disclosure language](../kit/client-disclosure.md) in your engagement letters or terms, and ask before recording client meetings. This applies even when someone on your team reviews the output before the client sees it. Once the wording is in use for new engagements and has been sent to current clients, and for a notetaker once auto-join is limited and consent is asked, change Disclosure to Medium in the inventory; the tier may drop.

## Within 30 days

- Vendor terms questions 4 and 5 for each tool.
- Switch-off steps for each tool on the incident card.
- Share the [staff briefing](../kit/staff-briefing.md).

## Then

Review each tool on the date in its inventory row: a year for Low and Medium, six months for High, three months for a Severe exception. Review sooner when someone wants a new tool or a vendor changes its terms. Move to [Level 2](level-2.md) when customers start asking how you govern AI, when you have more than one decision-maker, or when you build AI yourself.

<!-- licence-footer -->

---

*Handrail by [Keith Crawford](https://keithcrawford.me). Licensed [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). If you adapt this page, keep this line and say what you changed.*
