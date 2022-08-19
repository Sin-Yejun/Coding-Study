from functools import reduce
class Solution:
    def signFunc(self, x):
        if x > 0:
            return 1
        elif x < 0:
            return -1
        else:
            return 0
    
    def arraySign(self, nums: List[int]) -> int:
        return  self.signFunc(reduce(lambda x, y: x*y, nums))
