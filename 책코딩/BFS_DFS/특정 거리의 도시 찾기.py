import sys
from collections import deque   
input = sys.stdin.readline
n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
q = deque([x])
distance = [-1]*(n+1)
distance[x] = 0
while q:
    x = q.popleft()
    for i in graph[x]:
        if distance[i] == -1:
            distance[i] = distance[x] + 1
            q.append(i)
check = True
for i in range(len(distance)):
    if distance[i] == k:
        print(i)
        check = False
if check:
    print(-1)

    