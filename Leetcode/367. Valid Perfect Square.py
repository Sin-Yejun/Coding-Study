import math
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        n = math.sqrt(num)
        if float(n)-int(n) == 0:
            return True
        else:
            return False
