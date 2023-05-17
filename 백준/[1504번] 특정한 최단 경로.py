import sys, heapq
input = sys.stdin.readline

def dijkstra(s, z):
    distance = [float('inf')]*(n+1)
    distance[s] = 0
    heap = [(0, s)]
    while heap:
        dis , nod = heapq.heappop(heap)
        
        for u, w in graph[nod]:
            d = dis + w
            if d < distance[u]:
                distance[u] = d
                heapq.heappush(heap, (d, u))
    return distance[z]

n, e = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))
start, end = map(int, input().split())

S1 = dijkstra(1, start)+dijkstra(start, end) + dijkstra(end, n)
S2 = dijkstra(1, end)+dijkstra(end, start) + dijkstra(start, n)
ans = min(S1, S2)
if ans == float('inf'):
    print(-1)
else:
    print(ans)
