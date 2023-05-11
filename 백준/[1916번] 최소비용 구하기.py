import sys, heapq
from collections import defaultdict
input = sys.stdin.readline

def dijkstra(start):
    distance[start] = 0
    arr = [(0, start)]
    while arr:
        dis, now = heapq.heappop(arr)
        for node, weight in graph[now]:
            d = dis + weight
            if d < distance[node]:
                distance[node] = d
                heapq.heappush(arr, (d,node))
    return distance[end]
                
n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
distance = [float('inf')]*(n+1)
d = defaultdict(int)
for _ in range(m):
    u, v, e = map(int, input().split())
    if str(u)+str(v) not in d:
        d[str(u)+str(v)] = e
        graph[u].append([v,e])
    elif d[str(u)+str(v)] > e:
        for i in range(len(graph[u])):
            if graph[u][i][0] == v:
                graph[u][i][1] = e
                d[str(u)+str(v)] = e
               
start, end = map(int, input().split())
print(dijkstra(start))
        
    
    
