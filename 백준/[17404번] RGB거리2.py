import sys
input = sys.stdin.readline

n = int(input())
rgbs = [list(map(int, input().split())) for _ in range(n)]
INF = float('inf')
ans = INF

for first_color in range(3):  # R(0), G(1), B(2)
    dp = [[INF]*3 for _ in range(n)]
    dp[0][first_color] = rgbs[0][first_color]

    for i in range(1, n):
        dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + rgbs[i][0]
        dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + rgbs[i][1]
        dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + rgbs[i][2]

    # 마지막 집의 색은 첫 번째 집과 달라야 함
    for last_color in range(3):
        if last_color != first_color:
            ans = min(ans, dp[n-1][last_color])

print(ans)
