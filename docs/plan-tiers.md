# Consumer, business and enterprise AI plans

*Last checked: 2026-10. Vendors change plans and terms often. Use this guide to know what to look for, then check the current terms for the plan you actually use.*

The same AI tool can be safe for client work on one plan and unsafe on another. Most of the difference is in the contract, not the software.

## What usually changes between plans

| What to check | Free or personal plans usually | Team or business plans usually | Enterprise plans usually |
| --- | --- | --- | --- |
| Training on your inputs | On by default, sometimes with an opt-out | Off by default, stated in the terms | Off, stated in the contract |
| How long prompts and files are kept | Long or unstated | Stated, sometimes adjustable | Adjustable, sometimes zero retention |
| Data processing agreement (DPA) | None | Available, often self-serve | Negotiated |
| Who controls the account | The individual | The organization's admin | The organization, with single sign-on |
| Audit logs and admin controls | None | Some | Full, often exportable |
| Where data is processed | Unstated | Sometimes selectable | Selectable |

## What this means for scoring

- A personal or free account used for work usually rates **Severe** on retention and training, and **Severe** on contract coverage for any client or customer information. That is why most policies ban them for work.
- Moving the same tool to a business plan with no training, a DPA, and retention your admin controls often brings retention down to Medium and contract coverage to Low. The vendor still hosts the data; what changed is that your admin sets how long it is kept and the vendor may not train on it. That is what the worksheet means by "our own tenant". Some team plans let users delete their own chats but give the admin no retention setting; that is not your own tenant, and retention stays High.
- AI features inside software you already pay for usually follow that software's existing contract. Check whether the AI feature has its own terms and whether it was switched on by default. Which other model provider it sends data to is vendor question 4, which can wait 30 days.

## How to check a plan in fifteen minutes

1. Find which plan your organization is actually on. Ask whoever pays for it, or look in the admin console.
2. Open the vendor's documents for that plan (see the table below).
3. Answer questions 1 to 3 on the [vendor terms check](../kit/vendor-terms-check.md), quoting the sentence that answers each one. Questions 4 and 5 can wait up to 30 days.
4. If the terms are silent on training or retention, treat the answer as the worse one until the vendor confirms in writing.

## Where the answers usually are

| Question | Look in |
| --- | --- |
| Training on your data | The business or enterprise terms, product terms for your plan, or AI or data-use terms that those terms say are part of the contract; the admin console often shows the setting. A trust-center or FAQ page is a lead unless the contract includes it |
| Retention | The privacy or data-use terms for the plan; the admin console's retention settings |
| DPA | A "DPA" or "data processing addendum" link in the legal or trust section of the vendor's site; business plans often include it by reference |
| Subprocessors and model providers | A "subprocessors" page linked from the DPA |
| Where data is stored | The DPA or the trust center |

Read the documents on the vendor's own website, and check they are for your plan. A help article or blog post is a lead to the right document, not the answer.

## Meeting notetakers

Notetakers raise questions the other tools do not:

- **Training on "de-identified" or "aggregated" transcripts** is still training. Rate retention Severe unless the terms let you opt out and you have.
- **Voiceprints.** A tool that learns each speaker's voice to label them handles biometric data (Severe). One that takes speaker names from the meeting invite does not.
- **Joining automatically.** A notetaker that joins every meeting on a calendar records people who never chose it, so rate Disclosure High until auto-join is off or limited to meetings the user hosts.
- **Telling voiceprints from names.** Look for a speaker-recognition or "voice" setting and search the privacy policy for "voice". If the tool learns voices, rate question 1 Severe, or turn the setting off.
- **Sharing automatically.** Emailing a summary to every attendee is sending output outside before anyone reviews it, which usually completes the lethal trifecta. Turn it off and have the host review first.
- **Consent.** Some places require everyone on a call to agree to recording. Ask at the start of every recorded call (see the [client disclosure](../kit/client-disclosure.md) wording).

<!-- licence-footer -->

---

*Handrail by [Keith Crawford](https://keithcrawford.me). Licensed [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). If you adapt this page, keep this line and say what you changed.*
