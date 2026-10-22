# Security

Handrail is a governance kit: documents, data files, two Claude skills and a small Python checker. It runs no service.

## Reporting a problem

If you find a way to make the assessor skill or `tools/check` give a lower rating than the model's rules allow, a prompt-injection path through the skills, or anything else with security impact, report it privately through GitHub's **Report a vulnerability** button on this repository's Security tab. Please do not open a public issue for it.

Expect an acknowledgment within five working days.

## What `tools/check` does and does not do

`tools/check` confirms that a record is consistent with itself, the model and the catalog. It cannot tell whether what a record says is true, or verify who a confirmer or approver is. The named approver who signs each decision is that control.

<!-- licence-footer -->

---

*Handrail by [Keith Crawford](https://keithcrawford.me). Licensed [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). If you adapt this page, keep this line and say what you changed.*
