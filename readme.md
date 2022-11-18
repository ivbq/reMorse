# reMorse

reMorse är ett språk med 8-bitars instruktioner och 32-bitars register som är skrivet likt ett assembly-språk i grunden, representerat som morsekod (eller punktskrift) i text- eller ljudform. Varje instruktion representeras internt av en 8-bitars binär sträng, vilket motsvarar 2 hexadecimala siffror i morseform.

## Konverteringstabell mellan register och deras binära representationer

| Register | Binärt |
|----------|--------|
| a        | 00     |
| b        | 01     |
| c        | 10     |
| d        | 11     |


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

Nedan är alla operationer, vad de gör och vad mer man behöver skriva efter operationen.

- 000 Input (inp)

    Input låter användaren skriva in ett tal i programmet som sedan sparas på en variabel. 
    Efter operationen skrivs vilken variabel man vill använda på 2 bitar, alltså 00-11. 


- 001 Output (out)

    Output skriver ut talet som är sparat på en viss variabel. 
    Efter operationen skrivs vilken variabel man vill använda på 2 bitar, alltså 00-11. 


- 010 End

    End stänger av programmet


- 011 Add/Sub

    Denna operation är lite speciell då den används för att både addera och subtrahera en variabel med en annan.
    Den fjärde biten avgör om den andra variabeln ska adderas (0) eller subtraheras (1). 
    På de 4 sista bitarna står vilka två varibler man vill använda där den första är den där svaret sparas på och alltid är positiv. 


- 100 Addi

    Addi adderar en variabel med en siffra som inte måste sparas på en variabel.
    Efter de 3 bitarna för operationen skrivs det in vilken variabel man vill använda och sedan vilken 
    siffra (i binär form) man vill addera variabeln med. siffran kan vara mellan 0 och 7.  


- 101 Subi

    Subi är likadan som Addi bara att variablen subtraheras med siffran istället för adderas. 


- 110 Jump (jmp)

    Jump hoppar mellan instruktioner i koden. 
    Den fjärde biten säger om man ska hoppa fram eller bak där 0 är positivt och hoppar alltså fram medan 1 är negativt och hoppar bak.
    De 4 sista bitarna står för hur långt man ska hoppa, mellan 0 och 15 vilket är det högsta man kan få med 4 binära tecken


- 111 If equal (jme)

    Denna operation kollar om en variabel är lika med en annan variabel eller siffra, om de är lika hoppar den över nästa instruktion (som ofta är en Jump). 
    Den fjärde biten säger om de sista 2 bitarna är en variabel eller siffra. 
    De 2 nästkommande bitarna säger vilken variabel man ska jämföra med. 
    De sista 2 bitarna är antingen en variabel eller en siffra mellan 0 och 3. 


- Kod exempel
    
    Om man vill addera 2 variabler kollar man först på operationens binära kod: 011 för add/sub. Sedan ser vi att vi måste ha en bit för addition eller subtration så vi lägger till en 0a för addition. Därefter lägger vi till binära koden för de olika variablerna. a + b skulle därmed se ut så här: 011 0 00 01 som skrivs om till 0110 0001 för att lättare översättas till hexadeciamal (6 1). Sist görs de hexadecimala tecknena om till morse kod (-.... .----).