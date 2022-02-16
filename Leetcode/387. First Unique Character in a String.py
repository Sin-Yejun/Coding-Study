class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = {}
        for i in s:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1
        ans = []
        for key, val in d.items():
            if val == 1:
                ans.append(key)
        for i in range(len(s)):
            if s[i] in ans:
                return i
        
        return -1
