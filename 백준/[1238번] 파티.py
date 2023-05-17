import sys, heapq
input = sys.stdin.readline

def dijkstra(start, end):
    distance = [float('inf')]*(n+1)
    heap = [(0, start)]
    distance[start] = 0
    while heap:
        d, node = heapq.heappop(heap)
        for u, w in graph[node]:
            dis = d + w
            if dis < distance[u]:
                distance[u] = dis
                heapq.heappush(heap, (dis, u))
    return distance[end]

n, m, x = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b,c))

_max =0
for i in range(1, n+1):
    val = dijkstra(i, x) + dijkstra(x, i)
    if _max < val:
        _max = val
print(_max)
        
