def solution(n):
    if n < 2:
        return n
    dp = [0,1] + [0 for i in range(n-1)]
    for i in range(2,n+1):
        dp[i] = dp[i-2] + dp[i-1]
    return dp[-1] % 1234567
