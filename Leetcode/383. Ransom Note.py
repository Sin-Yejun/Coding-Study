class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        r = list(ransomNote)
        m = list(magazine)
        while r:
            x = r.pop()
            if x in m:
                m.remove(x)
            else:
                return False
        return True
