# https://xingxingpark.com/Leetcode-1047-Remove-All-Adjacent-Duplicates-In-String/
class Solution:
    def removeDuplicates(self, s: str) -> str:
        res = []
        for i in s:
            if res and res[-1]==i:
                res.pop()
            else:
                res.append(i)
        return ''.join(res)
