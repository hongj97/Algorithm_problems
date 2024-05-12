import sys

n = int(sys.stdin.readline())
stack = []
for _ in range(n):
    num = list(map(int, sys.stdin.readline().split()))
    if num[0]==1:
        stack.append(num[1])
    elif num[0]==2:
        if len(stack) != 0:
            print(stack.pop())
            continue
        print(-1)
    elif num[0]==3:
        print(len(stack))
    elif num[0]==4:
        if len(stack) ==0:
            print(1)
            continue
        print(0)
    elif num[0]==5:
        if len(stack) !=0:
            print(stack[-1])
            continue
        print(-1)