# 플로이드 위셜은 "모든 지점에서 다른 모든 지점까지의 최단 겨올를 모두 구해야 하는 경우" O(N^3)
# 4
# 7
# 1 2 4
# 1 4 6
# 2 1 3
# 2 3 7
# 3 1 5
# 3 4 4
# 4 3 2 
INF = int(1e9)

n = int(input())
m = int(input())

graph = [[INF]*(n+1) for _ in range(n+1)]

for a in range(1, n+1):
    graph[a][a] = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = c

for k in range(1, n+1): # 중간정점 k
    for a in range(1, n+1): # 출발정점 a
        for b in range(1, n+1): # 도착 정점 b
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

for i in range(1, n+1):
    for j in range(1, n+1):
        print(graph[i][j], end=' ')
    print()
