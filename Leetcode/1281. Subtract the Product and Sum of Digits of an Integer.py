from functools import reduce
class Solution:
    def multiply(self, arr):
        return reduce(lambda x, y : x*y, arr)
    def subtractProductAndSum(self, n: int) -> int:
        s = list(map(int,str(n)))
        return self.multiply(s) - sum(s)
