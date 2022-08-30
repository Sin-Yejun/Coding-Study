class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        l =  len(s)
        for i in range(1, len(s)//2+1):
            if l % i != 0:
                continue
            if s[:i]*(l//i) == s:
                return True
        return False
