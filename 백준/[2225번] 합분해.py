n, k = map(int, input().split())
r = 1000000000
dp = [[0]*(n+1) for _ in range(k+1)]
# i: 개수, j: 합
for i in range(k+1):
    dp[i][0] = 1

for i in range(1, k+1):
    for j in range(1, n+1):
        dp[i][j] = (dp[i-1][j] + dp[i][j-1]) % r

print(dp[k][n])
