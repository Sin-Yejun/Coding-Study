import sys

def dp(a, b):
    dp = [1,1]
    cnt = 0
    for i in range(2,b+1):
        if dp[i-1]+dp[i-2] > b:
            break
        dp.append(dp[i-1]+dp[i-2])
    dp = dp[1:]
    for i in dp:
        if a <= i <= b:
            cnt += 1
    return cnt

while True:
    a , b = map(int, sys.stdin.readline().split())
    if a == 0 and b == 0:
        break
    print(dp(a,b))
    
