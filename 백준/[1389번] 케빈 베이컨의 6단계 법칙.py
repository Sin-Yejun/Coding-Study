from collections import deque


def bfs(x):
    visited = [-1]*(n+1)
    q = deque([x])
    visited[x] = 0
    while q:
        x = q.popleft()
        for i in edge[x]:
            if visited[i] == -1:
                q.append(i)
                visited[i] = visited[x]+1
    return sum(visited)

n, m = map(int, input().split())
edge = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    edge[a].append(b)
    edge[b].append(a)    

ans = [float('inf')]
q = deque()

for i in range(1, n+1):
    ans.append(bfs(i))

print(ans.index(min(ans)))
    
