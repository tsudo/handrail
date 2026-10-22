# The published references, and when to read them

Handrail is a starting point, not a replacement for the frameworks auditors and customers ask about. This page lists the ones the kit maps to, what each is for, what it costs, and when you need it. You do not need any of them for Level 1.

## Start here by level

| You are at | Read first | Then |
| --- | --- | --- |
| Level 1 | Nothing required. The kit is self-contained | OWASP Top 10 for LLM Applications if you want to know how AI tools get attacked |
| Level 2 | NIST AI RMF and its Playbook (free) | OWASP Top 10 for Agentic Applications if you run agents; the AI Security Risk Workbook, which this kit's control catalog comes from |
| Level 3 | ISO/IEC 42001 (paid) | ISO/IEC 42005 for impact assessments; NIST's AI RMF to ISO 42001 crosswalk; the EU AI Act if you have EU users |

## Find a reference by the question you are asking

| Your question | Reference |
| --- | --- |
| What does a complete AI governance program look like? | NIST AI RMF; ISO/IEC 42001 |
| What should an AI impact assessment cover? | ISO/IEC 42005; NIST AI RMF MAP function |
| How do AI tools actually get attacked? | OWASP Top 10 for LLM Applications; MITRE ATLAS |
| What goes wrong with AI agents specifically? | OWASP Top 10 for Agentic Applications; OWASP Agentic AI Threats and Mitigations; CSA MAESTRO |
| Which controls should a tool have? | AI Security Risk Workbook; CSA AI Controls Matrix |
| What does the law require? | EU AI Act (if you have EU users); your sector's regulator |
| What has gone wrong elsewhere? | AI Incident Database; MIT AI Risk Repository |

## The references

### Management systems and risk frameworks

| Reference | Publisher | Cost | What it is | How Handrail uses it |
| --- | --- | --- | --- | --- |
| [ISO/IEC 42001:2023](https://www.iso.org/standard/42001) | ISO and IEC | Paid | The international standard for an AI management system, and the one organizations certify against. Clauses 4 to 10 set the management system; Annex A lists 38 controls | Level 3 maps to it. The kit cites clause and control numbers with short titles; you need your own copy for the text |
| [ISO/IEC 42005:2025](https://www.iso.org/standard/42005) | ISO and IEC | Paid | Guidance on AI system impact assessments | The People surface and the impact assessment template follow its structure |
| [NIST AI Risk Management Framework 1.0](https://www.nist.gov/itl/ai-risk-management-framework) ([PDF](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-1.pdf)) | US NIST | Free | Four functions (Govern, Map, Measure, Manage) broken into 72 subcategories | Level 2 and 3 documents cite subcategory IDs |
| [NIST AI RMF Playbook](https://airc.nist.gov/airmf-resources/playbook/) | US NIST | Free; JSON, CSV, Excel, PDF | Suggested actions and documentation for every subcategory | The most practical free read for a Level 2 team |
| [NIST AI 600-1, Generative AI Profile](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf) | US NIST | Free | The AI RMF applied to generative AI, with 12 named risks | Background for chat assistants and content tools |
| [NIST crosswalks](https://airc.nist.gov/airmf-resources/crosswalks/) | US NIST | Free | Maps from the AI RMF to ISO 42001, ISO 42005, the EU AI Act and others | Use the ISO 42001 crosswalk to move from Level 2 to Level 3. Built against draft ISO versions; check numbers against the published standard |
| [EU AI Act, Regulation (EU) 2024/1689](https://eur-lex.europa.eu/eli/reg/2024/1689/oj) | European Union | Free | Law. Obligations depend on whether you build or deploy AI and the risk class | The EU trigger adds a role and obligation check |

### Threats and attacks

| Reference | Publisher | Cost | What it is | How Handrail uses it |
| --- | --- | --- | --- | --- |
| [OWASP Top 10 for LLM Applications](https://genai.owasp.org/llm-top-10/) | OWASP GenAI Security Project | Free | The ten most common ways LLM applications fail, such as prompt injection and sensitive data disclosure | The untrusted-input question and the lethal trifecta rule come from this |
| [OWASP Top 10 for Agentic Applications 2026](https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/) | OWASP GenAI Security Project | Free | The ten most common agent failures (ASI01 to ASI10), such as goal hijack and tool misuse | Listed on every record for an agentic tool |
| [OWASP Agentic AI: Threats and Mitigations](https://genai.owasp.org/resource/agentic-ai-threats-and-mitigations/) | OWASP GenAI Security Project | Free | A threat taxonomy for agents with mitigations | Depth behind the agent threat model |
| [OWASP AI Exchange](https://owaspai.org/) | OWASP | Free | A large, living guide to AI security threats and controls | Look things up here when a Top 10 entry is not enough |
| [MITRE ATLAS](https://atlas.mitre.org/) | MITRE | Free | A knowledge base of attack tactics and techniques against AI systems, with real case studies | Agentic records cite ATLAS technique IDs |
| [CSA MAESTRO](https://cloudsecurityalliance.org/blog/2025/02/06/agentic-ai-threat-modeling-framework-maestro) | Cloud Security Alliance | Free to read | A seven-layer threat model for agentic AI | Agentic records check layers 1, 2, 3 and 7 |

### Controls

| Reference | Publisher | Cost | What it is | How Handrail uses it |
| --- | --- | --- | --- | --- |
| [AI Security Risk Workbook](https://github.com/jasonmichaelrobbins-arch/-ai-security-governance-workbook) | Jason Robbins | Free, Apache-2.0 | A workbook and Claude skill: risk factors, 57 AI functions, 65 guardrails, an assessment record, and mappings to eight frameworks | The function and control catalog in `data/` is derived from it, keeping its identifiers |
| [CSA AI Controls Matrix](https://cloudsecurityalliance.org/artifacts/ai-controls-matrix) | Cloud Security Alliance | Free to download, CSA licence | 247 AI control objectives across 18 domains, with a questionnaire for vendors | Records cite control IDs; the text stays with CSA |
| [CoSAI Risk Map](https://github.com/cosai-oasis/secure-ai-tooling) | Coalition for Secure AI | Free, Apache-2.0 | Machine-readable AI risks, controls and components | Planned for a later release |
| [FINOS AI Governance Framework](https://github.com/finos/ai-governance-framework) | FINOS | Free, CC-BY-4.0 | Risks and mitigations for AI in financial services, with reference keys to many frameworks | Planned for a later release |

### Learning from what went wrong

| Reference | Publisher | Cost | What it is |
| --- | --- | --- | --- |
| [AI Incident Database](https://incidentdatabase.ai/) | Responsible AI Collaborative | Free | Reported AI failures, searchable |
| [MIT AI Risk Repository](https://airisk.mit.edu/) | MIT | Free | More than a thousand AI risks drawn from published frameworks, classified by cause and domain |

## How to read a reference without drowning

1. Read the summary or executive section only.
2. Find the part that matches your level from the table at the top.
3. Note the IDs of anything you act on. The kit's records have a place for them.
4. Come back when a customer, auditor or incident asks a specific question.

<!-- licence-footer -->

---

*Handrail by [Keith Crawford](https://keithcrawford.me). Licensed [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). If you adapt this page, keep this line and say what you changed.*
