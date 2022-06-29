n = int(input())
dp = [0, 1,1,1] + [0]*97

for i in range(4, 101):
    dp[i] = dp[i-3]+dp[i-2]

for i in range(n):
    print(dp[int(input())])

