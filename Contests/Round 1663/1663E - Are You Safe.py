import math
X = int(input())
times = 0
no = 0
while (times < X):
    if X == len(input()):
        times += 1
        if (times == X):
            if (no == 0):
                print("YES")
            else:
                print("NO")
    else:
        no = 1
        times += 1
        if (times == X):
            print("NO")
