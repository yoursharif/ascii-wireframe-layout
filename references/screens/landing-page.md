# Landing page

Frame width 80, inner width 76. Sections stack top to bottom and are separated by a plain row of `-`. Three column blocks use a 2 column gap so they fill the inner width exactly: 24 + 2 + 24 + 2 + 24 = 76.

Section order: navbar, hero, social proof, features, testimonial, pricing, closing call to action, footer.

Read `primitives.md`, `components.md` and `patterns.md` first.

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
|             [ Logo ]   [ Logo ]   [ Logo ]   [ Logo ]   [ Logo ]             |
| ---------------------------------------------------------------------------- |
|                                   FEATURES                                   |
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
|                                   PRICING                                    |
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
