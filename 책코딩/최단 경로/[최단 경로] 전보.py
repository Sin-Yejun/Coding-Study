import heapq
import sys
input = sys.stdin.readline
INF = float('inf')
n, m, c = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    x, y, z = map(int, input().split())
    graph[x].append((y, z))

distance = [INF]*(n+1)

q = []
distance[c] = 0
heapq.heappush(q, (0, c))
while q:
    dist, now = heapq.heappop(q)
    for i in graph[now]:
        cost = dist + i[1]
        if cost < distance[i[0]]:
            distance[i[0]] = cost
            heapq.heappush(q, (cost, i[0]))
tot_city, tot_time = 0, 0
for i in distance:
    if i != 0 and i != INF:
        tot_city += 1
        tot_time = max(tot_time, i)
print(tot_city, tot_time)