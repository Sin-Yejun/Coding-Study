# https://leetcode.com/problems/count-and-say/discuss/155690/38-count-and-say-solution-in-c-java-python
class Solution:
    def countAndSay(self, n: int) -> str:
        dp = []
        dp.append("1") # initial string
        for i in range(1, n):
            lenLast = len(dp[i-1])
            cur = ""
            j = 0
            while j < lenLast:
                k = j
                while k < lenLast - 1 and dp[i-1][k] == dp[i-1][k+1]: 
                    k += 1
                cur += str(k-j+1) # append letter times
                cur += dp[i-1][j] # append letter itself
                j = k + 1
            dp.append(cur)
        return dp[n-1]
