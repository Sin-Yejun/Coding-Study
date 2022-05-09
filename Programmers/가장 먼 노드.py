from collections import deque

def bfs(v, visited, connect):
    cnt = 0
    q = deque([[v,cnt]])
    while q:
        v, cnt = q.popleft()
        if visited[v] == -1:
            visited[v] = cnt
            cnt += 1
            for e in connect[v]:
                q.append([e,cnt])
                
def solution(n, edge):
    ans = 0
    connect = [[] for i in range(n+1)]
    visited = [-1] * (n+1)
    for v in edge:
        connect[v[0]].append(v[1])
        connect[v[1]].append(v[0])
    bfs(1, visited, connect)
    for i in visited:
        if i == max(visited):
            ans += 1
    return ans
    
    
            
            
                
