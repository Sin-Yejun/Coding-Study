from collections import deque
n, k = map(int,input().split())
q = deque([i for i in range(1, n+1)])
arr = list(map(int,input().split()))

cnt = 0
for i in arr:
    while q[0] != i:
        if q.index(i) < len(q)-q.index(i):
            q.rotate(-1)
            cnt += 1
        else:
            q.rotate(1)
            cnt += 1
    else:
        q.popleft()
print(cnt)
