import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline
n, m, r = map(int,input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    u, v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)
for g in graph:
    g.sort(reverse = True)
visit = [-1] * (n+1)
nodes_cnt = [0 for _ in range(n+1)]
cnt = [0]
def DFS(node):
    visit[node] = 0
    cnt[0] += 1
    nodes_cnt[node] = cnt[0]
    for i in graph[node]:
        if visit[i] == -1:
            DFS(i)
    
DFS(r)
[print(i) for i in nodes_cnt[1:]]
