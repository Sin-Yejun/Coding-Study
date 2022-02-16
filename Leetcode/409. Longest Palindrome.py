class Solution:
    def longestPalindrome(self, s: str) -> int:
        d = {}
        for i in s:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1
        ans = 0
        odd = 0
        for key, val in d.items():
            if val%2==0:
                ans += val
            elif val %2 == 1:
                odd += 1
                ans += (val -1)
        if odd >= 1:
            return ans+1
        else:
            return ans
            
            
