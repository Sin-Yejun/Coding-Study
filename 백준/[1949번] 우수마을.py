import sys
from collections import defaultdict
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
n = int(input())
people = [0] + list(map(int, input().split()))
tree = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

# (dp[x][0] : x마을 선택 X / dp[x][1] : x마을 선택 O)
dp = [[0]*2 for _ in range(n+1)]
visited = [False]*(n+1)

def dfs(x):
    visited[x] = True
    dp[x][0] = 0
    dp[x][1] = people[x]

    for y in tree[x]:
        if not visited[y]:
            dfs(y)
            dp[x][0] += max(dp[y][0], dp[y][1])
            dp[x][1] += dp[y][0]
dfs(1)
print(max(dp[1][0], dp[1][1]))