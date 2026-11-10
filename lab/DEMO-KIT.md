# Demo kit: present your two favorite skills

Each student presents two skills from the installed library (`../LIBRARY.md`),
or one from the library plus their own build. About 8 minutes per student.

## Pick

- At least one must be a Scrum Master skill you would actually use next sprint
- Different skills, ideally different levels (markdown-only vs. uses code)

## Structure (4 min per skill)

1. **The job** (30 sec): what problem does it solve for a Scrum Master?
2. **Live run** (2 min): give it one realistic prompt and show the output
3. **What I like** (1 min): one specific line or design choice, quoted from the file
4. **What I'd change** (30 sec): one weakness or missing guardrail

## Rules for live runs

- Use a made-up team and sprint. Never real names or company data.
- Prepare the prompt in advance. Show the prompt on screen.
- If the output is bad, say so. That is a good demo.

## Scorecard (audience scores 1-5)

| Criterion | Skill 1 | Skill 2 |
|---|---|---|
| Solves a real SM problem | | |
| Asks before it guesses | | |
| Has guardrails (what it won't do) | | |
| Output usable in a real meeting | | |
| Easy to copy to another tool | | |

## Bonus: port it

Run one demoed skill through `../tools/export_skill.py` and show it working in
a second tool (Copilot, ChatGPT, etc.). Same skill, different model.
