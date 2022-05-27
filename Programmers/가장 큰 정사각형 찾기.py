def solution(board):
    n = len(board)
    m = len(board[0])
    dp = board[:]
    for i in range(1, n):
        for j in range(1,m):
            if dp[i][j] == 1:
                dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
    Max = 0
    for arr in dp:
        Max = max(Max, max(arr))
    return Max**2
