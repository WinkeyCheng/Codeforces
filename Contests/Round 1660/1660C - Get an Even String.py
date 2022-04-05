def solve():
    s = input()
    X = set()
    res = 0
    i = 0
    while i < len(s):
        if X.count(s[i]):
            res += 2
            X.clear()
        else:
            X.insert(s[i])
        i += 1
    print(int(len(s)) - res)

def main():
    T = input()
    T = int(T)
    while T != 0:
        T -= 1
        solve()
    T -= 1

if __name__ == "__main__":
    main()
