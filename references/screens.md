# Screens

Full screens, one section per target. Read only the section that matches the request.

Read `primitives.md` and `components.md` first. For landing pages, also read `patterns.md`.

## Web app

Frame width 80, inner width 76. Header spans the full width. Sidebar is 18 columns, main is 59. The `+` in the separator row aligns with the sidebar `|` in every row below it.

### Dashboard

```wire
+------------------------------------------------------------------------------+
| LOGO  Acme Admin                                 (Q) Search   (b)  (@) Sam v |
+------------------+-----------------------------------------------------------+
|                  | DASHBOARD                              [ Last 30 days v ] |
| > Dashboard      |                                                           |
|   Orders         | +----------------+ +----------------+ +----------------+  |
|   Customers      | | Revenue        | | Orders         | | Refunds        |  |
|   Products       | | $48,200        | | 1,284          | | 23             |  |
|   Reports        | | ^ 12%          | | ^ 8%           | | v 3%           |  |
|                  | +----------------+ +----------------+ +----------------+  |
| --------------   |                                                           |
|   Settings       | +- Revenue ---------------------------------------------+ |
|   Help           | |                 ##          ## ##       ##            | |
|                  | |           ##    ## ##    ## ## ## ##    ##            | |
|                  | |     ## ## ## ## ## ## ## ## ## ## ## ## ##            | |
|                  | |  ## ## ## ## ## ## ## ## ## ## ## ## ## ##            | |
|                  | |  ## ## ## ## ## ## ## ## ## ## ## ## ## ##            | |
|                  | |  -------------------------------------------          | |
|                  | | Jan 1                                          Jan 30 | |
|                  | +-------------------------------------------------------+ |
|                  |                                                           |
|                  | Recent Orders                                             |
|                  | +---------+-----------------+-------------+-------------+ |
|                  | | Order   | Customer        | Status      | Total       | |
|                  | +---------+-----------------+-------------+-------------+ |
|                  | | #1042   | Ana Silva       | (Paid)      | $120.00     | |
|                  | | #1041   | Raj Patel       | (Pending)   | $86.50      | |
|                  | | #1040   | Mei Chen        | (Paid)      | $214.00     | |
|                  | +---------+-----------------+-------------+-------------+ |
+------------------+-----------------------------------------------------------+
```

### Settings form

```wire
+------------------------------------------------------------------------------+
| LOGO  Acme Admin                                 (Q) Search   (b)  (@) Sam v |
+------------------+-----------------------------------------------------------+
|                  | PROFILE                                                   |
| SETTINGS         |                                                           |
|                  | (@)  Sam Rahman   [ Change photo ]                        |
| > Profile        |                                                           |
|   Account        | First name                   Last name                    |
|   Notifications  | +--------------------------+ +--------------------------+ |
|   Billing        | | Sam                      | | Rahman                   | |
|   Team           | +--------------------------+ +--------------------------+ |
|                  |                                                           |
|                  | Email                                                     |
|                  | +-------------------------------------------------------+ |
|                  | | sam@acme.com                                          | |
|                  | +-------------------------------------------------------+ |
|                  |                                                           |
|                  | Bio                                                       |
|                  | +-------------------------------------------------------+ |
|                  | | xxxx xxxxx xxx xxxxxxx xxxx                           | |
|                  | |                                                       | |
|                  | |                                                       | |
|                  | +-------------------------------------------------------+ |
|                  |                                                           |
|                  | Email alerts                                        [ON ] |
|                  | Weekly digest                                       [OFF] |
|                  |                                                           |
|                  |                            [ Cancel ]  [[ Save changes ]] |
+------------------+-----------------------------------------------------------+
```

## Mobile app

Frame width 40, inner width 36. Status bar on top, app bar next, content, then the tab bar or the sticky action at the bottom. Two columns of cards use a 2 column gap.

### Home feed

```wire
+- Home -------------------------------+
| 9:41                            100% |
| [=]  SHOPFINDER             (b)  (@) |
|                                      |
| +----------------------------------+ |
| | (Q) Search products...       [X] | |
| +----------------------------------+ |
|                                      |
| Categories                           |
| [All]  Shoes  Bags  Watches  Tops    |
|                                      |
| Popular Now                <See all> |
| +---------------+  +---------------+ |
| | +-----------+ |  | +-----------+ | |
| | |           | |  | |           | | |
| | |    IMG    | |  | |    IMG    | | |
| | |           | |  | |           | | |
| | +-----------+ |  | +-----------+ | |
| | Runner Shoe   |  | Day Pack      | |
| | Lightweight   |  | Fits 15 inch  | |
| | $48     (New) |  | $64    (Sale) | |
| | [[ Add ]]     |  | [[ Add ]]     | |
| +---------------+  +---------------+ |
|                                      |
| New Arrivals               <See all> |
| +-----+  Trail Runner 2              |
| |     |  $89.00                      |
| |     |  [ Save ]                    |
| |     |                              |
| +-----+                              |
| +-----+  Field Watch                 |
| |     |  $120.00                     |
| |     |  [ Save ]                    |
| |     |                              |
| +-----+                              |
|                                      |
| ------------------------------------ |
| +----------------------------------+ |
| |  [Home]  Search  Saved     Me    | |
| +----------------------------------+ |
+--------------------------------------+
```

### Product detail

```wire
+- Product detail ---------------------+
| 9:41                            100% |
| [<]  Product details         <3  [=] |
|                                      |
| +----------------------------------+ |
| |                                  | |
| |                                  | |
| |                                  | |
| |                                  | |
| |          PRODUCT IMAGE           | |
| |                                  | |
| |                                  | |
| |                                  | |
| |                                  | |
| +----------------------------------+ |
|                                      |
| Trail Runner 2                $89.00 |
| * * * * -   4.2 (128)                |
|                                      |
| Size                                 |
|    S      [M]      L      XL         |
|                                      |
| Description                          |
| xxxx xxxxx xxx xxxxxxx xxxx          |
| xxxxx xxx xxxxxx xxxxx xx            |
|                                      |
| ------------------------------------ |
| [ <3 ]  [[      Add to cart       ]] |
+--------------------------------------+
```

## Landing page

Frame width 80, inner width 76. Sections stack top to bottom and are separated by a plain row of `-`. Three column blocks use a 2 column gap so they fill the inner width exactly: 24 + 2 + 24 + 2 + 24 = 76.

Section order: navbar, hero, social proof, features, testimonial, pricing, closing call to action, footer.

```wire
+- Landing page ---------------------------------------------------------------+
| LOGO                  Features  Pricing  Docs   [ Sign in ] [[ Start free ]] |
| ---------------------------------------------------------------------------- |
|                                                                              |
|                           SHIP YOUR PRODUCT FASTER                           |
|                One workspace for plans, designs and launches.                |
|                                                                              |
|                      [[ Start free ]]   [ Book a demo ]                      |
|                                                                              |
|         +----------------------------------------------------------+         |
|         |                                                          |         |
|         |                                                          |         |
|         |                                                          |         |
|         |                        HERO IMAGE                        |         |
|         |                                                          |         |
|         |                                                          |         |
|         |                                                          |         |
|         +----------------------------------------------------------+         |
|                                                                              |
| ---------------------------------------------------------------------------- |
|                             Trusted by teams at                              |
|                   LOGO     LOGO     LOGO     LOGO     LOGO                   |
| ---------------------------------------------------------------------------- |
|                                   Features                                   |
|                        Everything you need to launch                         |
|                                                                              |
| +----------------------+  +----------------------+  +----------------------+ |
| | (*)                  |  | (@)                  |  | (Q)                  | |
| | Fast setup           |  | Team workspace       |  | Instant search       | |
| | xxxxxxxx xxxx xxxxx  |  | xxxxxxxx xxxx xxxxx  |  | xxxxxxxx xxxx xxxxx  | |
| | xxxxxx xxxx xxx xxxx |  | xxxxxx xxxx xxx xxxx |  | xxxxxx xxxx xxx xxxx | |
| +----------------------+  +----------------------+  +----------------------+ |
|                                                                              |
| ---------------------------------------------------------------------------- |
|         xxxx xxxxx xxxx xxxxxxx xxxxx xxxx xxxxxxx xxxxx xxxx xxxxx.         |
|                        (@) Ana Silva, Head of Product                        |
| ---------------------------------------------------------------------------- |
|                                   Pricing                                    |
|                                                                              |
| +----------------------+  +- Popular ------------+  +----------------------+ |
| |       STARTER        |  |         TEAM         |  |       BUSINESS       | |
| |      $0 / month      |  |     $29 / month      |  |     $99 / month      | |
| |                      |  |                      |  |                      | |
| | 1 project            |  | 10 projects          |  | Unlimited projects   | |
| | Basic reports        |  | Advanced reports     |  | Custom reports       | |
| | Email support        |  | Priority support     |  | Dedicated manager    | |
| |                      |  |                      |  |                      | |
| |    [ Start free ]    |  |  [[ Choose Team ]]   |  |    [ Contact us ]    | |
| +----------------------+  +----------------------+  +----------------------+ |
|                                                                              |
| ---------------------------------------------------------------------------- |
| +--------------------------------------------------------------------------+ |
| |                             Ready to launch?                             | |
| |                                                                          | |
| |                             [[ Start free ]]                             | |
| +--------------------------------------------------------------------------+ |
|                                                                              |
| ---------------------------------------------------------------------------- |
| PRODUCT            COMPANY            RESOURCES          LEGAL               |
| Features           About              Docs               Privacy             |
| Pricing            Careers            Blog               Terms               |
| Changelog          Contact            Support            Security            |
|                                                                              |
| (c) 2026 Acme Inc.                                        <Privacy>  <Terms> |
+------------------------------------------------------------------------------+
```
