# https://seongonion.tistory.com/69
import sys
input = sys.stdin.readline

from collections import deque
N, M = map(int,input().split())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

# BFS 방식
visited_BFS = [False]*(N+1)
def BFS(v):
    q = deque()
    q.append(v)

    while q:
        x = q.popleft()
        if visited_BFS[x] == False:
            visited_BFS[x] = True
            for i in graph[x]:
                q.append(i)

cnt = 0
for i in range(1, N+1):
    if visited_BFS[i] == False:
        BFS(i)
        cnt += 1

print(cnt)
'''
# DFS 방식
visited_DFS = [False]*(N+1)
    
def DFS(v):
    visited_DFS[v] = True
    for i in graph[v]:
        if visited_DFS[i] == False:
            DFS(i)

cnt = 0
for i in range(1, N+1):
    if visited_DFS[i] == False:
        DFS(i)
        cnt += 1

print(cnt)
'''
