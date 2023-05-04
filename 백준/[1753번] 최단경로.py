import heapq
import sys
input = sys.stdin.readline

def dijkstra(start):
    q = [(0, start)]
    distance[start] = 0
    while q:
        dis, now = heapq.heappop(q)
        for node, weight in edge[now]:
            d = dis + weight
            if d < distance[node]:
                distance[node] = d
                heapq.heappush(q, (d, node))

  
V, E = map(int, input().split())
start = int(input())
edge = [[] for _ in range(V+1)]
distance = [float('inf')]*(V+1)
for _ in range(E):
    u, v, e = map(int, input().split())
    edge[u].append((v,e))
dijkstra(start)
for i in range(1, V+1):
    if distance[i] == float('inf'):
        print('INF')
    else:
        print(distance[i])

'''
from collections import deque
import sys
input = sys.stdin.readline

def dijkstra(start):
    q = deque([start])
    distance[start] = 0
    while q:
        c = q.popleft()
        heapq.heapify(edge[c].sort(key = lambda x:x[1])
        for node, weight in edge[c]:
            d = distance[c] + weight
            if d < distance[node]:
                distance[node] = d
                q.append(node)

  
V, E = map(int, input().split())
start = int(input())
edge = [[] for _ in range(E+1)]
distance = [float('inf')]*(V+1)
for _ in range(E):
    u, v, e = map(int, input().split())
    edge[u].append((v,e))
dijkstra(start)
for i in range(1, V+1):
    if distance[i] == float('inf'):
        print('INF')
    else:
        print(distance[i])
'''
