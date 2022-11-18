# reMorse

reMorse är ett språk med 8-bitars instruktioner och 32-bitars register som är skrivet likt ett assembly-språk i grunden, representerat som morsekod (eller punktskrift) i text- eller ljudform. Varje instruktion representeras internt av en 8-bitars binär sträng, vilket motsvarar 2 hexadecimala siffror i morseform.

## Instruktioner

- 000 Input (inp): Input är en instruktion som tar in en integer från IO och sparar den i given variabel.
- 001 Output (out): Output är en instruktion som tar in ett register och skriver ut värdet i IO.
- 010 End: End är en instruktion som sätter nästa instruktion till slutet av programmet.
- 011 Add/sub: Add/sub är en instruktion som tar in två register x och y och sparar värdet av (x + y) eller (x - y) i register x, beroende på om den 4:e biten är 0 (add) eller 1 (sub).
- 100 Addi: Addi är en instruktion som tar in ett register x och en immediate imm mellan 0 och 2^3 - 1 och sparar värdet av (x + imm) i x.
- 101 Subi: Subi är en instruktion som tar in ett register x och en immediate imm mellan 0 och 2^3 - 1 och sparar värdet av (x - imm) i x.
- 110 Jump (jmp): Jump är en instruktion som tar in en immediate imm mellan 0 och 2^4 - 1 och sätter nästa instruktion till (nuvarande + imm) eller (nuvarande - imm), beroende på om den 4:e biten är 0 (add) eller 1 (sub).
- 111 If equal (jme): If equal är en instruktion som tar in ett register och ett register/immediate mellan 0 och 2^2 - 1, beroende på om den 4:e biten är 0 (add) eller 1 (sub), och hoppar över nästa instruktion om de har samma värde.

- Kod exempel
    
    Om man vill addera 2 variabler kollar man först på operationens binära kod: 011 för add/sub. Sedan ser vi att vi måste ha en bit för addition eller subtration så vi lägger till en 0a för addition. Därefter lägger vi till binära koden för de olika variablerna. a + b skulle därmed se ut så här: 011 0 00 01 som skrivs om till 0110 0001 för att lättare översättas till hexadeciamal (6 1). Sist görs de hexadecimala tecknena om till morse kod (-.... .----).

## Konverteringstabell mellan register och deras binära representationer

| Register | Kod |
|----------|-----|
| a        | 00  |
| b        | 01  |
| c        | 10  |
| d        | 11  |


## Konverteringstabell mellan instruktioner och dess binära representationer

| Bitar | Kod  | Namn    | 1   | 2   | 3   | 4   | 5   | 6   | 7   | 8   |
|-------|------|---------|-----|-----|-----|-----|-----|-----|-----|-----|
| 5     | 000  | inp     | op  | op  | op  | var | var |     |     |     |
| 5     | 001  | out     | op  | op  | op  | var | var |     |     |     |
| 3     | 010  | end     | op  | op  | op  |     |     |     |     |     |
| 8     | 011  | add/sub | op  | op  | op  | sgn | var | var | var | var |
| 8     | 100  | addi    | op  | op  | op  | var | var | imm | imm | imm |
| 8     | 101  | subi    | op  | op  | op  | var | var | imm | imm | imm |
| 8     | 110  | jmp     | op  | op  | op  | sgn | imm | imm | imm | imm |
| 8     | 111  | jme     | op  | op  | op  | i/v | var | var | i/v | i/v |