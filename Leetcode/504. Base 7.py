class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return '0'
        ans = ''
        pos = 1
        if num < 0:
            pos = 0
            num = abs(num)
        while num != 0:
            x = num%7
            ans += str(x)
            num = num//7
        if pos:
            return ans[::-1]
        else:
            return '-'+ans[::-1]
