# Description
## CTRL+ keys
| char                | origin                                                |
| :------------------ | ----------------------------------------------------- |
| `CTRL-C`            | `Interrupt`                                           |
| `CTRL-V`            | `Visual-block mode`                                   |
| `CTRL-A` & `CTRL-X` | `+ N number under cursor` & `- N number under cursor` |

| char                | origin                                      |
| :------------------ | ------------------------------------------- |
| `CTRL-E` & `CTRL-Y` | `Scroll up N lines` & `Scroll down N lines` |
| `CTRL-U` & `CTRL-D` | `Up half screen` & `Down half screen`       |
| `CTRL-F` & `CTRL-B` | `Forward N screen` & `Backward N screen`    |

| char                | origin                    |
| :------------------ | ------------------------- |
| `CTRL-O` & `CTRL-T` | `Jump back N times` `???` |

| char            | origin |
| :-------------- | ------ |
| `CTRL-@`        |        |
| `CTRL-G`        |        |
| `CTRL-H`        |        |
| `CTRL-I`        |        |
| `CTRL-J`        |        |
| `CTRL-K`        |        |
| `CTRL-L`        |        |
| `CTRL-M`        |        |
| `CTRL-N`        |        |
| `CTRL-P`        |        |
| `CTRL-Q`        |        |
| `CTRL-R`        |        |
| `CTRL-S`        |        |
| `CTRL-W` {char} |        |
| `CTRL-Z`        |        |
| `CTRL-[` <Esc>  |        |
| `CTRL-\` CTRL-N |        |
| `CTRL-\` CTRL-G |        |
| `CTRL-\` a - z  |        |
| `CTRL-\` others |        |
| `CTRL-]`        |        |
| `CTRL-^`        |        |
| `CTRL-_`        |        |

| char                | origin |
| :------------------ | ------ |
| `<BS>`              |        |
| `<Tab>`             |        |
| `<NL>`              |        |
| `<CR>`              |        |
| `<Space>`           |        |
| `!{motion}{filter}` |        |
| `!!{filter}`        |        |
| `"{register}`       |        |
| `#`                 |        |
| `$`                 |        |
| `%`                 |        |
| `{count}%`          |        |
| `&`                 |        |
| `'{a-zA-Z0-9}`      |        |
| `''`                |        |
| `'(`                |        |
| `')`                |        |
| `'<`                |        |
| `'>`                |        |
| `'[`                |        |
| `']`                |        |
| `'{`                |        |
| `'}`                |        |
| `(`                 |        |
| `)`                 |        |
| `*`                 |        |
| `+`                 |        |
| `,`                 |        |
| `-`                 |        |
| `.`                 |        |
| `/{pattern}<CR>`    |        |
| `/<CR>`             |        |

| char             | origin |
| :--------------- | ------ |
| `0`              |        |
| `1`              |        |
| `2`              |        |
| `3`              |        |
| `4`              |        |
| `5`              |        |
| `6`              |        |
| `7`              |        |
| `8`              |        |
| `9`              |        |
| `:`              |        |
| `{count}:`       |        |
| `;`              |        |
| `<{motion}`      |        |
| `<<`             |        |
| `={motion}`      |        |
| `==`             |        |
| `>{motion}`      |        |
| `>>`             |        |
| `?{pattern}<CR>` |        |
| `?<CR>`          |        |
| `@{a-z}`         |        |
| `@:`             |        |
| `@@`             |        |

## Uppercase keys
| char               | origin               |
| :----------------- | -------------------- |
| `[{char}`          | `???`                |
| `\`                | <Nop>                |
| `]{char}`          | `???`                |
| `^`                | `first char of line` |
| `_`                | `~~ ^`               |
| ````{a-zA-Z0-9}``` |                      |
| ````(```           |                      |
| ````)```           |                      |
| ````<```           |                      |
| ````>```           |                      |
| ````[```           |                      |
| ````]```           |                      |
| ````````           |                      |
| ````{```           |                      |
| ````}```           |                      |

| char | origin      |
| :--- | ----------- |
| `i`  | `insert`    |
| `I`  | `INSERT`    |
| `a`  | `append`    |
| `A`  | `APPEND`    |
| `o`  | `open line` |
| `O`  | `OPEN line` |

| char            | origin            |
| :-------------- | ----------------- |
| `["x]c{motion}` | `change`          |
| `["x]cc`        | `change line`     |
| `["x]C`         | `Change to end`   |
| `["x]s`         | `substitute`      |
| `["x]S`         | `substitute line` |
| `["x]d{motion}` | `delete`          |
| `["x]dd`        | `delete line`     |
| `do`            | `:diffget`        |
| `dp`            | `:diffput`        |
| `["x]D`         | `Delete to end`   |

| char            | origin               |
| :-------------- | -------------------- |
| `w`             | `word N words`       |
| `W`             | `WORD N WORDS`       |
| `b`             | `backward N words`   |
| `B`             | `BACKWARD N WORDS`   |
| `e`             | `end N words`        |
| `E`             | `END N WORDS`        |
| `f{char}`       | `find forward`       |
| `F{char}`       | `FIND backward`      |
| `g{char}`       | `go` `???`           |
| `h`             | `←`                  |
| `j`             | `↓`                  |
| `k`             | `↑`                  |
| `l`             | `→`                  |
| `m{A-Za-z}`     | `mark`               |
| `n`             | `next`               |
| `["x]p`         | `paste`              |
| `["x]P`         | `PASTE???`           |
| `q{0-9a-zA-Z"}` | `record`             |
| `q`             | `stop record`        |
| `q:`            |                      |
| `q/`            |                      |
| `q?`            |                      |
| `r{char}`       | `replace`            |
| `R`             | `REPLACE`            |
| `t{char}`       | `till`               |
| `u`             | `undo`               |
| `v`             | `Visual mode`        |
| `["x]x`         | `delete char`        |
| `["x]y{motion}` | `yank`               |
| `["x]yy`        | `yank line`          |
| `z{char}`       | `???`                |
| `G`             | `GO`                 |
| `H`             | `High`               |
| `J`             | `Join`               |
| `K`             | `:help under cursor` |
| `L`             | `Low`                |
| `M`             | `Middle`             |
| `N`             | `NEXT`               |
| `Q`             | `Ex mode???`         |
| `T{char}`       | `TILL`               |
| `U`             | `undo all on line`   |
| `V`             | `Visual-line mode`   |
| `["x]X`         | `== <Del> == <C-h>`  |
| `["x]Y`         | `== yy`              |
| `ZZ`            | `~= :wq`             |
| `ZQ`            | `== :q!`             |

| char                                                                                   | origin |
| :------------------------------------------------------------------------------------- | ------ |
| `{`                                                                                    |        |
| `|`                                                                                    |        |
| `}`                                                                                    |        |
| `~`                                                                                    |        |
| `~{motion}`                                                                            |        |
| `<C-End>`                                                                              |        |
| `<C-Home>`                                                                             |        |
| `<C-Left>`                                                                             |        |
| `<C-LeftMouse>`                                                                        |        |
| `<C-Right>`                                                                            |        |
| `<C-RightMouse>`                                                                       |        |
| `<C-Tab>`                                                                              |        |
| `<Up>`                                                                                 |        |
| `<Down>`                                                                               |        |
| `<Left>`                                                                               |        |
| `<Right>`                                                                              |        |
| `<Insert>`                                                                             |        |
| `["x]<Del>`                                                                            |        |
| `{count}<Del>`                                                                         |        |
| `<Home>`                                                                               |        |
| `<End>`                                                                                |        |
| `<PageUp>`                                                                             |        |
| `<PageDown>`                                                                           |        |
| `<F1>`                                                                                 |        |
| `<Help>`                                                                               |        |
| `<LeftMouse>`                                                                          |        |
| `<MiddleMouse>`                                                                        |        |
| `<RightMouse>`                                                                         |        |
| `<ScrollWheelUp>` `<ScrollWheelDown>` `<ScrollWheelLeft>` `<ScrollWheelRight>`         |        |
| `<S-Up>`                                                                               |        |
| `<S-Down>`                                                                             |        |
| `<S-Left>`                                                                             |        |
| `<S-Right>`                                                                            |        |
| `<S-LeftMouse>`                                                                        |        |
| `<S-RightMouse>`                                                                       |        |
| `<Undo>`                                                                               |        |
| `<S-ScrollWheelUp>` `<S-ScrollWheelDown>` `<S-ScrollWheelLeft>` `<S-ScrollWheelRight>` |        |

# Index
|                                                                                                                                       origin action |          char          | remap                                        |
| --------------------------------------------------------------------------------------------------------------------------------------------------: | :--------------------: | :------------------------------------------- |
|                                                                                                                                            not used |        `CTRL-@`        | x                                            |
|                                                                                                                     add N to number at/after cursor |        `CTRL-A`        |                                              |
|                                                                                                                          scroll N screens Backwards |        `CTRL-B`        |                                              |
|                                                                                                                  interrupt current (search) command |        `CTRL-C`        |                                              |
|                                                                                                        scroll Down N lines (default: half a screen) |        `CTRL-D`        |                                              |
|                                                                                                              scroll N lines upwards (N lines Extra) |        `CTRL-E`        |                                              |
|                                                                                                                            scroll N screens Forward |        `CTRL-F`        |                                              |
|                                                                                                              display current file name and position |        `CTRL-G`        |                                              |
|                                                                                                                                         same as "h" |         `<BS>`         | x                                            |
|                                                                                                                                         same as "h" |        `CTRL-H`        | go to Nth left window (stop at first window) |
|                                                                                                                    go to N newer entry in jump list |        `<Tab>`         |                                              |
|                                                                                                                                       same as <Tab> |        `CTRL-I`        | x                                            |
|                                                                                                                                         same as "j" |         `<NL>`         | x                                            |
|                                                                                                                                         same as "j" |        `CTRL-J`        | go N windows down (stop at last window)      |
|                                                                                                                                            not used |        `CTRL-K`        | go N windows up (stop at first window)       |
|                                                                                                                                       redraw screen |        `CTRL-L`        | go to Nth right window (stop at last window) |
|                                                                                                              cursor to the first CHAR N lines lower |         `<CR>`         |                                              |
|                                                                                                                                        same as <CR> |        `CTRL-M`        | x                                            |
|                                                                                                                                         same as "j" |        `CTRL-N`        | x                                            |
|                                                                                                                    go to N older entry in jump list |        `CTRL-O`        |                                              |
|                                                                                                                                         same as "k" |        `CTRL-P`        | x                                            |
|                                                                                                         not used, or used for terminal control flow |        `CTRL-Q`        | ?                                            |
|                                                                                                             redo changes which were undone with 'u' |        `CTRL-R`        |                                              |
|                                                                                                         not used, or used for terminal control flow |        `CTRL-S`        | ?                                            |
|                                                                                                                     jump to N older Tag in tag list |        `CTRL-T`        |                                              |
|                                                                                                     scroll N lines Upwards (default: half a screen) |        `CTRL-U`        |                                              |
|                                                                                                                         start blockwise Visual mode |        `CTRL-V`        |                                              |
|                                                                                                                         window commands, see CTRL-W |    `CTRL-W` {char}     |                                              |
|                                                                                                              subtract N from number at/after cursor |        `CTRL-X`        |                                              |
|                                                                                                                            scroll N lines downwards |        `CTRL-Y`        |                                              |
|                                                                                                                suspend program (or start new shell) |        `CTRL-Z`        |                                              |
|                                                                                                                                            not used |     `CTRL-[` <Esc>     | x                                            |
|                                                                                                                           go to Normal mode (no-op) |    `CTRL-\` CTRL-N     |                                              |
|                                                                                                              go to mode specified with 'insertmode' |    `CTRL-\` CTRL-G     |                                              |
|                                                                                                                             reserved for extensions |     `CTRL-\` a - z     |                                              |
|                                                                                                                                            not used |    `CTRL-\` others     | x                                            |
|                                                                                                                           :ta to ident under cursor |        `CTRL-]`        |                                              |
|                                                                                                     edit Nth alternate file (equivalent to ":e #N") |        `CTRL-^`        | x                                            |
|                                                                                                                                            not used |        `CTRL-_`        |                                              |
|                                                                                                                                         same as "l" |       `<Space>`        | `<Leader>`                                   |
|                                                                                                      filter Nmove text through the {filter} command |  `!{motion}{filter}`   |                                              |
|                                                                                                         filter N lines through the {filter} command |      `!!{filter}`      |                                              |
|                                                                             use {register} for next delete, yank or put ({.%#:} only work with put) |     `"{register}`      |                                              |
|                                                                                search backward for the Nth occurrence of the ident under the cursor |          `#`           |                                              |
|                                                                                                                  cursor to the end of Nth next line |          `$`           |                                              |
| find the next (curly/square) bracket on this line and go to its match, or go to matching comment bracket, or go to matching preprocessor directive. |          `%`           |                                              |
|                                                                                                                      go to N percentage in the file |       `{count}%`       |                                              |
|                                                                                                                                      repeat last :s |          `&`           |                                              |
|                                                                                          cursor to the first CHAR on the line with mark {a-zA-Z0-9} |     `'{a-zA-Z0-9}`     |                                              |
|                                                                   cursor to the first CHAR of the line where the cursor was before the latest jump. |          `''`          |                                              |
|                                                                           cursor to the first CHAR on the line of the start of the current sentence |          `'(`          |                                              |
|                                                                             cursor to the first CHAR on the line of the end of the current sentence |          `')`          |                                              |
|                                                   cursor to the first CHAR of the line where highlighted area starts/started in the current buffer. |          `'<`          |                                              |
|                                                       cursor to the first CHAR of the line where highlighted area ends/ended in the current buffer. |          `'>`          |                                              |
|                                                        cursor to the first CHAR on the line of the start of last operated text or start of put text |          `'[`          |                                              |
|                                                            cursor to the first CHAR on the line of the end of last operated text or end of put text |          `']`          |                                              |
|                                                                          cursor to the first CHAR on the line of the start of the current paragraph |          `'{`          |                                              |
|                                                                            cursor to the first CHAR on the line of the end of the current paragraph |          `'}`          |                                              |
|                                                                                                                         cursor N sentences backward |          `(`           |                                              |
|                                                                                                                          cursor N sentences forward |          `)`           |                                              |
|                                                                                 search forward for the Nth occurrence of the ident under the cursor |          `*`           |                                              |
|                                                                                                                                        same as <CR> |          `+`           | x                                            |
|                                                                                            repeat latest f, t, F or T in opposite direction N times |          `,`           |                                              |
|                                                                                                             cursor to the first CHAR N lines higher |          `-`           |                                              |
|                                                                                                       repeat last change with count replaced with N |          `.`           |                                              |
|                                                                                                  search forward for the Nth occurrence of {pattern} |    `/{pattern}<CR>`    |                                              |
|                                                                                                         search forward for {pattern} of last search |        `/<CR>`         |                                              |
|                                                                                                                cursor to the first char of the line |          `0`           |                                              |
|                                                                                                                  prepend to command to give a count |          `1`           |                                              |
|                                                                                                                                                   " |          `2`           |                                              |
|                                                                                                                                                   " |          `3`           |                                              |
|                                                                                                                                                   " |          `4`           |                                              |
|                                                                                                                                                   " |          `5`           |                                              |
|                                                                                                                                                   " |          `6`           |                                              |
|                                                                                                                                                   " |          `7`           |                                              |
|                                                                                                                                                   " |          `8`           |                                              |
|                                                                                                                                                   " |          `9`           |                                              |
|                                                                                                                        start entering an Ex command |          `:`           |                                              |
|                                                                         start entering an Ex command with range from current line to N-1 lines down |       `{count}:`       |                                              |
|                                                                                                                  repeat latest f, t, F or T N times |          `;`           |                                              |
|                                                                                                        shift Nmove lines one 'shiftwidth' leftwards |      `<{motion}`       |                                              |
|                                                                                                            shift N lines one 'shiftwidth' leftwards |          `<<`          |                                              |
|                                                                                                                 filter Nmove lines through "indent" |      `={motion}`       |                                              |
|                                                                                                                     filter N lines through "indent" |          `==`          |                                              |
|                                                                                                       shift Nmove lines one 'shiftwidth' rightwards |      `>{motion}`       |                                              |
|                                                                                                           shift N lines one 'shiftwidth' rightwards |          `>>`          |                                              |
|                                                                                        search backward for the Nth previous occurrence of {pattern} |    `?{pattern}<CR>`    |                                              |
|                                                                                                        search backward for {pattern} of last search |        `?<CR>`         |                                              |
|                                                                                                      execute the contents of register {a-z} N times |        `@{a-z}`        |                                              |
|                                                                                                             repeat the previous ":" command N times |          `@:`          |                                              |
|                                                                                                                  repeat the previous @{a-z} N times |          `@@`          |                                              |
|                                                                                                       append text after the end of the line N times |          `A`           |                                              |
|                                                                                                                             cursor N WORDS backward |          `B`           |                                              |
|                                      change from the cursor position to the end of the line, and N-1 more lines [into register x]; synonym for "c$" |        `["x]C`         | _                                            |
|                             delete the characters under the cursor until the end of the line and N-1 more lines [into register x]; synonym for "d$" |        `["x]D`         | _                                            |
|                                                                                                                 cursor forward to the end of WORD N |          `E`           |                                              |
|                                                                                                  cursor to the Nth occurrence of {char} to the left |       `F{char}`        |                                              |
|                                                                                                                 cursor to line N, default last line |          `G`           |                                              |
|                                                                                                                 cursor to line N from top of screen |          `H`           |                                              |
|                                                                                               insert text before the first CHAR on the line N times |          `I`           |                                              |
|                                                                                                                          Join N lines; default is 2 |          `J`           |                                              |
|                                                                                                   lookup Keyword under the cursor with 'keywordprg' |          `K`           |                                              |
|                                                                                                              cursor to line N from bottom of screen |          `L`           |                                              |
|                                                                                                                     cursor to middle line of screen |          `M`           |                                              |
|                                                                                          repeat the latest '/' or '?' N times in opposite direction |          `N`           |                                              |
|                                                                                   begin a new line above the cursor and insert text, repeat N times |          `O`           |                                              |
|                                                                                            put the text [from register x] before the cursor N times |        `["x]P`         |                                              |
|                                                                                                                                 switch to "Ex" mode |          `Q`           |                                              |
|                                                                 enter replace mode: overtype existing characters, repeat the entered text N-1 times |          `R`           |                                              |
|                                                                                delete N lines [into register x] and start insert; synonym for "cc". |        `["x]S`         |                                              |
|                                                                                              cursor till after Nth occurrence of {char} to the left |       `T{char}`        |                                              |
|                                                                                                                 undo all latest changes on one line |          `U`           |                                              |
|                                                                                                                          start linewise Visual mode |          `V`           |                                              |
|                                                                                                                              cursor N WORDS forward |          `W`           |                                              |
|                                                                                             delete N characters before the cursor [into register x] |        `["x]X`         |                                              |
|                                                                                                    yank N lines [into register x]; synonym for "yy" |        `["x]Y`         |                                              |
|                                                                                                            write if buffer changed and close window |          `ZZ`          |                                              |
|                                                                                                                        close window without writing |          `ZQ`          |                                              |
|                                                                                                                square bracket command (see [ below) |       `[{char}`        |                                              |
|                                                                                                                                            not used |          `\`           | x                                            |
|                                                                                                                square bracket command (see ] below) |       `]{char}`        |                                              |
|                                                                                                                cursor to the first CHAR of the line |          `^`           |                                              |
|                                                                                                          cursor to the first CHAR N - 1 lines lower |          `_`           |                                              |
|                                                                                                                      cursor to the mark {a-zA-Z0-9} |   ````{a-zA-Z0-9}```   |                                              |
|                                                                                                         cursor to the start of the current sentence |        ````(```        |                                              |
|                                                                                                           cursor to the end of the current sentence |        ````)```        |                                              |
|                                                                                                         cursor to the start of the highlighted area |        ````<```        |                                              |
|                                                                                                           cursor to the end of the highlighted area |        ````>```        |                                              |
|                                                                                   cursor to the start of last operated text or start of putted text |        ````[```        |                                              |
|                                                                                       cursor to the end of last operated text or end of putted text |        ````]```        |                                              |
|                                                                                                           cursor to the position before latest jump |        ````````        |                                              |
|                                                                                                        cursor to the start of the current paragraph |        ````{```        |                                              |
|                                                                                                          cursor to the end of the current paragraph |        ````}```        |                                              |
|                                                                                                                append text after the cursor N times |          `a`           |                                              |
|                                                                                                                             cursor N words backward |          `b`           |                                              |
|                                                                                                delete Nmove text [into register x] and start insert |    `["x]c{motion}`     |                                              |
|                                                                                                   delete N lines [into register x] and start insert |        `["x]cc`        |                                              |
|                                                                                                                 delete Nmove text [into register x] |    `["x]d{motion}`     |                                              |
|                                                                                                                    delete N lines [into register x] |        `["x]dd`        |                                              |
|                                                                                                                                  same as ":diffget" |          `do`          | x                                            |
|                                                                                                                                  same as ":diffput" |          `dp`          | x                                            |
|                                                                                                                 cursor forward to the end of word N |          `e`           |                                              |
|                                                                                                     cursor to Nth occurrence of {char} to the right |       `f{char}`        |                                              |
|                                                                                                                      extended commands, see g below |       `g{char}`        |                                              |
|                                                                                                                          cursor N chars to the left |          `h`           |                                              |
|                                                                                                               insert text before the cursor N times |          `i`           |                                              |
|                                                                                                                             cursor N lines downward |          `j`           |                                              |
|                                                                                                                               cursor N lines upward |          `k`           |                                              |
|                                                                                                                         cursor N chars to the right |          `l`           |                                              |
|                                                                                                                set mark {A-Za-z} at cursor position |      `m{A-Za-z}`       |                                              |
|                                                                                                                repeat the latest '/' or '?' N times |          `n`           |                                              |
|                                                                                   begin a new line below the cursor and insert text, repeat N times |          `o`           |                                              |
|                                                                                             put the text [from register x] after the cursor N times |        `["x]p`         |                                              |
|                                                                      record typed characters into named register {0-9a-zA-Z"} (uppercase to append) |    `q{0-9a-zA-Z"}`     |                                              |
|                                                                                                                   (while recording) stops recording |          `q`           |                                              |
|                                                                                                          edit : command-line in command-line window |          `q:`          |                                              |
|                                                                                                          edit / command-line in command-line window |          `q/`          |                                              |
|                                                                                                          edit ? command-line in command-line window |          `q?`          |                                              |
|                                                                                                                         replace N chars with {char} |       `r{char}`        |                                              |
|                                                                                 (substitute) delete N characters [into register x] and start insert |        `["x]s`         |                                              |
|                                                                                            cursor till before Nth occurrence of {char} to the right |       `t{char}`        |                                              |
|                                                                                                                                        undo changes |          `u`           |                                              |
|                                                                                                                     start characterwise Visual mode |          `v`           |                                              |
|                                                                                                                              cursor N words forward |          `w`           |                                              |
|                                                                                    delete N characters under and after the cursor [into register x] |        `["x]x`         |                                              |
|                                                                                                                   yank Nmove text [into register x] |    `["x]y{motion}`     |                                              |
|                                                                                                                      yank N lines [into register x] |        `["x]yy`        |                                              |
|                                                                                                             commands starting with 'z', see z below |       `z{char}`        |                                              |
|                                                                                                                        cursor N paragraphs backward |          `{`           |                                              |
|                                                                                                                                  cursor to column N |          `|`           |                                              |
|                                                                                                                         cursor N paragraphs forward |          `}`           |                                              |
|                                               'tildeop' off: switch case of N characters under cursor and move the cursor N characters to the right |          `~`           |                                              |
|                                                                                                             'tildeop' on: switch case of Nmove text |      `~{motion}`       |                                              |
|                                                                                                                                         same as "G" |       `<C-End>`        | x                                            |
|                                                                                                                                        same as "gg" |       `<C-Home>`       | x                                            |
|                                                                                                                                         same as "b" |       `<C-Left>`       | x                                            |
|                                                                                                             ":ta" to the keyword at the mouse click |    `<C-LeftMouse>`     |                                              |
|                                                                                                                                         same as "w" |      `<C-Right>`       | x                                            |
|                                                                                                                                    same as "CTRL-T" |    `<C-RightMouse>`    | x                                            |
|                                                                                                                                    same as "g<Tab>" |       `<C-Tab>`        | x                                            |
|                                                                                                                                         same as "x" |      `["x]<Del>`       | x                                            |
|                                                                                                                  remove the last digit from {count} |     `{count}<Del>`     |                                              |
|                                                                                                                                         same as "j" |        `<Down>`        | x                                            |
|                                                                                                                                         same as "$" |        `<End>`         | x                                            |
|                                                                                                                                      same as <Help> |         `<F1>`         | x                                            |
|                                                                                                                                  open a help window |        `<Help>`        |                                              |
|                                                                                                                                         same as "0" |        `<Home>`        | x                                            |
|                                                                                                                                         same as "i" |       `<Insert>`       | x                                            |
|                                                                                                                                         same as "h" |        `<Left>`        | x                                            |
|                                                                                                             move cursor to the mouse click position |     `<LeftMouse>`      |                                              |
|                                                                                                            same as "gP" at the mouse click position |    `<MiddleMouse>`     | x                                            |
|                                                                                                                                      same as CTRL-F |      `<PageDown>`      | x                                            |
|                                                                                                                                      same as CTRL-B |       `<PageUp>`       | x                                            |
|                                                                                                                                         same as "l" |       `<Right>`        | x                                            |
|                                                                                          start Visual mode, move cursor to the mouse click position |     `<RightMouse>`     |                                              |
|                                                                                                                                      same as CTRL-F |       `<S-Down>`       | x                                            |
|                                                                                                                                         same as "b" |       `<S-Left>`       | x                                            |
|                                                                                                             same as "*" at the mouse click position |    `<S-LeftMouse>`     | x                                            |
|                                                                                                                                         same as "w" |      `<S-Right>`       | x                                            |
|                                                                                                             same as "#" at the mouse click position |    `<S-RightMouse>`    | x                                            |
|                                                                                                                                      same as CTRL-B |        `<S-Up>`        | x                                            |
|                                                                                                                                         same as "u" |        `<Undo>`        | x                                            |
|                                                                                                                                         same as "k" |         `<Up>`         | x                                            |
|                                                                                                                        move window three lines down |  `<ScrollWheelDown>`   |                                              |
|                                                                                                                           move window one page down | `<S-ScrollWheelDown>`  |                                              |
|                                                                                                                          move window three lines up |   `<ScrollWheelUp>`    |                                              |
|                                                                                                                             move window one page up |  `<S-ScrollWheelUp>`   |                                              |
|                                                                                                                        move window six columns left |  `<ScrollWheelLeft>`   |                                              |
|                                                                                                                           move window one page left | `<S-ScrollWheelLeft>`  |                                              |
|                                                                                                                       move window six columns right |  `<ScrollWheelRight>`  |                                              |
|                                                                                                                          move window one page right | `<S-ScrollWheelRight>` |                                              |



