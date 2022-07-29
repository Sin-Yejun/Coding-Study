# https://hongcoding.tistory.com/50
import sys
input = sys.stdin.readline
N, K = map(int, input().split())

items = [[0, 0]]
d = [[0]*(K+1) for _ in range(N+1)]

for i in range(N):
    items.append(list(map(int,input().split())))

for i in range(1, N+1):
    for j in range(1, K+1):
        w = items[i][0]
        v = items[i][1]

        if j < w:
            d[i][j] = d[i-1][j]
        else:
            d[i][j] = max(d[i-1][j], d[i-1][j-w]+v)
print(d[N][K])
    
