import sys
from collections import deque
input = sys.stdin.readline

# 벨만-포드 알고리즘
'''
INF = float('inf')
n,m = map(int, input().split())
edges = []
for _ in range(m):
    u, v, w = map(int, input().split())
    edges.append((u, v, w))

distances = [INF]*(n+1)
distances[1] = 0
for _ in range(n-1):
    for u, v, w in edges:
        if distances[u] != INF and distances[u] + w < distances[v]:
            distances[v] = distances[u] + w

negative_cycle = False
for u, v, w in edges:
    if distances[u] != INF and distances[u] + w < distances[v]:
        negative_cycle = True

if negative_cycle:
    print(-1)
else:
    for i in range(2, n+1):
        if distances[i] == INF:
            print(-1)
        else:
            print(distances[i])
'''
# SPFA 알고리즘
INF = float('inf')
n,m = map(int, input().split())
edges = [[] for _ in range(n+1)]
for _ in range(m):
    u, v, w = map(int, input().split())
    edges[u].append((v, w))
distances = [INF]*(n+1)
visited = [False] * (n+1)
count = [0] * (n + 1)
distances[1] = 0
q = deque([1])
visited[1] = True

negative_cycle = False
while q:
    u = q.popleft()
    visited[u] = False

    for v, w in edges[u]:
        if distances[u]+w < distances[v]:
            distances[v] = distances[u]+w
            if not visited[v]:
                q.append(v)
                visited[v] = True
                count[v] += 1
                if count[v] >= n:
                    negative_cycle = True
                    break
    if negative_cycle:
        break

if negative_cycle:
    print(-1)
else:
    for i in range(2, n+1):
        if distances[i] == INF:
            print(-1)
        else:
            print(distances[i])
