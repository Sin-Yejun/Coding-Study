import math
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n<1:
            return False
        if math.log(n,4).is_integer():
            return True
        else:
            return False
