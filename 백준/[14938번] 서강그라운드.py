import sys, heapq
input = sys.stdin.readline

def dijstra(start):
    distance = [float('inf')]*(n+1)
    distance[start] = 0
    heap = [(0, start)]
    while heap:
        d, node = heapq.heappop(heap)
        for u, dis in graph[node]:
            D = d + dis
            if D < distance[u]:
                distance[u] = D
                heapq.heappush(heap,(D, u))
    items = 0
    for i in range(1, n+1):
        if distance[i] <= m:
            items += arr[i]
    return items
n, m, r = map(int, input().split())
arr = [0]+list(map(int,input().split()))

graph = [ [] for _ in range(n+1)]
for _ in range(r):
    a, b, l = map(int, input().split())
    graph[a].append((b, l))
    graph[b].append((a,l))
result = 0
for i in range(1, n+1):
    result = max(result, dijstra(i))
print(result)
