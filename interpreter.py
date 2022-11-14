# Variables (2 bits)
# Operations (3 bits) 
# Immediates (2-3 bits)

# add(x, y): Add y to x
# jme(x, y): Skip next line if x = y
# jmp(x): Jump back x spaces

#nummer -1 för array
#0 000 input                  3bit op + 2bit var                           5bit
#1 001 output                 3bit op + 2bit var                           5bit
#2 010 end                    3bit op                                      3bit
#3 011 add/sub (op+ /op-  ?)  3bit op + 1bit (+/-) + 2bit var  + 2bit var  8bit
#4 100 addi                   3bit op + 2bit var   + 5bit (32)             8bit
#5 101 subi                   3bit op + 2bit var   + 5bit (32)             8bit
#6 110 jmp                    3bit op + 1bit (+/-) + 4bit (16)             8bit
#7 111 jme                    3bit op + 2bit var   + 2bit var              7bit



register = {'a': 0, 'b': 0, 'c': 0, 'd': 0}
regBin = ['a', 'b', 'c', 'd']
opBin = ["inp", "out", "end", "add/sub", "addi", "subi", "jmp", "jme"]

#morse to hex to bin
morseDic = {"-----":'0', ".----":'1', "..---":'2', "...--":'3', "....-":'4', ".....":'5', "-....":'6', "--...":'7', "---..":'8', "----.":'9', ".-":'A', "-...":'B', "-.-.":'C', "-..":'D', ".":'E', "..-.":'F'}


def morseToBinary(a:str):
    x, y = a.split()
    deci = int(morseDic[x]+morseDic[y], 16)
    return format(deci, '0>8b')

morse = input()
binary = morseToBinary(morse)
print(binary)





def evaluate(command: str, debug: bool = False):
    """Evaluates statement, updates variables, and returns relative index of next statement to evaluate"""
    op = opBin[int(binary[:3],2)] #tar tre första talen i binary, gör om det till bas 10 och sätter in det i opReg
    rest = binary[5:]
    match op:
        case "add/sub":
            xv, yv = int(register[x]), int(register[y]) if y in register else int(y)
            if debug: print(f"add {x} {y} -> {x} = {xv + yv}")
            register[x] = xv + yv
            return 1
            #sub
            #xv, yv = int(register[x]), int(register[y]) if y in register else int(y)
            #if debug: print(f"sub {x} {y} -> {x} = {xv - yv}")
            #register[x] = xv - yv
            #return 1
        case "jme":
            xv, yv = int(register[x]), int(register[y]) if y in register else int(y)
            if debug: print(f"jme {x} {y} -> {xv == yv}")
            if xv == yv: return 2
            else: return 1
        case "jmp":
            xv = int(x)
            if debug: print(f"jmp {x}")
            return xv
        case "inp":
            if debug: print(f"inp -> {x} = ",end="")
            register[x] = input()
            return 1
        case "out":
            if debug: print(f"out -> ",end="")
            print(register[x])
            return 1
            
        case _:
            if debug: print(f"Line not evaluated")
            return 1

fn = input("File: ")
with open(fn, "r") as source:
    commands: list[str] = source.readlines()
    i: int = 0
    while i < len(commands): i += evaluate(commands[i])