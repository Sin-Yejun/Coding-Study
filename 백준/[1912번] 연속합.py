n = int(input())
arr = list(map(int,input().split()))

dp = [0] * n

for i in range(len(arr)):
    dp[i] = max(arr[i], dp[i-1]+arr[i])
print(max(dp))
