import math
n = 0
s = ""
t = ["", "", "", "the", "", "buffy", "slayer", "vampire"]

def main():
    s = input()
    if len(s) == 4:
        print("none")
    i = 0
    while i < len(s):
        s[i] = math.fmod((s[i] - 97 + t[len(s)][i] - 97), 26) + 97
        i += 1

if __name__ == "__main__":
    main()
