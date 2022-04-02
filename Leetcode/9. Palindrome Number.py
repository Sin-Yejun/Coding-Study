class Solution:
    def isPalindrome(self, x: int) -> bool:
        arr = list(map(str,str(x)))
        if arr == arr[::-1]:
            return True
        else:
            return False
