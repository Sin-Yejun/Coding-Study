import math
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n == 1:
            return True
        elif n == 0:
            return False
        else:
            return n%3 == 0 and self.isPowerOfThree(n//3)
