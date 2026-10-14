# ascii-wireframe

An agent skill that draws low-fidelity UI wireframes as fixed-width ASCII. Web app screens, mobile screens, landing pages, single components and common patterns.

Every drawing uses only `+ - |`, spaces, text and basic ASCII symbols. Every row is the same width, so it stays aligned in any monospace view: a terminal, a code block, a PR comment, a text file.

```wire
+- Login form -----------------------------------+
|                      LOGO                      |
|                                                |
|                  WELCOME BACK                  |
|              Sign in to continue               |
|                                                |
|                     Email                      |
|      +----------------------------------+      |
|      | name@company.com                 |      |
|      +----------------------------------+      |
|                                                |
|                    Password                    |
|      +----------------------------------+      |
|      | **********                       |      |
|      +----------------------------------+      |
|      [x] Remember me   <Forgot password?>      |
|                                                |
|      [[            Sign in             ]]      |
|                                                |
|                       or                       |
|                                                |
|      [       Continue with Google       ]      |
|                                                |
|             No account? <Sign up>              |
+------------------------------------------------+
```

It is plain markdown plus one optional Python script, so it works with any agent that can read files.

## Folder structure

```
SKILL.md                            rules, widths, workflow, validation, library map
references/primitives.md            grid, borders, inline tokens, icons, text hierarchy
references/components.md            18 component sheets
references/patterns.md              8 patterns: login, search with filters, dashboard
                                    header, pricing, empty state, table toolbar,
                                    settings list, product grid
references/screens/web-app.md       2 screens, 80 columns
references/screens/mobile-app.md    2 screens, 40 columns
references/screens/landing-page.md  1 screen, 80 columns
references/screens/flows.md         1 flow, 5 screens, web and mobile
scripts/validate.py                 optional validator
```

Frame widths: 80 columns for web and landing pages, 40 for mobile.

## Install

The skill folder should be named `ascii-wireframe`, matching the `name` in `SKILL.md`.

**Claude Code**, for all your projects:

```bash
git clone https://github.com/yoursharif/ascii-wireframe-skill.git ~/.claude/skills/ascii-wireframe
```

Or for one project, clone into `.claude/skills/ascii-wireframe` inside that repo.

**Claude apps**: download the repo as a zip and upload it under Settings > Capabilities > Skills.

**Any other agent**: put the folder somewhere the agent can read and point it at `SKILL.md`, for example from `AGENTS.md` or your system prompt:

```
When asked for a wireframe, follow ascii-wireframe/SKILL.md.
```

`SKILL.md` tells the agent which reference files to open for each kind of request.

## Validate

Requires Python 3, no dependencies.

```bash
python3 scripts/validate.py references/*.md references/screens/*.md
```

For a markdown file it checks every fenced block labelled `wire`. Any other file, or `-` for stdin, is treated as one drawing. It exits non zero when a row is the wrong width or a border does not line up.

Checks:

1. Printable ASCII only, no tabs.
2. Every row has the same width.
3. Every row starts and ends with `+` or `|`.
4. Every `|` has a `|` or `+` directly above or below.
5. Every `+` that touches a `-` has a `|` or `+` directly above or below.

Run it after any edit to the references. Every drawing in this repo passes.

## License

[CC BY-NC-ND 4.0](https://creativecommons.org/licenses/by-nc-nd/4.0/). Copyright (c) 2026 Md Shariful Islam Khan.

- You can install and use the skill, and share unchanged copies, with credit.
- You can't sell it or use it in a paid product.
- You can't share modified versions.

Full terms in [LICENSE](LICENSE).
