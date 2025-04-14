import sys
input = sys.stdin.readline

T, W = map(int, input().split())
arr = [int(input()) for _ in range(T)]
dp = [[0]*(W+1) for _ in range(T+1)]

for i in range(1, T+1):
    for j in range(W+1):
        current_tree = arr[i-1]
        if j == 0:
            dp[i][j] = dp[i-1][j] + (1 if current_tree == 1 else 0)
        else:
            if current_tree == (j%2) + 1:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-1]) + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-1])

print(max(dp[T]))