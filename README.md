# Handrail

**Guardrails stop you. A handrail helps you climb.**

Handrail is an open kit for deciding which AI tools your organization can use, on what terms, and who decides. A five-person firm starts with a one-page policy and an afternoon of work; a software company climbs to named owners, assessment records and, when it is ready, an ISO/IEC 42001 program. The steps are the same; what changes is how much you write down.

At its core is the **Three Surfaces** model. Every use of AI touches three surfaces: the **data** it handles, the **people** who see and rely on what it produces, and the **capability** it has to act on its own. Rate each Low, Medium, High or Severe. The worst rating decides.

## Start here

| If you are | Start with | You end up with |
| --- | --- | --- |
| New to this | [The 101](docs/101.md) | Ten minutes, the whole idea |
| A small team that buys AI tools | [Level 1](docs/level-1.md) | A one-page policy, a rated list of your AI tools, a vendor terms check and an incident card |
| A growing company, or customers are asking | [Level 2](docs/level-2.md) | Named owners, an intake form, an assessment record per tool, a register, a review calendar |
| Preparing for an ISO/IEC 42001 audit | [What Level 2 evidences](docs/what-level-2-evidences.md) | An honest map of what Level 2 covers and what Level 3 adds (Level 3 is planned) |
| Mapping AI controls to SOC 2, ISO/IEC 42001, NIST or the EU AI Act | [Master crosswalk](docs/crosswalk.md) ([spreadsheet](kit/crosswalk.xlsx)) | Every control with its framework references; the spreadsheet covers eight frameworks and filters by any of them |

No software is required. Every template is a Markdown file or a spreadsheet; the inventory and register spreadsheets have drop-down lists and work out tiers for you. An optional skill plugin for Claude helps you score tools and draft documents.

## What is in the repository

| Folder | Holds |
| --- | --- |
| `docs/` | Everything to read: the 101, the Level 1 and Level 2 walkthroughs, the reasoning behind the model, single-task guides, the master crosswalk, a glossary and references |
| `kit/` | Everything to copy: templates and spreadsheets. Each has sections marked Level 1, Level 2 or Level 3; fill the sections for your level |
| `examples/` | Two fictional organizations, filled in: a consulting practice at Level 1 and a SaaS company at Level 2 |
| `data/` | The model, the function and control catalog, and framework crosswalks, as YAML |
| `plugin/` | The optional Claude skill plugin: an assessor and an advisor |
| `tools/` | `check`, which validates the data, templates and example records |

## The model in one table

| Surface | Question | Riskier when |
| --- | --- | --- |
| Data | What does it touch, and what happens to it? | Client or customer information goes in; the vendor keeps it or trains on it; your contract doesn't cover it |
| People | Who sees the output before you review it, how much do they trust it, who is hurt if it is wrong? | It reaches clients or the public; people act on it without checking; a mistake affects someone's money, job or a client's business |
| Capability | What can it do on its own? | It sends, changes or deletes things; it reads content from outside; it acts without a person approving |

The full model, with every rubric, is [data/model.yaml](data/model.yaml).

## Using the data

The YAML in `data/` is the single definition of the model and the control catalog. Templates, the skill plugin and the examples are checked against it. To adapt the model, edit the YAML and run:

```bash
python tools/check
```

`check` needs Python 3.10 or later and PyYAML; it is tested on Python 3.13 and 3.14, and runs on every push.

## Credits and licences

| Path | Licence |
| --- | --- |
| `README.md`, `CHANGELOG.md`, `SECURITY.md`, `docs/`, `docs/`, `kit/`, `docs/`, `examples/` (except the rows below) | [CC-BY-4.0](LICENSE) |
| `data/`, `plugin/`, `tools/`, `.github/` | [Apache-2.0](LICENSE-code) |
| `kit/assessment-record.md`, `kit/intake-form.md` (modified from the workbook's skill and intake form) | [Apache-2.0](LICENSE-code) |
| `examples/expected-tiers.yaml` (a test fixture `tools/check` reads) | [Apache-2.0](LICENSE-code) |
| `kit/crosswalk.xlsx`, `docs/crosswalk.md` (generated from `data/`) | [Apache-2.0](LICENSE-code) |
| Copies in `plugin/skills/*/data/` | The licence of the file they copy (for example, `inventory.csv` stays CC-BY-4.0), with the Apache-2.0 parts named in the next row |
| Rubric level wording (inside `<!-- rubric -->` blocks), the default routing roles, and the control and function names in the example records, wherever they appear | [Apache-2.0](LICENSE-code), from the workbook via `data/` (see NOTICE) |

Every CC-BY page ends with a credit line; keep it when you copy a page, and say what you changed.

The function and control catalog in `data/` is modified from the [AI Security Risk Workbook v3.0](https://github.com/jasonmichaelrobbins-arch/-ai-security-governance-workbook) by Jason Robbins (Apache-2.0). Identifiers such as POS-01 and NHI-07 are his workbook's identifiers, kept for traceability; they are not a published standard. Handrail is not endorsed by or affiliated with him.

ISO/IEC 42001 and 42005, the CSA AI Controls Matrix, CSA MAESTRO, SOC 2 and OWASP are cited by identifier, not reproduced. See [NOTICE](NOTICE).

Handrail is written by [Keith Crawford](https://keithcrawford.me). It is guidance, not legal advice, and using it does not make an organization compliant with any standard or law.

<!-- licence-footer -->

---

*Handrail by [Keith Crawford](https://keithcrawford.me). Licensed [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). If you adapt this page, keep this line and say what you changed.*
