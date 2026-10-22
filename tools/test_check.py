# Copyright 2026 Keith Crawford. Licensed under the Apache License, Version 2.0.
"""Seeded-fault tests for tools/check.

Usage: python tools/test_check.py

Copies the repository to a temporary folder once per fault, plants one fault,
runs tools/check, and confirms it fails with the expected error code. Also
confirms the unmodified copy passes. Needs PyYAML.
"""
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CHECK = ROOT / "tools" / "check"
RUBRIC_GOOD = None


def run(repo, extra=()):
    p = subprocess.run([sys.executable, str(repo / "tools" / "check"), str(repo), *extra], capture_output=True, text=True)
    return p.returncode, p.stdout


def copy():
    tmp = Path(tempfile.mkdtemp(prefix="ts-check-"))
    dst = tmp / "repo"
    shutil.copytree(ROOT, dst, ignore=shutil.ignore_patterns(".git", "__pycache__"))
    return tmp, dst


def edit(path, old, new):
    text = path.read_text(encoding="utf-8")
    assert old in text, f"fixture text not found in {path.name}: {old[:40]!r}"
    path.write_text(text.replace(old, new, 1), encoding="utf-8", newline="\n")


def first_record(repo):
    recs = sorted(repo.glob("examples/**/*.record.md"))
    assert recs, "no example records to seed"
    return recs[0]


def fault_model(repo):
    edit(repo / "data/model.yaml", "          low: Public information only.", "          minimal: Public information only.")


def fault_catalog(repo):
    edit(repo / "data/functions.yaml", "- OBS-01", "- OBS-99", )


def fault_provenance(repo):
    edit(repo / "data/controls.yaml", "- id: POS-08", "- id: POS-88")
    for p in repo.glob("data/crosswalks/*.yaml"):
        t = p.read_text(encoding="utf-8").replace("  POS-08:", "  POS-88:")
        p.write_text(t, encoding="utf-8", newline="\n")
    for p in [repo / "data/functions.yaml"]:
        t = p.read_text(encoding="utf-8").replace("- POS-08", "- POS-88")
        p.write_text(t, encoding="utf-8", newline="\n")


def fault_crosswalk(repo):
    edit(repo / "data/crosswalks/csa-aicm.yaml", "  - GRC-05\n", "  - GRC-05 SEEDED-FAULT\n")


def fault_plugin(repo):
    p = repo / "plugin/skills/handrail-assessor/data/model.yaml"
    p.write_text(p.read_text(encoding="utf-8") + "\n# drift\n", encoding="utf-8", newline="\n")


def fault_template(repo):
    p = repo / "kit" / "zz-seeded.md"
    p.write_text("<!-- rubric: data.sensitivity -->\n- **Low:** Public information only.\n- **Medium:** Anything at all.\n"
                 "- **High:** x\n- **Severe:** y\n<!-- /rubric -->\n", encoding="utf-8", newline="\n")


def fault_record_tier(repo):
    p = first_record(repo)
    t = p.read_text(encoding="utf-8")
    import re
    t = re.sub(r"(?m)^tier: \w+$", "tier: Low", t, count=1)
    p.write_text(t, encoding="utf-8", newline="\n")


def fault_record_gap(repo):
    p = first_record(repo)
    import re
    t = p.read_text(encoding="utf-8")
    t, n = re.subn(r"(?m)^(- id: (\w+-\d+)\n  owner: \w+\n  status: )Identified", r"\1Gap", t, count=1)
    assert n == 1, "no Identified control to flip"
    p.write_text(t, encoding="utf-8", newline="\n")


def fault_record_controls(repo):
    p = first_record(repo)
    import re
    t = p.read_text(encoding="utf-8")
    t, n = re.subn(r"(?m)^- id: POS-01\n  owner: \w+\n  status: \w+\n  control: [^\n]*\n", "", t, count=1)
    assert n == 1, "POS-01 line not found"
    p.write_text(t, encoding="utf-8", newline="\n")


def fault_expected(repo):
    p = repo / "examples/expected-tiers.yaml"
    import re
    t = p.read_text(encoding="utf-8")
    t = re.sub(r"(?m)^(  [\w-]+: )(Low|Medium|High|Severe)$", lambda m: m.group(1) + ("Severe" if m.group(2) != "Severe" else "Low"), t, count=1)
    p.write_text(t, encoding="utf-8", newline="\n")


def fault_record_yaml(repo):
    p = first_record(repo)
    t = p.read_text(encoding="utf-8")
    p.write_text(t.replace("\n", "\nbroken: [unclosed\n", 1), encoding="utf-8", newline="\n")


def fault_pin(repo):
    import re
    p = repo / "plugin/skills/handrail-assessor/SKILL.md"
    t, n = re.subn(r"(?m)^(  model_sha256: ).*$", r"\g<1>" + "0" * 64, p.read_text(encoding="utf-8"), count=1)
    assert n == 1, "no model_sha256 pin"
    p.write_text(t, encoding="utf-8", newline="\n")


def fault_flags(repo):
    p = first_record(repo)
    t = p.read_text(encoding="utf-8")
    if "impact_assessment_required: false" in t:
        edit(p, "impact_assessment_required: false", "impact_assessment_required: true")
    else:
        edit(p, "impact_assessment_required: true", "impact_assessment_required: false")


def fault_third_party(repo):
    edit(repo / "examples/saas-company/support-assistant.record.md", "third_party_model: true", "third_party_model: false")


def fault_followup(repo):
    import csv
    p = repo / "examples/consulting-practice/inventory.csv"
    with open(p, newline="", encoding="utf-8") as f:
        rows = list(csv.reader(f))
    head = rows[0]
    row = next(r for r in rows[1:] if r[head.index("Tier")] == "High")
    row[head.index("Disclosure")] = "Severe"
    with open(p, "w", newline="", encoding="utf-8") as f:
        csv.writer(f).writerows(rows)


def fault_user_records(repo):
    import re
    own = repo.parent / "my-records"
    own.mkdir()
    t = first_record(repo).read_text(encoding="utf-8")
    (own / "mine.record.md").write_text(re.sub(r"(?m)^tier: \w+$", "tier: Low", t, count=1), encoding="utf-8", newline="\n")
    return ["--records", str(own)]


def fault_trifecta_off(repo):
    import re
    p = repo / "examples/saas-company/sales-notetaker.record.md"
    t = p.read_text(encoding="utf-8")
    t, n = re.subn(r"(?m)^  applies: true$", "  applies: false", t, count=1)
    assert n == 1, "no applies: true"
    p.write_text(t, encoding="utf-8", newline="\n")


def fault_trifecta_tier(repo):
    import re
    p = repo / "examples/saas-company/sales-notetaker.record.md"
    t = p.read_text(encoding="utf-8")
    t, n = re.subn(r"(?m)^tier: Severe$", "tier: High", t, count=1)
    assert n == 1, "no tier: Severe"
    t = t.replace("people.audience: High", "people.audience: Medium").replace("people.disclosure: High", "people.disclosure: Medium")
    t = re.sub(r"(?m)^(  capability\.\w+: )(High|Severe)$", r"\1Medium", t)
    t = re.sub(r"(?m)^(  data\.persistence: )High$", r"\1Medium", t)
    p.write_text(t, encoding="utf-8", newline="\n")


def fault_kind(repo):
    import re
    p = first_record(repo)
    t, n = re.subn(r"(?m)^kind: .*$", "kind: bought it", p.read_text(encoding="utf-8"), count=1)
    assert n == 1
    p.write_text(t, encoding="utf-8", newline="\n")


def fault_profile(repo):
    edit(repo / "examples/saas-company/profile.yaml", "triggers: [BUILD, HIGH, AGENT, PEOPLE, REG]", "triggers: [BUILD, HIGH, AGENT, PEOPLE, REG, MAGIC]")


def fault_no_confirmation(repo):
    edit(repo / "examples/saas-company/support-assistant.record.md", "question: trifecta", "question: something else")


def fault_understated(repo):
    edit(repo / "examples/saas-company/support-assistant.record.md", "  data.sensitivity: High", "  data.sensitivity: Medium")


def fault_ceiling(repo):
    edit(repo / "examples/saas-company/profile.yaml", "  data_class: confidential", "  data_class: internal")


def fault_user_inventory(repo):
    import csv
    own = repo.parent / "my-inventory"
    own.mkdir()
    with open(repo / "examples/consulting-practice/inventory.csv", newline="", encoding="utf-8") as f:
        rows = list(csv.reader(f))
    rows[1][rows[0].index("Tier")] = "Low"
    with open(own / "inventory.csv", "w", newline="", encoding="utf-8") as f:
        csv.writer(f).writerows(rows)
    return ["--records", str(own)]


def fault_architecture(repo):
    edit(repo / "examples/saas-company/coding-assistant.record.md", "architecture: human_facing_llm", "architecture: chatbot")


def fault_route_gap(repo):
    import re
    p = repo / "examples/saas-company/prior-auth-drafting.record.md"
    t, n = re.subn(r"(?m)^(- id: DAT-08\n  owner: \w+\n  status: )Identified", r"\1Gap", p.read_text(encoding="utf-8"), count=1)
    assert n == 1, "DAT-08 not found"
    p.write_text(t, encoding="utf-8", newline="\n")


def fault_route_path(repo):
    edit(repo / "examples/saas-company/prior-auth-drafting.record.md", "designed_path: phi", "designed_path: pci")


def fault_untrusted_low(repo):
    edit(repo / "examples/saas-company/support-assistant.record.md", "  capability.untrusted_input: High", "  capability.untrusted_input: Low")


def fault_borrowed_profile(repo):
    own = repo.parent / "my-path-records"
    own.mkdir()
    src = repo / "examples/saas-company/prior-auth-drafting.record.md"
    (own / "mine.record.md").write_text(src.read_text(encoding="utf-8").replace("record_id: SAAS-04", "record_id: MINE-01"),
                                        encoding="utf-8", newline="\n")
    return ["--records", str(own)]


def fault_self_confirmed(repo):
    edit(repo / "examples/saas-company/prior-auth-drafting.record.md", "by: Privacy officer", "by: VP Product")


def fault_dot_prefix_profile(repo):
    extra = fault_borrowed_profile(repo)
    f = repo.parent / "my-path-records" / "mine.record.md"
    f.write_text(f.read_text(encoding="utf-8").replace("profile: examples/saas-company/profile.yaml",
                                                       "profile: ./examples/saas-company/profile.yaml"), encoding="utf-8", newline="\n")
    return extra


def fault_no_requester(repo):
    import re
    p = repo / "examples/saas-company/prior-auth-drafting.record.md"
    t, n = re.subn(r"(?m)^requester: .*\n", "", p.read_text(encoding="utf-8"), count=1)
    assert n == 1
    p.write_text(t, encoding="utf-8", newline="\n")


def fault_requester_as_confirmer(repo):
    edit(repo / "examples/saas-company/prior-auth-drafting.record.md", "requester: VP Product", "requester: Privacy officer, healthcare line")


def fault_link(repo):
    p = repo / "README.md"
    p.write_text(p.read_text(encoding="utf-8") + "\n[broken](docs/does-not-exist.md)\n", encoding="utf-8", newline="\n")


FAULTS = [
    ("E-MODEL", fault_model),
    ("E-CATALOG", fault_catalog),
    ("E-ID-PROVENANCE", fault_provenance),
    ("E-CROSSWALK", fault_crosswalk),
    ("E-PLUGIN-COPY", fault_plugin),
    ("E-TEMPLATE", fault_template),
    ("E-RECORD-TIER", fault_record_tier),
    ("E-RECORD-TIER", fault_record_yaml),
    ("E-RECORD-GAP", fault_record_gap),
    ("E-RECORD-FLAGS", fault_flags),
    ("E-RECORD-CONTROLS", fault_third_party),
    ("E-RECORD-TIER", fault_followup),
    ("E-RECORD-TIER", fault_user_records),
    ("E-PLUGIN-COPY", fault_pin),
    ("E-RECORD-TIER", fault_trifecta_off),
    ("E-RECORD-TIER", fault_trifecta_tier),
    ("E-RECORD-CONTROLS", fault_kind),
    ("E-PROFILE", fault_profile),
    ("E-RECORD-TIER", fault_no_confirmation),
    ("E-RECORD-TIER", fault_understated),
    ("E-RECORD-TIER", fault_ceiling),
    ("E-RECORD-TIER", fault_user_inventory),
    ("E-RECORD-FLAGS", fault_architecture),
    ("E-RECORD-ROUTE", fault_route_gap),
    ("E-RECORD-ROUTE", fault_route_path),
    ("E-RECORD-TIER", fault_untrusted_low),
    ("E-RECORD-ROUTE", fault_borrowed_profile),
    ("E-RECORD-TIER", fault_self_confirmed),
    ("E-RECORD-ROUTE", fault_dot_prefix_profile),
    ("E-RECORD-ROUTE", fault_no_requester),
    ("E-RECORD-TIER", fault_requester_as_confirmer),
    ("E-RECORD-CONTROLS", fault_record_controls),
    ("E-EXPECTED", fault_expected),
    ("E-LINK", fault_link),
]


def main():
    failures = 0
    tmp, repo = copy()
    code, out = run(repo)
    shutil.rmtree(tmp, ignore_errors=True)
    if code != 0:
        print("FAIL baseline: the unmodified repository does not pass\n" + out)
        return 1
    print("ok   baseline passes")
    for expected, plant in FAULTS:
        tmp, repo = copy()
        try:
            extra = plant(repo) or []
            code, out = run(repo, extra)
            hit = code != 0 and any(line.startswith(expected + " ") for line in out.splitlines())
            print(("ok   " if hit else "FAIL ") + f"{expected:<18} {'caught' if hit else 'not caught'}")
            if not hit:
                failures += 1
                print(out)
        finally:
            shutil.rmtree(tmp, ignore_errors=True)
    print("all seeded faults caught" if not failures else f"{failures} seeded fault(s) not caught")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
