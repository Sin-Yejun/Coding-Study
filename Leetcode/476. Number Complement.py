class Solution:
    def findComplement(self, num: int) -> int:
        b = bin(num)[2:]
        return num^int('1'*len(b),2)
