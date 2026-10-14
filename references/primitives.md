# Primitives

The smallest pieces. Every component, pattern and screen is built from these.

## Grid

- One character is one column. Assume a monospace font.
- Frame widths: 80 for web and landing, 40 for mobile.
- Inner width is frame width minus 4 (border plus 1 padding space on each side).
- Padding is 1 space inside every box. Gap between side by side boxes is 1 column.
- A blank row separates groups of content. Two blank rows are never needed.

## Borders

`+` is a corner or a junction. `-` is a horizontal edge. `|` is a vertical edge. Nothing else draws a border.

Plain box:

```wire
+----------------------------+
| Plain box                  |
+----------------------------+
```

Titled box. The title sits in the top edge with one space on each side:

```wire
+- Title --------------------+
| Titled box                 |
+----------------------------+
```

Nested box. The inner box is exactly as wide as the parent inner width:

```wire
+- Outer --------------------+
| +------------------------+ |
| | Inner box              | |
| +------------------------+ |
+----------------------------+
```

Side by side boxes. Widths plus gap equal the parent inner width:

```wire
+-------------------------------+
| +------------+ +------------+ |
| | Left       | | Right      | |
| +------------+ +------------+ |
+-------------------------------+
```

Grid. Every column shares its `+` junction with the `|` above and below it:

```wire
+----------+----------+----------+
| Name     | Role     | Status   |
+----------+----------+----------+
| Ana      | Admin    | Active   |
| Raj      | Editor   | Invited  |
+----------+----------+----------+
```

Split frame (header, sidebar and main). The `+` in the separator row sits in the exact column of the `|` below it:

```wire
+--------------------------------------+
| Header                               |
+----------+---------------------------+
| Menu     | Main content              |
| Item 1   |                           |
| Item 2   | xxxx xxxxx xxx            |
+----------+---------------------------+
```

Image placeholder. Label it IMG or with what it shows:

```wire
+----------------------+
|                      |
|                      |
|         IMG          |
|                      |
|                      |
+----------------------+
```

## Inline tokens

Use these exact tokens. They are not boxes, so they never need a frame.

```text
BUTTONS
[[ Primary ]]   [ Secondary ]   [- Disabled -]   [! Danger !]   <Text link>

ICON BUTTONS
[+] add    [X] close    [=] menu    [<] back    [>] forward    [...] more

FORM CONTROLS
[x] checked         [ ] unchecked       (o) selected       ( ) unselected
[ON ] toggle on     [OFF] toggle off
[ Choose one        v ]   select
[________________]        inline input
[ 12/200 ]                counter

ICONS
(Q) search   (b) bell   (@) user   (*) settings   (i) info   (!) warning
(?) help     <3 like    *  star    ^  up          v  down    >  next

STATUS AND DATA
(New) badge    {design} tag    (Active) status
[#####-----] progress          [----O------] slider

NAVIGATION
Home > Products > Shoes
< 1 [2] 3 4 ... 9 >
 Overview    Activity    Settings
 ========

TEXT
PAGE TITLE                 H1, all caps
Section Title              H2, title case
Body copy, sentence case   body
xxxx xxxxx xxx xxxxxxx     body copy placeholder
```

Rules for tokens:

- A bare `+` is not allowed in text. Add is `[+]` or `(+)`.
- `|` is not allowed in text. Use `/` or a gap of spaces to separate items.
- Up and down trend: `^ 12%` and `v 3%`.
- Primary action uses double brackets. There is at most one primary button per region.

## Spacing

- 1 space between a label and its value.
- 2 or 3 spaces between items in a row (buttons, tabs, nav links).
- 1 blank row between groups inside a box.
- Left aligned text starts right after the padding space. Never indent with tabs.

## Row formula

For a frame of width W and a content string `s`:

```
row = "|" + " " + s padded with spaces to (W - 4) + " " + "|"
```

Every row of the drawing is built this way, so every row is W characters. Count it. Do not eyeball it.
