import math

def main():
    globals.s = input()
    if len(globals.s) == 4:
        print("none")
    i = 0
    while i < len(globals.s):
        globals.s[i] = math.fmod((globals.s[i] - 97 + globals.t[len(globals.s)][i] - 97), 26) + 97
        i += 1

class globals:
    n = 0
    s = ""
    t = ["", "", "", "the", "", "buffy", "slayer", "vampire"]

if __name__ == "__main__":
    main()