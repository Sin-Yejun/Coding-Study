# https://devlibrary00108.tistory.com/683
import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
dp = arr[:]

for i in range(N):
    for j in range(i):
        if arr[j] > arr[i]:
            dp[i] = max(dp[i], dp[j] + arr[i])
print(max(dp))
