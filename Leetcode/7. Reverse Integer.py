class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return 0
        sign = 0
        if x < 0:
            x = -x
            sign = 1
        arr = list(map(int,str(x)))
        arr.reverse()
        while arr[0]==0:
            arr.remove(0)
        ans = int(''.join(map(str,arr)))
        if -2**31 < ans < 2**31-1:
            if sign == 0:
                return ans
            else:
                return -ans
        else:
            return 0
