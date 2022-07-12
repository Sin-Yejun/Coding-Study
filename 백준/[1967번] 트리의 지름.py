import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
graph = [[] for i in range(n+1)]

for _ in range(n-1):
    x, y, w = map(int,input().split())
    graph[x].append([y,w])
    graph[y].append([x,w])

def BFS(node):
    arr = deque()
    arr.append(node)
    visited = [-1] * (n+1)
    visited[node] = 0
    _max = [0,0]
    while arr:
        x = arr.popleft()
        for e, w in graph[x]:
            if visited[e] == -1:
                visited[e] = visited[x] + w
                arr.append(e)
                if _max[0] < visited[e]:
                    _max = visited[e], e
    return _max

dis, node = BFS(1)
dis, node = BFS(node)
print(dis)
