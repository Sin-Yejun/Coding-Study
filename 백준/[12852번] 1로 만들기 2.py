import sys

n = int(sys.stdin.readline())
dp = [[0, []] for _ in range( n+1)]
dp[1][0] = 0
dp[1][1] = [1]
for x in range(2, n+1):
    dp[x][0] = dp[x-1][0] + 1
    dp[x][1] = dp[x-1][1] + [x]
    
    if (x % 2 == 0):
        # f(x//2) + 1과 기존 DP 테이블의 값을 비교해, 최솟값으로 변환
        if (dp[x][0] > dp[x//2][0] + 1):
            dp[x][0] = dp[x//2][0] + 1
            dp[x][1] = dp[x//2][1] + [x]

    # 이후, x가 3으로 나눠지는 경우, 
    if (x % 3 == 0):
        # f(x//3) + 1과 기존 DP 테이블의 값을 비교해, 최솟값으로 변환
        if (dp[x][0] > dp[x//3][0] + 1):
            dp[x][0] = dp[x//3][0] + 1
            dp[x][1] = dp[x//3][1] + [x]

# x를 만드는 최소 연산의 수
print(dp[n][0])
# x를 최소 연산으로 만드는 방법
for i in dp[n][1][::-1]:
    print(i, end=" ")

