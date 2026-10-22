# Roles and responsibilities (Level 2)

*Template. Replace the example roles with yours. Small organizations can hold several roles in one person; what matters is that each line has a name.*

| Activity | Program owner | Security | Legal or privacy | Business owner of the use case | Department lead | Business unit head | Committee | Executive sponsor |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Keep the AI policy current | **A** | C | C | I | I | I | C | I |
| Keep the organization profile current, including tighter ceilings | **A**, R | C | C | I | I | I | C | I |
| Keep the AI register current | **A**, R | C | I | C | I | I | I | I |
| Receive intake requests | **A**, R | I | I | C | I | I | I | I |
| Assess a use case (assessment record) | C | **A**, R | C | C | I | I | I | I |
| Run an impact assessment | C | C | **A**, R | C | I | I | I | I |
| Decide a Low use case | I | **A** | I | C | I | I | I | I |
| Decide a Medium use case | I | R (security review) | I | C | **A** | I | I | I |
| Decide a High use case | I | C | C | C | I | C | **A** | I |
| Grant a Severe exception | I | C | C | C | I | C | R | **A** |
| Accept remaining risk: Low and Medium | I | I | I | **A** | I | I | I | I |
| Accept remaining risk: High | I | I | I | C | I | **A** | I | I |
| Accept remaining risk: Severe | I | I | I | C | I | C | I | **A** |
| Verify controls after go-live | I | **A**, R | I | I | I | I | I | I |
| Respond to an AI incident | C | **A**, R | R | C | I | I | I | I |
| Disable a tool in an emergency | I | **A** (on call) | I | I | I | I | I | I |

The tier routing in the [policy](policy.md) and your [profile](profile.yaml) must match this table: Low decided by security, Medium by the department lead with security review, High by the committee, Severe only by exception.

**A** accountable (one per row) · **R** does the work · **C** consulted · **I** informed

**Named people**

| Role | Name | Backup |
| --- | --- | --- |
| Program owner | | |
| Security reviewer | | |
| Legal or privacy | | |
| Department leads (Medium decisions) | | |
| Business unit heads (High risk acceptance) | | |
| Committee chair | | |
| Executive sponsor | | |
| Who can disable a tool immediately | | |

<!-- licence-footer -->

---

*Handrail by [Keith Crawford](https://keithcrawford.me). Licensed [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). If you adapt this page, keep this line and say what you changed.*
