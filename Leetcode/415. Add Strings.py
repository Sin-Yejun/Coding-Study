class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        def str2int(num):
            result = 0
            for i in num:
                result = result * 10 + ord(i) - ord('0')
            return result
        return str(str2int(num1)+str2int(num2))
