class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        arr = set(list(sentence))
        if len(arr) == 26:
            return True
        else:
            return False
