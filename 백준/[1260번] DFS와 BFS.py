from collections import deque

node, line, start = map(int,input().split())
graph = [[] for _ in range(node+1)]
for _ in range(line):
    a, b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
for i in graph:
    i.sort()
visited_BFS = [False] * (node+1)
visited_DFS = [False] * (node+1)
def BFS(v):
    q = deque()
    q.append(v)
    while q:
        x = q.popleft()
        if visited_BFS[x] == False:
            print(x, end = ' ')
            visited_BFS[x] = True
            for i in graph[x]:
                q.append(i)
def DFS(v):
    q = deque()
    q.append(v)
    while q:
        x = q.popleft()
        if visited_DFS[x] == False:
            print(x, end=' ')
            visited_DFS[x] = True
            for i in graph[x]:
                DFS(i)
DFS(start)
print()
BFS(start)
