n = int(input())

dp = [1,2]

if n <= 2:
    print(n)
else:
    for i in range(2, n):
        dp.append(dp[i-2] + dp[i-1])
    print(dp[-1]%10007)
    
