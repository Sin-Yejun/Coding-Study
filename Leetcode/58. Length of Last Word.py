class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        arr = s.split(' ')
        for i in arr[::-1]:
            if len(i) > 0:
                return len(i)
        
