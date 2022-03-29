# https://kangeee.tistory.com/123?category=962337
n = int(input())
dp = [0] * 100001

dp[1] = 1
dp[2] = 1
dp[3] = 2
dp[4] = 2
dp[5] = 1
dp[6] = 2
dp[7] = 1
if n > 7:
    for i in range(8, n+1):
        if i%7 == 0:
            dp[i] = i//7
        else:
            dp[i] = min(dp[i-7], dp[i-5], dp[i-2], dp[i-1])+1
print(dp[n])
