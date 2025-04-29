n = int(input())
k = int(input())
dp = [[0]*(k+1) for _ in range(n+1)]

for i in range(n+1):
    dp[i][0] = 1

for i in range(1, n+1):
    for j in range(1, k+1):
        dp[i][j] = (dp[i-1][j] + dp[i-2][j-1]) % 1000000003

ans = (dp[n-1][k]+dp[n-3][k-1])%1000000003
print(ans)