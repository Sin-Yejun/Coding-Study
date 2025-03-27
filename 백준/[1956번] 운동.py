import sys
input = sys.stdin.readline
n, m = map(int, input().split())
INF = float('inf')
arr = [[INF]*(n+1) for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    arr[a][b] = c


for k in range(1, n+1):
    for a in range(1, n+1):
        if arr[a][k] == INF:
            continue
        for b in range(1, n+1):
            if arr[k][b] == INF:
                continue
            arr[a][b] = min(arr[a][b], arr[a][k]+arr[k][b])

min_val = INF
for i in range(1, n):
    min_val = min(min_val, arr[i][i])

if min_val == INF:
    print(-1)
else:
    print(min_val)
