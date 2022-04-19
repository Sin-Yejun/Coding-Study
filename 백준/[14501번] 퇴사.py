# https://jrc-park.tistory.com/119
n = int(input())
T = []
P = []
for i in range(n):
    a, b = map(int,input().split())
    T.append(a)
    P.append(b)

dp = [0 for i in range(n+1)]

for i in range(n-1, -1, -1):
    if T[i]+i <= n:
        dp[i] = max(P[i] + dp[T[i]+i], dp[i+1])
    else:
        dp[i] = dp[i+1]

print(dp[0])
