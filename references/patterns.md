# Patterns

Common multi-component groups. Copy the pattern, then swap the labels. Keep the widths.

Read `components.md` first.

## Login form

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

## Search with filters

```wire
+- Search with filters --------------------------------------------------------+
| +--------------------------------------------------------------------------+ |
| | (Q) running shoes                                           [[ Search ]] | |
| +--------------------------------------------------------------------------+ |
|                                                                              |
| +- Filters ----------+ +- Results -----------------------------------------+ |
| | Category           | | 128 results                       Sort: Popular v | |
| | [x] Shoes          | |                                                   | |
| | [ ] Bags           | | +-------+  Trail Runner 2                         | |
| | [ ] Watches        | | |       |  Lightweight, waterproof                | |
| |                    | | |  IMG  |  $89.00   * 4.5 (212)                   | |
| | Price              | | |       |                                         | |
| | [----O------]      | | +-------+  [ Save ]                               | |
| | $20       $200     | | ------------------------------------------------- | |
| |                    | | +-------+  Road Glide                             | |
| | Rating             | | |       |  Cushioned daily trainer                | |
| | (o) 4 stars and up | | |  IMG  |  $74.00   * 4.3 (98)                    | |
| | ( ) Any            | | |       |                                         | |
| +--------------------+ | +-------+  [ Save ]                               | |
|                        +---------------------------------------------------+ |
+------------------------------------------------------------------------------+
```

## Dashboard header

```wire
+- Dashboard header -----------------------------------------------------------+
| OVERVIEW                                    [ Last 30 days v ]  [[ Export ]] |
|                                                                              |
|  Overview    Sales    Customers                                              |
|  ========                                                                    |
| ---------------------------------------------------------------------------- |
|                                                                              |
| +----------------+ +----------------+ +----------------+ +----------------+  |
| | Revenue        | | Orders         | | Customers      | | Refunds        |  |
| | $48,200        | | 1,284          | | 932            | | 23             |  |
| | ^ 12%          | | ^ 8%           | | ^ 5%           | | v 3%           |  |
| +----------------+ +----------------+ +----------------+ +----------------+  |
+------------------------------------------------------------------------------+
```

## Pricing block

The featured tier gets a title in its top edge and the primary button.

```wire
+- Pricing block --------------------------------------------------------------+
|                                   PRICING                                    |
|                       Simple plans that scale with you                       |
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
+------------------------------------------------------------------------------+
```

## Empty state

```wire
+- Empty state ----------------------------------+
|                                                |
|                 +-----------+                  |
|                 |           |                  |
|                 |    (+)    |                  |
|                 |           |                  |
|                 +-----------+                  |
|                                                |
|                NO PROJECTS YET                 |
|   Create your first project to get started.    |
|                                                |
|              [[ Create project ]]              |
|                                                |
+------------------------------------------------+
```

## Table with toolbar

```wire
+- Table with toolbar ---------------------------------------------------------+
| +--------------------------+ +----------------+                              |
| | (Q) Search users...      | | Role: All    v |            [[ Invite user ]] |
| +--------------------------+ +----------------+                              |
|                                                                              |
| +-----+----------------------+----------------+-------------+--------------+ |
| | [ ] | Name v               | Role           | Status      | Actions      | |
| +-----+----------------------+----------------+-------------+--------------+ |
| | [x] | Ana Silva            | Admin          | (Active)    | [ Edit ]     | |
| | [ ] | Raj Patel            | Editor         | (Invited)   | [ Edit ]     | |
| | [ ] | Mei Chen             | Viewer         | (Active)    | [ Edit ]     | |
| | [ ] | Leo Kim              | Viewer         | (Active)    | [ Edit ]     | |
| +-----+----------------------+----------------+-------------+--------------+ |
| Showing 1-10 of 128                                     < 1 [2] 3 4 ... 13 > |
+------------------------------------------------------------------------------+
```

## Settings list

Label and toggle on one row, description below.

```wire
+- Settings list --------------------------------+
| Email alerts                             [ON ] |
| Product news and updates                       |
+------------------------------------------------+
| Weekly digest                            [OFF] |
| A summary every Monday                         |
+------------------------------------------------+
| Two step sign in                         [ON ] |
| Ask for a code on new devices                  |
+------------------------------------------------+
| Public profile                           [OFF] |
| Let others find you by name                    |
+------------------------------------------------+
```

## Product grid

```wire
+- Product grid ---------------------------------------------------------------+
| +----------------------+  +----------------------+  +----------------------+ |
| | +------------------+ |  | +------------------+ |  | +------------------+ | |
| | |                  | |  | |                  | |  | |                  | | |
| | |       IMG        | |  | |       IMG        | |  | |       IMG        | | |
| | |                  | |  | |                  | |  | |                  | | |
| | +------------------+ |  | +------------------+ |  | +------------------+ | |
| | Running Shoe         |  | Day Backpack         |  | Field Watch          | |
| | Light and waterproof |  | Fits 15 inch laptop  |  | Water resistant 40mm | |
| | $89.00         (New) |  | $64.00        (Sale) |  | $120.00        (New) | |
| | [[ Add to cart ]]    |  | [[ Add to cart ]]    |  | [[ Add to cart ]]    | |
| +----------------------+  +----------------------+  +----------------------+ |
+------------------------------------------------------------------------------+
```
