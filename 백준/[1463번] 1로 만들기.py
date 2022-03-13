# https://jae04099.tistory.com/entry/%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EB%B0%B1%EC%A4%80-1463-1%EB%A1%9C-%EB%A7%8C%EB%93%A4%EA%B8%B0
n = int(input())

dp = [0]*(n+1)

for i in range(2, n+1):
    dp[i] = dp[i-1]+1
    if i%3 == 0:
        dp[i] = min(dp[i], dp[i//3] +1)
    if i%2 == 0:
        dp[i] = min(dp[i], dp[i//2] +1)

print(dp[n])
