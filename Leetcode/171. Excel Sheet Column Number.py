class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        length = len(columnTitle)
        temp = 0
        for i in range(length-1):
            temp += ord(columnTitle[i])-64
            temp *= 26
        temp += (ord(columnTitle[length-1])-64)
        return temp
