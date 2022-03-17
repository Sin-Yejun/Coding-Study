import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
c = int(input())

graph = [[] for _ in range(n+1)]
for _ in range(c):
    a, b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
visited = [False] *(n+1)
def BFS(v):
    q = deque()
    q.append(v)
    
    while q:
        x = q.popleft()
        if visited[x] == False:
            visited[x] = True
            for i in graph[x]:
                q.append(i)
for i in graph[1]:
    if visited[i] == False:
        BFS(i)
print(visited[2:].count(True))
