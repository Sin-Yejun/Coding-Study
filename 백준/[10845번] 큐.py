from collections import deque
import sys
input = sys.stdin.readline
n = int(input())
q = deque()
for _ in range(n):
    cmd = list(map(str,input().split()))
    if len(cmd) == 2:
        cmd[1] = int(cmd[1])
    if cmd[0] == 'push':
        q.append(cmd[1])
    elif cmd[0] == 'pop':
        if q:
            print(q.popleft())
        else:
            print(-1)
    elif cmd[0] == 'front':
        if q:
            print(q[0])
        else:
            print(-1)
    elif cmd[0] == 'back':
        if q:
            print(q[-1])
        else:
            print(-1)
    elif cmd[0] == 'size':
        print(len(q))
    elif cmd[0] == 'empty':
        if q:
            print(0)
        else:
            print(1)
