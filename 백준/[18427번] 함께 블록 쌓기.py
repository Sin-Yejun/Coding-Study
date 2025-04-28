import sys
input = sys.stdin.readline

n, m, h = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

dp = [[0]*(h+1) for _ in range(n+1)]
dp[0][0] = 1

for i in range(1, n+1):
    for j in range(h+1):
        if dp[i-1][j]:  # 이전 학생까지 j를 만들 수 있었다면
            for block in arr[i-1]:
                if j + block <= h:
                    dp[i][j+block] = (dp[i][j+block]+dp[i-1][j]) % 10007
            
            dp[i][j] = (dp[i][j]+dp[i-1][j]) % 10007
print(dp[n][h])