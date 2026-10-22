# Glossary

| Term | Meaning |
| --- | --- |
| Agent, agentic | An AI tool that plans and carries out steps, uses other tools, or acts without a person approving each action |
| Allowlist | A list of the only things a tool may do or reach; everything else is blocked |
| BAA | Business associate agreement: the contract US health-care organizations need before a vendor handles health data |
| Ceiling | A limit an organization sets in advance, stricter than the default, such as "no Confidential data without an exception". Crossing it makes the use case Severe. Level 2 organizations set ceilings in their profile. Level 1 has none of its own: the defaults never change a Level 1 tier |
| Connector | A link that lets an AI tool read or act in another system, such as email, a CRM or file storage |
| Control | A safeguard that reduces a risk, such as single sign-on, a retention setting or a review step. The control catalog is in `data/controls.yaml` |
| Dominant surface | The surface (Data, People or Capability) holding a use case's highest rating. It tells you where to look first to lower the rating |
| DPA | Data processing agreement: the contract that says what a vendor may do with your data |
| Exception | Written, time-limited permission to use a tool or information the policy would not otherwise allow |
| Exfiltration path | A way for a tool to put content where an outsider can see it: replying, emailing out, posting, fetching a link, or loading a remote image (the image's web address can carry data out). The worksheet calls it "the way out" |
| Function | Something an AI tool does, such as "LLM prompt processing" or "automated messaging". Functions decide which controls a tool needs; the library is in `data/functions.yaml`. The inventory's Function column is different: it is the rating for question 7, the most the tool is allowed to do |
| Impact assessment | A short record of who could be harmed if an AI tool is wrong, how badly, and what reduces the harm |
| Lethal trifecta | Sensitive data, untrusted input and an exfiltration path in one tool. Rated Severe unless a setting or control you can point to breaks one leg |
| MCP | Model Context Protocol: a common way to connect AI tools to other software and data |
| Organization profile | At Level 2, the file that records who decides at each tier, decision targets, ceilings and which triggers apply (`kit/profile.yaml`) |
| Owner | At Level 1, the person who decides whether a tool is allowed and on what terms. At Level 2 the work splits: the program owner runs the program, and each use case has a business owner, accountable for it, and a technical owner, who runs it |
| Prompt injection | Instructions hidden in content an AI tool reads, which the tool then follows |
| Provisional | A rating that rests on an answer nobody has confirmed yet |
| Residency | Where a vendor stores and processes your data, by country or region |
| Retention | How long a vendor keeps what you send it |
| STRIDE | Six kinds of threat used to check an agent design: spoofing, tampering, repudiation, information disclosure, denial of service and elevation of privilege |
| Subprocessor | Another company a vendor passes your data to, such as the AI model provider behind a tool |
| Tenant | Your organization's own workspace in a vendor's service. "Our own tenant" in the worksheet means one where your admin controls retention and the vendor does not train on your content |
| Tier | A use case's overall rating: the worst of its question ratings, or Severe when the trifecta or a ceiling applies |
| Trigger | A fact that adds a document to your kit, such as "AI output reaches clients" adding disclosure language |
| Untrusted input | Content nobody in your organization wrote or checked, such as web pages, inbound email or outside files. The worksheet and inventory call it "outside content" |
| Use case | One tool used for one purpose. The same tool used two ways is two use cases |

<!-- licence-footer -->

---

*Handrail by [Keith Crawford](https://keithcrawford.me). Licensed [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). If you adapt this page, keep this line and say what you changed.*
