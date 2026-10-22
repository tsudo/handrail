# The three surfaces of AI risk

Generic IT risk assessments rate a coding assistant and a customer-facing chatbot wired into the CRM the same way: "AI tool, Medium." They are not the same risk. The difference is in what each one touches, who it reaches, and what it can do. Those are the three surfaces.

## Data: what it touches, and what happens to it

- **Sensitivity.** The most sensitive information that goes in, or that it could produce. Output counts: a summary of a confidential meeting is confidential.
- **Retention and training.** Whether the vendor keeps what you send, for how long, and whether it trains its models on it.
- **Contract coverage.** Whether your terms with the vendor cover the information you will send.

A notetaker on a business plan with no training and a data processing agreement can be Medium on Data. The same notetaker on a personal account is Severe.

## People: who it reaches, and how much they trust it

- **Audience.** Who sees the output before anyone on your side has reviewed it. A draft a consultant rewrites before sending has an internal audience. A summary the tool emails to a client has an external one.
- **Reliance.** How much people trust the output before checking it, from "a person checks every output" to "the output makes the decision."
- **Decision impact.** Who outside your own team is affected if the output is wrong, and how badly: a person's money or job, or a client's decisions or confidential information.
- **Disclosure and consent.** Whether you have told the people affected what you must, and have their consent where it is needed, such as before recording a call.

This surface is the one most assessments leave out, and it is where the harm lands.

## Capability: what it can do on its own

- **Function.** The most it is allowed to do, from drafting for a person who decides, to sending and changing things, to operating without limits.
- **Autonomy and reversibility.** How much it does without a person approving each step, and whether its actions can be undone.
- **Access, integration and reach.** What it can read and change inside your systems, how deeply it is wired in, and what it can reach outside.
- **Untrusted input.** Whether it reads content nobody in your organization wrote or checked: web pages, inbound email, uploaded files. That is how instructions get injected.

## Why three, and not one score

The surfaces tell you what to do, not only how risky something is. If Data is the worst surface, the fix is usually contractual or a data rule. If People is the worst, the fix is a review step or a disclosure. If Capability is the worst, the fix is a permission, an approval gate or a sandbox.

Next: [why the worst surface decides](worst-surface.md).

<!-- licence-footer -->

---

*Handrail by [Keith Crawford](https://keithcrawford.me). Licensed [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). If you adapt this page, keep this line and say what you changed.*
