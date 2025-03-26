import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    n = int(input())
    parents = [-1]*(n+1)
    for _ in range(n-1):
        a, b = map(int, input().split())
        parents[b] = a
    x, y = map(int, input().split())

    cur = x
    temp1 = [x]
    while cur != -1:
        temp1.append(cur)
        cur = parents[cur]

    temp2 = [y]
    cur = y
    while cur != -1:
        temp2.append(cur)
        cur = parents[cur]

    for i in temp1:
        if i in temp2:
            print(i)
            break