class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowel = ['a','e','i','o','u']
        half = len(s)//2
        a = s[:half]
        b = s[half:]
        a = a.lower()
        b = b.lower()
        cnt_a = 0
        cnt_b = 0
        for i in a:
            if i in vowel:
                cnt_a += 1
        for i in b:
            if i in vowel:
                cnt_b += 1
        if cnt_a == cnt_b:
            return True
        else:
            return False
                
            
