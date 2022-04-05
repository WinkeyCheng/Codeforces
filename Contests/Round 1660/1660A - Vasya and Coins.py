def solve():
    x = 0
    y = 0
    x, y = input().split()
    x, y = [int(x), int(y)]
    if (x == 0):
        print(1)
    else:
        print(x + y * 2 + 1)

def main():
    T = 0
    T = input()
    T = int(T)
    while T != 0:
        T -= 1
        solve()
    T -= 1

if __name__ == "__main__":
    main()
