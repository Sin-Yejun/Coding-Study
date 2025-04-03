import sys
input = sys.stdin.readline

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

dp = [[0]*m for _ in range(n)]
dp[0][0] = board[0][0]

# 첫 줄은 오른쪽으로만 진행 가능
for j in range(1, m):
    dp[0][j] = dp[0][j-1] + board[0][j]

for i in range(1, n):
    # 왼쪽→오른쪽 탐색
    left = [0]*m
    left[0] = dp[i-1][0] + board[i][0]
    for j in range(1, m):
        left[j] = max(left[j-1], dp[i-1][j]) + board[i][j]

    # 오른쪽→왼쪽 탐색
    right = [0]*m
    right[-1] = dp[i-1][-1] + board[i][-1]
    for j in range(m-2, -1, -1):
        right[j] = max(right[j+1], dp[i-1][j]) + board[i][j]

    # 둘 중 큰 값 선택
    for j in range(m):
        dp[i][j] = max(left[j], right[j])

print(dp[n-1][m-1])
