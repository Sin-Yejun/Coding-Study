class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        n = columnNumber
        string = ''
        while n != 0:
            if n%26 == 0:
                string += 'Z'
                n -= 1
            else:
                string += chr(n%26+64)
            n = n//26
           
        return string[::-1]
