import sys
from collections import deque
input = sys.stdin.readline

n, m, r = map(int,input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    u, v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)
for g in graph:
    g.sort(reverse = True)

visited = [0] * (n+1)
cnt = 1

def BFS(start):
    global cnt
    arr = deque([start])
    visited[start] = cnt
    while arr:
        x = arr.popleft()
        visited[x] = cnt
        cnt += 1
        for i in graph[x]:
            if visited[i] == 0:
                arr.append(i)
                visited[i] = cnt
BFS(r)
          
[print(i) for i in visited[1:]]
