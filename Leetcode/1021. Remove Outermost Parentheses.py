# https://leetcode.com/problems/remove-outermost-parentheses/discuss/270022/JavaC%2B%2BPython-Count-Opened-Parenthesis
class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        res = []
        opened = 0
        for c in s:
            if c == "(" and opened > 0:
                res.append(c)
            if c == ")" and opened > 1:
                res.append(c)
            if c == "(":
                opened += 1
            else:
                opened -= 1
        return "".join(res)
