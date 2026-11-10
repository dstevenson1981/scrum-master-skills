# Agile36 Scrum Master Skill Library

30 skills for the jobs a Scrum Master does every sprint, plus 4 optional ones. Every Scrum event has its own skill. Each one is pinned to the exact version Agile36 reviewed.

## Scrum events

| Skill | Job | Level | Needs |
|---|---|---|---|
| **sprint-plan** | Sprint Planning: goal, real capacity, commit vs stretch, dependencies, risks, Definition of Done | Beginner | Nothing (optional plan audit needs Python 3) |
| **daily-scrum** | Daily Scrum: formats, keeping it to 15 minutes, a quick Sprint Goal check | Beginner | Nothing |
| **sprint-review** | Sprint Review: agenda, showing the Increment, getting real stakeholder feedback | Beginner | Nothing |
| **scrum-retrospective** | Sprint Retrospective: pick a format, facilitate it, make actions stick | Beginner | Nothing |
| **backlog-refinement** | Backlog Refinement: INVEST checks, vertical splits, Definition of Ready | Beginner | Nothing (optional scorer needs Python 3) |
| **scrum-of-scrums** | Scrum of Scrums: coordinate 2-5 teams on one product | Beginner | Nothing |
| **sprint-retrospective** | Retro data pack from git history: velocity, cycle time, churn hotspots | Intermediate | Python 3 + a git repository |

## Role and coaching

| Skill | Job | Level | Needs |
|---|---|---|---|
| **scrum-role-coach** | The Scrum Master role: stances, servant leadership, anti-patterns, onboarding, health check | Beginner | Nothing |
| **agile-coach** | Agile coaching: framework choice, maturity assessment, transformation roadmap | Intermediate | Nothing (optional scorers need Python 3) |
| **problem-solver** | Diagnose a recurring problem before fixing it: problem statement, verified root causes | Intermediate | A project folder (keeps notes) |
| **scrum-workflow** | Scrum Master of record: runs a team's sprints with memory across sessions | Advanced | A project folder (keeps notes in _project/scrum-master/) |

## Risks and impediments

| Skill | Job | Level | Needs |
|---|---|---|---|
| **impediment-log** | Log, triage and escalate a blocker; draft the escalation message | Beginner | Nothing |
| **pre-mortem** | Pre-mortem: imagine the launch failed, surface risks, give each an owner | Beginner | Nothing (optional sorter needs Python 3) |
| **post-mortem** | Blameless review after an incident, missed launch or failed sprint | Beginner | Nothing |
| **dependency-map** | Cross-team dependencies: risk-ranked blocker list and a graph | Intermediate | Nothing (optional graph tool needs Python 3) |
| **project-manager** | Project risk register (RAID), plans, scope changes, status for delivery | Advanced | A project folder (keeps notes in _project/) |

## Backlog and estimation

| Skill | Job | Level | Needs |
|---|---|---|---|
| **planning-poker** | Estimation: planning poker, story points, t-shirt sizing, when not to estimate | Beginner | Nothing |
| **story-splitting** | Split oversized stories into thin vertical slices | Beginner | Nothing |
| **story-mapping** | User story map: journey, ranked tasks, release lines for an MVP | Beginner | Nothing |
| **agile-product-owner** | Write user stories and acceptance criteria, break down epics | Intermediate | Nothing (optional story generator needs Python 3) |
| **prioritization-frameworks** | Rank a backlog with RICE, ICE, MoSCoW or weighted scoring | Intermediate | Nothing (optional scorer needs Python 3) |

## Metrics and forecasting

| Skill | Job | Level | Needs |
|---|---|---|---|
| **scrum-analytics** | Velocity forecasts (Monte Carlo), sprint health score, retro action tracking | Intermediate | Python 3 + sprint data as JSON (sample included) |
| **cycle-time-analyzer** | Flow metrics: lead time, cycle time, throughput, WIP aging, cumulative flow | Intermediate | Python 3 + an issue status export |
| **brainstorm-okrs** | Draft and score team OKRs with a counter-metric | Beginner | Nothing (optional validator needs Python 3) |

## Stakeholders and communication

| Skill | Job | Level | Needs |
|---|---|---|---|
| **stakeholder-map** | Map stakeholders by power, interest and stance; plan engagement | Beginner | Nothing (optional analyzer needs Python 3) |
| **status-update-generator** | Weekly executive status: highlights, blockers, risks, asks | Intermediate | Nothing (optional generator needs Python 3) |
| **team-communications** | Internal updates, newsletters, FAQs, incident and leadership notes | Beginner | Nothing |
| **summarize-meeting** | Turn notes or a transcript into decisions, owned action items, open questions | Beginner | Nothing |
| **daci-framework** | Decision roles (Driver, Approver, Contributor, Informed) for stalled decisions | Beginner | Nothing |

## Tools and scaling

| Skill | Job | Level | Needs |
|---|---|---|---|
| **jira-expert** | Jira boards, workflows, JQL, automation and dashboards; audit a messy board | Intermediate | Nothing (optional audit tools need Python 3 + a Jira export) |
| **program-manager** *(optional)* | Multi-team programs: charter, governance, cross-project dependencies, steering reports | Advanced | Nothing (optional tools need Python 3) |
| **quarterly-planning** *(optional)* | Quarter planning meetings: kickoff, weekly check-ins, mid-quarter carry/kill/pivot, close retro | Intermediate | Nothing (optional tools need Python 3) |

## Reference

| Skill | Job | Level | Needs |
|---|---|---|---|
| **agile-scrum-guide** *(optional)* | Background reading: roles, artifacts, events, stories, estimation, metrics | Beginner | Nothing |
| **skill-security-auditor** *(optional)* | Check any skill for prompt injection, dangerous code or data leaks before installing it | Intermediate | Python 3 |

**Which retro skill?** `scrum-retrospective` plans and facilitates the meeting. `sprint-retrospective` builds a data pack from git history to bring to it.

**Event skills vs. scrum-workflow:** the event skills prepare one meeting. `scrum-workflow` runs a team's sprints over time and remembers them between sessions.

---

## Install it

Nothing to download first. In a terminal:

```bash
curl -fsSL https://raw.githubusercontent.com/dstevenson1981/scrum-master-skills/main/tools/install_library.py | python3 -
```

That installs all core skills into Claude Code. Add options after `python3 -`:

| You use… | Add | Then |
|---|---|---|
| **Claude Code** | nothing | Start a new session. Skills load on their own |
| **Claude app** (claude.ai, desktop, mobile) | `--target zip` | Upload each zip: Settings > Capabilities > Skills |
| **GitHub Copilot** | `--target copilot` | Copy the `.github/` folder into your repo |
| **ChatGPT, Gemini, others** | `--target plain` | Paste a `.txt` file as your first message, or save it as a custom GPT / Gem instruction |

Other options: `--list`, `--category "Scrum events"`, `--only daily-scrum,sprint-review`, `--with-optional`, `--force` (update).

Working from a copy of this repo instead? Run `python3 tools/install_library.py` with the same options.

**Outside Claude Code**, skills marked *Nothing* under Needs work fully. Skills with Python tools still give advice without them; in the Claude app they can run their tools when code execution is on.

---

## Try each one

Use a made-up team. Never paste real names or company data into a class exercise.

| Skill | Try this |
|---|---|
| sprint-plan | "Plan Sprint 4: 2 weeks, 6 developers, one on leave Thursday and Friday. Our last three velocities were 21, 18 and 24." |
| daily-scrum | "Our daily standup has turned into a 40-minute status report to our manager. How do I fix it?" |
| sprint-review | "Plan a 60-minute Sprint Review. Two of five items are Done and our stakeholders usually skip it." |
| scrum-retrospective | "The same three complaints come up every retro and nothing changes. Plan our next retro." |
| backlog-refinement | "Refine this story: 'As an admin I want a reporting dashboard so I can see everything.'" |
| scrum-of-scrums | "We have 3 teams on one mobile app and they keep breaking each other's releases. How do I set up a Scrum of Scrums?" |
| sprint-retrospective | "(inside a git repo) Build a retro data pack for the last two weeks." |
| scrum-role-coach | "I'm joining a new team as Scrum Master next week. What should my first two weeks look like?" |
| agile-coach | "Our org runs 'Scrum' but nothing has changed in a year. Assess our maturity and suggest a 90-day coaching plan." |
| problem-solver | "Our team misses its Sprint Goal almost every sprint and nobody agrees why. Help me diagnose it." |
| scrum-workflow | "Adopt this team: 'Mobile Squad', 2-week sprints. Set up the workspace." |
| impediment-log | "We've been blocked 4 days waiting on the platform team for a staging environment. Log it and help me escalate." |
| pre-mortem | "We launch the new checkout in 3 weeks. Run a pre-mortem with me." |
| post-mortem | "Our release last Friday took the app down for 2 hours. Help me run a blameless post-mortem." |
| dependency-map | "Three teams depend on each other for the Q3 release. Map the dependencies and show the riskiest ones." |
| project-manager | "Set up a risk register for our payments migration and add the top five risks." |
| planning-poker | "One senior developer anchors every estimate. How should I run planning poker?" |
| story-splitting | "Split this story: 'Users can pay by card, PayPal or invoice, with refunds.'" |
| story-mapping | "Build a story map for a mobile app's first-time onboarding and draw the MVP line." |
| agile-product-owner | "Write user stories with acceptance criteria for 'customers can save a card for later'." |
| prioritization-frameworks | "Help our Product Owner rank these 8 items with RICE. Ask me for what you need." |
| scrum-analytics | "Run a velocity forecast on the sample sprint data and tell me what we can safely commit to next sprint." |
| cycle-time-analyzer | "Analyze the sample board data: where is work getting stuck?" |
| brainstorm-okrs | "Draft Q1 OKRs for a team whose main problem is slow releases." |
| stakeholder-map | "Map the stakeholders for our billing rollout. The finance director is skeptical." |
| status-update-generator | "Write this week's status update for our sponsor. We're yellow: one blocker, two risks." |
| team-communications | "Write a short update to leadership: we're moving from 3-week to 2-week sprints next month." |
| summarize-meeting | "Here are my notes from Sprint Planning. Summarize decisions and action items. [paste notes]" |
| daci-framework | "Nobody can decide whether we adopt Kanban for our support team. Set up a DACI for it." |
| jira-expert | "Write a JQL filter for everything in the current sprint that's been In Progress for more than 3 days." |
| program-manager | "We're starting a 4-team program to replace our billing system. Draft the charter and governance cadence." |
| quarterly-planning | "Plan the kickoff and weekly check-in rhythm for next quarter's OKRs." |
| agile-scrum-guide | "Explain the difference between the Sprint Review and the Retrospective." |
| skill-security-auditor | "Audit the skill folder I just downloaded before I install it." |

---

## Sources and credit

Skills marked *Agile36* were written for this class. Skills from MIT-licensed repos are copied here with their license file (see `THIRD_PARTY_NOTICES.md`). All others download from their author's repo at install time and are not re-hosted here.

| Skill | Author | License | Where it comes from |
|---|---|---|---|
| sprint-plan | [borghei/Claude-Skills](https://github.com/borghei/Claude-Skills) | MIT + Commons Clause | author's repo @ `25bf86b` |
| daily-scrum | Agile36 | Agile36 | this repo |
| sprint-review | Agile36 | Agile36 | this repo |
| scrum-retrospective | Agile36 | Agile36 | this repo |
| backlog-refinement | [borghei/Claude-Skills](https://github.com/borghei/Claude-Skills) | MIT + Commons Clause | author's repo @ `25bf86b` |
| scrum-of-scrums | [skills-on-ai/skills-on-ai](https://github.com/skills-on-ai/skills-on-ai) | none stated | author's repo @ `e8f587d` |
| sprint-retrospective | [borghei/Claude-Skills](https://github.com/borghei/Claude-Skills) | MIT + Commons Clause | author's repo @ `25bf86b` |
| scrum-role-coach | [byersboi/claude-agile-skills](https://github.com/byersboi/claude-agile-skills) | none stated | author's repo @ `a18f726` |
| agile-coach | [borghei/Claude-Skills](https://github.com/borghei/Claude-Skills) | MIT + Commons Clause | author's repo @ `25bf86b` |
| problem-solver | Hieu T. Luu | MIT (Hieu T. Luu) | this repo |
| scrum-workflow | Hieu T. Luu | MIT (Hieu T. Luu) | this repo |
| impediment-log | Agile36 | Agile36 | this repo |
| pre-mortem | [borghei/Claude-Skills](https://github.com/borghei/Claude-Skills) | MIT + Commons Clause | author's repo @ `25bf86b` |
| post-mortem | [borghei/Claude-Skills](https://github.com/borghei/Claude-Skills) | MIT + Commons Clause | author's repo @ `25bf86b` |
| dependency-map | [borghei/Claude-Skills](https://github.com/borghei/Claude-Skills) | MIT + Commons Clause | author's repo @ `25bf86b` |
| project-manager | Hieu T. Luu | MIT (Hieu T. Luu) | this repo |
| planning-poker | Agile36 | Agile36 | this repo |
| story-splitting | [borghei/Claude-Skills](https://github.com/borghei/Claude-Skills) | MIT + Commons Clause | author's repo @ `25bf86b` |
| story-mapping | [borghei/Claude-Skills](https://github.com/borghei/Claude-Skills) | MIT + Commons Clause | author's repo @ `25bf86b` |
| agile-product-owner | Alireza Rezvani | MIT (Alireza Rezvani) | this repo |
| prioritization-frameworks | [borghei/Claude-Skills](https://github.com/borghei/Claude-Skills) | MIT + Commons Clause | author's repo @ `25bf86b` |
| scrum-analytics | Alireza Rezvani | MIT (Alireza Rezvani) | this repo |
| cycle-time-analyzer | [borghei/Claude-Skills](https://github.com/borghei/Claude-Skills) | MIT + Commons Clause | author's repo @ `25bf86b` |
| brainstorm-okrs | [borghei/Claude-Skills](https://github.com/borghei/Claude-Skills) | MIT + Commons Clause | author's repo @ `25bf86b` |
| stakeholder-map | [borghei/Claude-Skills](https://github.com/borghei/Claude-Skills) | MIT + Commons Clause | author's repo @ `25bf86b` |
| status-update-generator | [borghei/Claude-Skills](https://github.com/borghei/Claude-Skills) | MIT + Commons Clause | author's repo @ `25bf86b` |
| team-communications | Alireza Rezvani | MIT (Alireza Rezvani) | this repo |
| summarize-meeting | [borghei/Claude-Skills](https://github.com/borghei/Claude-Skills) | MIT + Commons Clause | author's repo @ `25bf86b` |
| daci-framework | [borghei/Claude-Skills](https://github.com/borghei/Claude-Skills) | MIT + Commons Clause | author's repo @ `25bf86b` |
| jira-expert | [borghei/Claude-Skills](https://github.com/borghei/Claude-Skills) | MIT + Commons Clause | author's repo @ `25bf86b` |
| program-manager | [borghei/Claude-Skills](https://github.com/borghei/Claude-Skills) | MIT + Commons Clause | author's repo @ `25bf86b` |
| quarterly-planning | [borghei/Claude-Skills](https://github.com/borghei/Claude-Skills) | MIT + Commons Clause | author's repo @ `25bf86b` |
| agile-scrum-guide | [majiayu000/claude-skill-registry-data](https://github.com/majiayu000/claude-skill-registry-data) | none stated | author's repo @ `cc56cf7` |
| skill-security-auditor | [borghei/Claude-Skills](https://github.com/borghei/Claude-Skills) | MIT + Commons Clause | author's repo @ `25bf86b` |

Three skills were renamed so they don't clash: `scrum-role-coach`, `scrum-analytics` and `scrum-workflow` were all originally called `scrum-master`.

## Want more?

- [borghei/Claude-Skills](https://github.com/borghei/Claude-Skills): 400 skills, the source of many here
- [Claude Skill Registry](https://majiayu000.github.io/claude-skill-registry/): searchable community catalog
- [loremaster-ai/loremaster](https://github.com/loremaster-ai/loremaster): a complete AI Scrum Master system for Hermes Agent, built around a shared project wiki. Advanced; not installable skill-by-skill.

Before installing any skill, read its `SKILL.md` in full and open any scripts, or run `skill-security-auditor` on it.
