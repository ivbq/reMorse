# Variables (2 bits)
# Operations (3 bits) 
# Immediates (2-3 bits)

# add(x, y): Add y to x
# jme(x, y): Skip next line if x = y
# jmp(x): Jump back x spaces

register = {'a': 0, 'b': 0, 'c': 0, 'd': 0}

def evaluate(command: str, debug: bool = False):
    """Evaluates statement, updates variables, and returns relative index of next statement to evaluate"""
    match command.split():
        case ["add", x, y]:
            xv, yv = int(register[x]), int(register[y]) if y in register else int(y)
            if debug: print(f"add {x} {y} -> {x} = {xv + yv}")
            register[x] = xv + yv
            return 1
        case ["sub", x, y]:
            xv, yv = int(register[x]), int(register[y]) if y in register else int(y)
            if debug: print(f"sub {x} {y} -> {x} = {xv - yv}")
            register[x] = xv - yv
            return 1
        case ["set", x, y]:
            yv = int(register[y]) if y in register else int(y)
            if debug: print(f"set {x} {y} -> {x} = {yv}")
            register[x] = yv
            return 1
        case ["jme", x, y]:
            xv, yv = int(register[x]), int(register[y]) if y in register else int(y)
            if debug: print(f"jme {x} {y} -> {xv == yv}")
            if xv == yv: return 2
            else: return 1
        case ["jmp", x]:
            xv = int(x)
            if debug: print(f"jmp {x}")
            return xv
        case ["inp"]:
            if debug: print(f"inp -> a = ",end="")
            register['a'] = input()
            return 1
        case ["out"]:
            if debug: print(f"out -> ",end="")
            print(register['a'])
            return 1
        case ["spause"]:
            input()
            return 1
        # Error handling
        case _:
            if debug: print(f"Line not evaluated")
            return 1

fn = input("File: ")
with open(fn, "r") as source:
    commands: list[str] = source.readlines()
    i: int = 0
    while i < len(commands): i += evaluate(commands[i])

