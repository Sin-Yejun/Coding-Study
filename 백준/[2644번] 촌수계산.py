import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
x, y = map(int,input().split())
m = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
#print(graph)

q = deque()
q.append([x,0])
Flag = False
while q:
    #print(q)
    X, ct = q.popleft()
    if X == y:
        Flag = True
        print(ct)
        break
    ct += 1
    for i in graph[X][::-1]:
        graph[X].pop()
        q.append([i,ct])
if not Flag:
    print(-1)
        
