from morse_audio_decoder.morse import MorseCode

# Variables (2 bits)
# Operations (3 bits) 
# Immediates (2-3 bits)

# add(x, y): Add y to x
# jme(x, y): Skip next line if x = y
# jmp(x): Jump back x spaces

#nummer -1 för array          när det är (x/y) är x = 0 och y = 1
#0 000 input                  3bit op + 2bit var                               5bit
#1 001 output                 3bit op + 2bit var                               5bit
#2 010 end                    3bit op                                          3bit
#3 011 add/sub (op+ /op-  ?)  3bit op + 1bit (+/-)     + 2bit var  + 2bit var  8bit
#4 100 addi                   3bit op + 2bit var       + 3bit (7)              8bit
#5 101 subi                   3bit op + 2bit var       + 3bit (7)              8bit
#6 110 jmp                    3bit op + 1bit (+/-)     + 4bit (15)             8bit
#7 111 jme                    3bit op + 1bit (imm/var) + 2bit var  + 2bit      8bit

register = {'a': 0, 'b': 0, 'c': 0, 'd': 0}
regBin = ['a', 'b', 'c', 'd']
opBin = ["inp", "out", "end", "add/sub", "addi", "subi", "jmp", "jme"]

#morse to hex to bin
morseToHex = {"-----": '0', ".----": '1', "..---": '2', "...--": '3', "....-": '4', ".....": '5', "-....": '6', "--...": '7', "---..": '8', "----.": '9', ".-": 'A', "-...": 'B', "-.-.": 'C', "-..": 'D', ".": 'E', "..-.": 'F'}
hexToMorse = {'0': "-----", '1': ".----", '2': "..---", '3': "...--", '4': "....-", '5': ".....", '6': "-....", '7': "--...", '8': "---..", '9': "----.", 'A': ".-", 'B': "-...", 'C': "-.-.", 'D': "-..", 'E': ".", 'F': "..-."}
brailleToMorse = {'⠁': "-----", '⠃': ".----", '⠉': "..---", '⠙': "...--", '⠑': "....-", '⠋': ".....", '⠛': "-....", '⠓': "--...", '⠊': "---..", '⠚': "----.", '⠅': ".-", '⠇': "-...", '⠍': "-.-.", '⠝': "-..", '⠕': ".", '⠏': "..-."}
#⠁⠃⠉⠙⠑⠋⠛⠓⠊⠚⠅⠇⠍⠝⠕⠏

def audioToMorse(fn: str):
    """Converts from hexadecimal morse code in audio to binary morse code in string form"""
    morse: MorseCode = MorseCode.from_wavfile(fn)
    hexBytes: str = morse.decode()

    n = 0
    while n < len(hexBytes):
        binX, binY = format(int(hexBytes[n], 16), '0>4b'), format(int(hexBytes[n + 1], 16), '0>4b')
        instructions.append(binX + binY)
        n += 2

    return instructions
    
def morseToBinary(a: str):
    """Converts from binary morse code in text form to a binary string"""
    x, y = a.split()
    binX, binY = format(int(morseToHex[x], 16), '0>4b'), format(int(morseToHex[y], 16), '0>4b')
    return binX + binY

def evaluate(binary: str, debug: bool = False):
    """Evaluates statement, updates variables, and returns relative index of next statement to evaluate"""
    
    op = opBin[int(binary[:3],2)] #tar tre första talen i binary, gör om det till bas 10 och sätter in det i opReg

    match op:
        case "inp": #måste vara int
            x = regBin[int(binary[3:5], 2)]
            register[x] = int(input())
            return 1
        case "out":
            x = regBin[int(binary[3:5], 2)]
            if debug: print(f"out {x} -> ",end="")
            print(register[x])
            return 1
        case "end": #good enough
            return 1000000 
        case "add/sub":
            x = regBin[int(binary[4:6], 2)]
            y = regBin[int(binary[6:], 2)]
            if binary[3] == '1': 
                if debug: print(f"sub {x} ({register[x]}) - {y} ({register[y]})")
                register[x] -= register[y]
            else: 
                if debug: print(f"add {x} + {y}")
                register[x] += register[y]
            return 1
        case "addi":
            x = regBin[int(binary[3:5], 2)]
            y = int(binary[5:], 2)
            register[x] += y
            if debug: print(f"addi {x} + {y}")
            return 1
        case "subi":
            x = regBin[int(binary[3:5], 2)]
            y = int(binary[5:],2)
            register[x] -= y
            if debug: print(f"subbi {x} - {y}")
            return 1
        case "jmp": #check så att i inte blir negativt
            x = int(binary[4:], 2)
            if binary[3] == '1': x = -x
            if debug: print(f"jmp {x}")
            return x
        case "jme":
            x = register[regBin[int(binary[4:6],2)]]
            y = int(binary[6:], 2)
            if binary[3] == '1': y = register[regBin[y]] #variabel
            if x == y:
                if debug: 
                    print(f"equal: {x} och {y}")
                    input()
                return 2
            else: 
                if debug: 
                    print(f"not equal: {x} och {y}")
                    input()
                return 1
        case _:
            if debug: print(f"Line not evaluated")
            return 1

# Reads file and interprets instructions
error = False
braille = False
fn = input("File: ")
if fn[-3:] == "txt":
    with open(fn, "r") as source:
        commands: list[str] = source.read().split()
        instructions: list[str] = []
        
        if commands[0] in brailleToMorse: braille = True

        if len(commands)%2 != 0:
            print("Error: Needs to be an even number of morse code commands\n")
            error = True
        else:
            i: int = 0
            while i < len(commands):
                if commands[i] not in morseToHex:
                    print("Error: Unknown command: " + commands[i] + f" at command number {i+1}\n       accepted commands are morse code equivalents of 0-9 and A-F\n")
                    error = True
                    break
                elif commands[i+1] not in morseToHex:
                    print("Error: Unknown command: " + commands[i+1] + f" at command number{i+2}\n       accepted commands are morse code equivalents of 0-9 and A-F\n")
                    error = True
                    break
                else:
                    if braille: 
                        commands[i] = brailleToMorse[commands[i]]
                        commands[i+1] = brailleToMorse[commands[i+1]]
                    instructions.append(morseToBinary(commands[i] + " " + commands[i + 1]))
                    i += 2
                
        if not error:
            j: int = 0
            while j < len(instructions):
                if j < 0: j = 0
                j += evaluate(instructions[j])
                
elif fn[-3:] == "wav":
    instructions: list[str] = []
    instructions = audioToMorse(fn)

    j: int = 0
    while j < len(instructions):
        if j < 0: j = 0
        j += evaluate(instructions[j])