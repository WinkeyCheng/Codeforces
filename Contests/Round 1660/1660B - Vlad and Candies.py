def solve():
    n = 0
    n = input()
    n = int(n)
    a = [int(_) for _ in input().split()]
    a.sort()
    if n == 1:
        if a[0] <= 1:
            print("YES")
        else:
            print("NO")  
    else:
        if a[n - 1] - a[n - 2] <= 1:
            print("YES")
        else:
            print("NO")

def main():
    T = input()
    T = int(T)
    while T != 0:
        T -= 1
        solve()
    T -= 1

if __name__ == "__main__":
    main()
