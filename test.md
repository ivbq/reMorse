| Bits | Code | Name    | 1   | 2   | 3   | 4   | 5   | 6   | 7   | 8   |
|------|------|---------|-----|-----|-----|-----|-----|-----|-----|-----|
| 5bit | 000  | input   | op  | op  | op  | var | var |     |     |     |
| 5bit | 001  | output  | op  | op  | op  | var | var |     |     |     |
| 3bit | 010  | end     | op  | op  | op  |     |     |     |     |     |
| 8bit | 011  | add/sub | op  | op  | op  | sgn | var | var | var | var |
| 8bit | 100  | addi    | op  | op  | op  | var | var | imm | imm | imm |
| 8bit | 101  | subi    | op  | op  | op  | var | var | imm | imm | imm |
| 8bit | 110  | jump    | op  | op  | op  | sgn | imm | imm | imm | imm |
| 8bit | 111  | ifeq    | op  | op  | op  | i/v | var | var | v/i | v/i |