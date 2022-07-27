n = int(input())
dp = [1,2]
if n > 2:
    for i in range(2, n):
        dp.append((dp[i-2]+dp[i-1])%15746)
    print(dp[-1])
else:
    print(dp[n-1])
