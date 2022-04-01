# https://leetcode.com/problems/string-to-integer-atoi/discuss/857817/Python.-A-beautiful-solution.-faster-than-98.72-of-Python3
class Solution:
    def myAtoi(self, s: str) -> int:
        stripped = s.strip()
        sign = 1

        if not stripped:
            return 0       

        elif stripped[0] in ("+", "-"): 
            if stripped[0] == "-":
                sign = -1
            stripped = stripped[1:]
        elif not stripped[0].isdigit():
            return 0

        if not stripped:
            return 0
        try:
            ans = int(stripped[0])
            stripped = stripped[1:]

            for c in stripped:
                if c.isdigit():
                    ans = ans * 10 + int(c)
                else:
                    break    

            if sign == 1:
                return sign * ans if ans < 2**31 else 2147483647
            return -ans if ans <= 2**31 else -2147483648
        except:
            return 0
