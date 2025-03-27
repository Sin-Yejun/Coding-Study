import sys
input = sys.stdin.readline

def is_palindrome(s):
    n = len(s)
    dp = [[False]*n for _ in range(n)]
    for i in range(n):
        dp[i][i] = True
    
    for i in range(n-1):
        dp[i][i+1] = (s[i] == s[i+1])
    
    for length in range(3, n+1):
        for i in range(n-length+1):
            j = i+length-1
            dp[i][j] = (s[i]==s[j]) and dp[i+1][j-1]
    return dp

n = int(input())
arr = list(map(int, input().split()))
dp = is_palindrome(arr)
m = int(input())
for _ in range(m):
    a, b = map(int, input().split())
    if dp[a-1][b-1]:
        print(1)
    else:
        print(0)