import sys
input = sys.stdin.readline

def floyd_warshall(graph):
    dist = graph.copy()

    # 모든 노드 쌍간의 최단경로를 구하는 알고리즘
    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    # 여전히 무한대로 남아있는 것을 0으로 바꿔준다. (문제에 그렇게 하라고 나와있다)     
    for i in range(n):
        for j in range(n):
            if dist[i][j] == float('inf'):
                dist[i][j] = 0
    return dist


n = int(input())
m = int(input())
graph = [[float('inf')]*(n) for _ in range(n)]
for i in range(n):
    graph[i][i] = 0

# graph 만드는 작업    
for _ in range(m):
    u, v, e = map(int, input().split())
    if e < graph[u-1][v-1]:
        graph[u-1][v-1] = e

# 출력 작업
for arr in floyd_warshall(graph):
    print(' '.join(map(str,arr)))


