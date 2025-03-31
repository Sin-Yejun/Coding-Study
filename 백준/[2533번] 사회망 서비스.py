import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(node, parent):
    dp[node][0] = 0 # node 선택 안했을 때
    dp[node][1] = 1 # node 선택 했을 때

    for child in graph[node]:
        if child == parent:
            continue
        dfs(child, node)
        dp[node][0] += dp[child][1]
        dp[node][1] += min(dp[child][0], dp[child][1])


n = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
dp = [[0, 0] for _ in range(n+1)]
dfs(1, -1)
print(min(dp[1][0], dp[1][1]))
    