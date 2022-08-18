class Solution:
    def hammingWeight(self, n: int) -> int:
        a = bin(n)[2:]
        return a.count('1')
