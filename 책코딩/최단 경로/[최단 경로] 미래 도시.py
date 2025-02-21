import heapq
import sys
input = sys.stdin.readline
INF = float('inf')
n, m = map(int, input().split())
graph = [[INF]*(n+1) for _ in range(n+1)]
for i in range(1, n+1):
    graph[i][i] = 0

for i in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

x, k = map(int, input().split())

for i in range(1, n+1):
    for j in range(1, n+1):
        for l in range(1, n+1):
            graph[j][l] = min(graph[j][l], graph[j][i]+graph[i][l])

distance = graph[1][k] + graph[k][x]

if distance == INF:
    print(-1)
else:
    print(distance)