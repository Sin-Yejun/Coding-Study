class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        idx = -1
        for i in range(len(word)):
            if word[i] == ch:
                idx = i
                break
        if idx == -1:
            return word
        output = word[:idx+1][::-1] + word[idx+1:]
        return output
