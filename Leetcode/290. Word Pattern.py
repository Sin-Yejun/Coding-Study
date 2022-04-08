# https://leetcode.com/problems/word-pattern/discuss/73411/My-solution-in-python

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        if len(pattern) != len(words):
            return 0
        d1 = {}
        d2 = {}
        for ch, word in zip(pattern, words):
            if ch not in d1 and word not in d2:
                d1[ch] = word
                d2[word] = ch
            elif (ch not in d1 and word in d2):
                return 0
            elif (ch in d1 and d1[ch] != word):
                return 0
        return 1
