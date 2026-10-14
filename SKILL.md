---
name: ascii-wireframe
description: Draws low-fidelity UI wireframes as fixed-width ASCII text. Use when someone asks for a wireframe, layout sketch, screen outline or text mockup of a web app screen, mobile app screen, landing page, UI component or UI pattern. Output uses only + - | spaces, text and basic ASCII symbols, and every row has the same width.
---

# ASCII Wireframe

Draw UI layouts as plain text that stays aligned in any monospace view. Work from a small library of primitives, components, patterns and example screens, and validate every drawing before output.

This skill is plain markdown plus one optional Python script. It works in any agent that can read files.

## Hard rules

1. Use only `+`, `-`, `|`, spaces, text, brackets and basic ASCII symbols (printable characters 32 to 126).
2. Assume a monospace font. One character is one column.
3. Every row in a drawing has exactly the same character count.
4. All `+`, `|` and `-` characters align perfectly across rows and columns.
5. Treat each `+` as an exact corner or junction. Treat each `|` and `-` as a continuous border.
6. Never use proportional spacing, tabs, Unicode box-drawing characters, emoji or decorative characters.
7. Keep column widths, padding and spacing consistent. Padding is 1 space inside every box. The gap between boxes side by side is 1 column (2 in landing page columns).
8. Never put `|` in text content. Never put a bare `+` in text content. Write the word "plus" or use the icon `(+)` or `[+]`.
9. Before output, validate the character count of every row and fix any misalignment. See Validation.

## Frame widths

Pick the width from the target and keep it for the whole drawing.

| Target | Frame width | Inner width |
|---|---|---|
| Web app screen | 80 | 76 |
| Landing page | 80 | 76 |
| Mobile app screen | 40 | 36 |
| Component or pattern sheet | 30 to 80 | frame width minus 4 |

Height is free. Inner width is frame width minus 4: one border and one padding space on each side.

## Workflow

1. Name the target: web app, mobile app, landing page, component or pattern. Pick the frame width.
2. Open the matching reference file (see Library map). Start from the closest skeleton instead of inventing new symbols.
3. Lay out the regions first (header, sidebar, main, footer), then fill each region with components.
4. Build every row with the row formula below. Never eyeball alignment.
5. Validate. Fix. Validate again.
6. Output only the drawing.

## Building rows without drifting

- Inner width = frame width minus 4.
- Every content line is padded with spaces to exactly the inner width, then wrapped as `| ` + line + ` |`.
- Build nested boxes first. A nested box must be exactly as wide as the space it sits in, or be padded to it.
- Side by side boxes: box widths plus gaps must equal the parent inner width exactly. If the heights differ, pad the shorter one with blank rows that are the same width as that box.
- Sidebar plus main layouts share one junction column. The `+` in the separator row sits in the exact column of the `|` in every row below it.
- Left and right aligned text on one row (title and button, label and toggle): count both strings, then fill the gap with spaces so the row hits the inner width.
- Centered text: split the spare spaces left and right, extra space goes right.

## Validation

For every drawing, before output:

1. Count the characters in every row. All rows must match the frame width.
2. The first and last character of every row is `+` or `|`.
3. Every `|` has a `|` or `+` directly above or below it in the same column.
4. Every `+` that touches a `-` has a `|` or `+` directly above or below it in the same column.
5. Re-count after any fix, because one fix often shifts another row.

If you can run code, run the script and treat its output as the source of truth:

```
python3 scripts/validate.py drawing.txt
python3 scripts/validate.py references/components.md
```

It accepts a plain text file (the whole file is one drawing), a markdown file (it checks every fenced block labelled `wire`), or `-` for stdin. It exits with a non zero code when a row is the wrong width or a border does not line up.

## Library map

Read only what the request needs.

| File | Read it when |
|---|---|
| `references/primitives.md` | Always, first. Grid, borders, inline tokens, icons, text hierarchy. |
| `references/components.md` | The drawing needs a button, input, card, navbar, table, modal, tab bar or any single UI part. |
| `references/patterns.md` | The drawing needs a login form, search with filters, dashboard header, pricing block, empty state, table with toolbar, settings list or product grid. |
| `references/screens/web-app.md` | Full web app screens, 80 columns. |
| `references/screens/mobile-app.md` | Full mobile app screens, 40 columns. |
| `references/screens/landing-page.md` | Full landing pages, 80 columns. |

## Content rules

- Use realistic labels (Sign in, Add to cart, Last 30 days). Skip lorem ipsum.
- Use `xxxx xxxxx xxx` for body copy placeholders and `[ IMG ]` boxes for images.
- Use the exact tokens from `references/primitives.md` so the same thing always looks the same.
- Keep screens low fidelity. Layout and hierarchy matter, polish does not.

## Output format

- Reply with the drawing in one fenced code block labelled `text`. Nothing inside the block except the drawing.
- At most one short line above it, for example: Web dashboard, 80 columns.
- When asked to change something, redraw the whole drawing and validate again. Do not patch single rows.

### Saving to a file

Only when the user asks to save, download or export the wireframe:

- Save it as a `.md` file named after the screen, lowercase with hyphens, for example `web-analytics-dashboard.md`. Use the folder the user names, otherwise the current working directory.
- File content: a `#` title, the one short line, then the same `text` code block.
- When the drawing changes later, redraw it and overwrite the same file.
- Tell the user the file path. If you cannot write files, put the same markdown in the reply so the user can save it.

## Annotations

Not defined yet. Do not add numbered callouts, legends or notes unless the user asks for them. Draw the clean wireframe only.
