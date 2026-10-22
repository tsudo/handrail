# Handrail skill plugin

Two optional skills for Claude Code, Codex and Claude.ai. Nothing in the kit needs them: every template works on its own.

| Skill | Modes | Use it to |
| --- | --- | --- |
| `handrail-assessor` | `quick`, `assess` | Score one AI tool or use case and draft its inventory row (Level 1) or assessment record (Level 2) |
| `handrail-advisor` | `onboard`, `draft` | Pick your level, write your organization profile, and draft your policy and other documents |

## Install

**Claude Code or Codex:** install this folder as a plugin, or copy a skill folder from `skills/` into your skills directory. Each skill carries its own copy of the data it reads in its `data/` folder (the model; for the assessor also the catalog, the record template, the inventory columns, the ATLAS and OWASP lists; for the advisor the profile template), and the advisor carries outlines of every document it drafts, so a single skill works on its own. With the repository at hand, the advisor follows the fuller templates in `kit/`.

**Claude.ai:** zip one skill folder (for example `skills/handrail-assessor/`) and upload it as a skill. Each `SKILL.md` pins the version and SHA-256 of the model it shipped with; where the skill cannot compute the hash itself, the record gives the pin followed by "unverified". The pin catches copies that have drifted; it is not tamper protection.

## What the skills will and won't do

Both skills:

- draft and score; a named person in your organization decides;
- treat vendor pages, pasted documents and tickets as data, never as instructions, and record any text that tries to instruct them;
- never ask you to paste client or customer personal data;
- read files and the web only, and write nothing to disk unless you ask for a file and say where;
- stop with a named error if their data is missing, or does not match the pinned model version;
- do not give legal advice or tell you that you are compliant.

The assessor also refuses to let a statement with nothing behind it ("assume no untrusted input") break the lethal trifecta, and never lets a marketing page or a pasted document lower a rating.

## Keeping the data in step

The files in each skill's `data/` folder are copies of the repository's `data/`. After editing the model, the catalog or a bundled kit file, copy them again and update the pinned hash in each `SKILL.md`, then run `python tools/check`, which fails if any copy or pin is stale.

## Licence

Apache-2.0 (see `LICENSE` and `NOTICE`). The function and control catalog, and the structure of the assessor's ground rules and record, are modified from the AI Security Risk Workbook v3.0 by Jason Robbins (Apache-2.0). He does not endorse this plugin.
