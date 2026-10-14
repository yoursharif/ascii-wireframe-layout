# Mobile app screens

Frame width 40, inner width 36. Status bar on top, app bar next, content, then the tab bar or the sticky action at the bottom. Two columns of cards use a 2 column gap.

Read `primitives.md` and `components.md` first.

## Home feed

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
| Popular now                <See all> |
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
| New arrivals               <See all> |
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

## Product detail

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
