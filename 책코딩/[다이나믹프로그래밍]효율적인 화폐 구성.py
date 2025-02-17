n, m = map(int, input().split())
coins = []
dp = [10001]*(m+1)
for _ in range(n):
    coins.append(int(input()))
dp[0] = 0
for i in range(n):
    for j in range(coins[i], m+1):
        if dp[j-coins[i]] != 10001:
            dp[j] = min(dp[j], dp[j-coins[i]]+1)

if dp[m] == 10001:
    print(-1)
else:
    print(dp[m])