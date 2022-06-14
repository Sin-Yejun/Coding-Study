def solution(n):
    dp = [1, 2] + [0]*(n-2)
    for i in range(2, n):
        dp[i] = (dp[i-1] + dp[i-2]) % 1000000007
    return dp[-1]
