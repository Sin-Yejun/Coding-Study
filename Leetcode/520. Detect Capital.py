class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        L = len(word)
        D = 0
        d = 0
        for i in word:
            if 65 <= ord(i) <= 90:
                D += 1
            else:
                d += 1
        if L == D:
            return True
        elif d == L:
            return True
        elif 65 <= ord(word[0]) <= 90 and d == L-1:
            return True
        return False