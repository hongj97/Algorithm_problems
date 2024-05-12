import sys
from collections import deque

n = int(sys.stdin.readline())

que = deque()
for _ in range(n):
    option = sys.stdin.readline().split()
    if option[0]=='push':
        que.append(int(option[1]))
    elif option[0]=='pop':
        if len(que)==0:
            print(-1)
            continue
        print(que.popleft())
    elif option[0]=='size':
        print(len(que))
    elif option[0]=='empty':
        if len(que)==0:
            print(1)
            continue
        print(0)
    elif option[0]=='front':
        if len(que)==0:
            print(-1)
            continue
        print(que[0])
    elif option[0]=='back':
        if len(que)==0:
            print(-1)
            continue
        print(que[-1])