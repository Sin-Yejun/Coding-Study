import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    n = int(input())
    dp = [0,1,2,4] + [0] * (n-3)
    if n <=3 :
        print(dp[n])
    else:
        for i in range(4, n+1):
            dp[i] = dp[i-1]+dp[i-2]+dp[i-3]
        print(dp[n])
        
    
