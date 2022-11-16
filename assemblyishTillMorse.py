morseToBraille = {"-----": '⠁', ".----": '⠃', "..---": '⠉', "...--": '⠙', "....-": '⠑', ".....": '⠋', "-....": '⠛', "--...": '⠓', "---..": '⠊', "----.": '⠚', ".-": '⠅', "-...": '⠇', "-.-.": '⠍', "-..": '⠝', ".": '⠕', "..-.": '⠏'}
binToMorse = {'0000': "-----", '0001': ".----", '0010': "..---", '0011': "...--", '0100': "....-", '0101': ".....", '0110': "-....", '0111': "--...", '1000': "---..", '1001': "----.", '1010': ".-", '1011': "-...", '1100': "-.-.", '1101': "-..", '1110': ".", '1111': "..-.", 'skip':""}
varToBin = {'a': "00", 'b': "01", 'c': "10", 'd': "11"}

def toMorse(command, braille = False):
    match command.split():
        case ["inp", x]:
            binary = "000" + varToBin[x] + "000"
        case ["out", x]:
            binary = "001" + varToBin[x] + "000"
        case ["end"]:
            binary = "01000000"
        case ["add", x, y]:
            binary = "0110" + varToBin[x] + varToBin[y]
        case ["sub", x, y]:
            binary = "0111" + varToBin[x] + varToBin[y]
        case ["addi", x, y]:
            if int(y) > (2**3 - 1): print("Warning: addi can only take input up to 2^3-1 (15). Input will be truncated.")
            binary = "100" + varToBin[x] + format(int(y), '0>3b')
        case ["subi", x, y]:
            binary = "101" + varToBin[x] + format(int(y), '0>3b')
        case ["jmp", x]:
            binary = "110"
            if int(x) < 0: binary += '1' + format(-int(x), '0>4b')
            else: binary += '0' + format(int(x), '0>4b')
        case ["jme", x, y]: #help
            binary = "111"
            if y in varToBin: binary += '1' + varToBin[x] + varToBin[y]
            else: binary += '0' + varToBin[x] + format(int(y), '0>2b')
        case _:
            binary = "skipskip"
    com1 = binToMorse[binary[:4]]
    com2 = binToMorse[binary[4:]]
    if braille:
        com1 = morseToBraille[com1]
        com2 = morseToBraille[com2]
    morse = com1 + ' ' + com2
    print(morse + " ", end="")

with open("examples/fac.txt", "r") as source:
    commands: list[str] = source.readlines()
    print()
    for line in commands:
        toMorse(line, braille = True)
    print()
    print()