from collections import deque
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dials = {'2':"abc",'3':"def",'4':"ghi",'5':"jkl",
     '6':"mno",'7':"pqrs",'8':"tuv",'9':"wxyz"}
        if not digits:
            return []
        LEN = len(digits)
        ans = []
        def dfs(idx, string):
            if idx == LEN:
                ans.append(string)
            else:
                letters = dials[digits[idx]]
                for letter in letters:
                    dfs(idx+1, string+letter)
        dfs(0,"")
        return ans
