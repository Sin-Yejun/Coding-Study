class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        if n == 1:
            return True
        binary = bin(n)[2:]
        if binary[0] == '1':
            check = 1
        else:
            check = 0
        for b in binary[1:]:
            if check == 1 and b == '0':
                check = 0
            elif check == 0 and b == '1':
                check = 1
            else:
                return False
        return True
