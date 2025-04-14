import sys
input = sys.stdin.readline

n = int(input())
T = [0] *(n+2)
P = [0] *(n+2)
dp = [0] *(n+2)

for i in range(1, n+1):
    t, p = map(int, input().split())
    T[i] = t 
    P[i] = p 

for i in range(1, n+1):

    dp[i+1] = max(dp[i+1], dp[i])

    if i + T[i] <= n+1:
        dp[i+T[i]] = max(dp[i+T[i]], dp[i]+P[i])

print(max(dp))