class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        answer = ''
        M_LEN = max(len(word1), len(word2))
        
        for i in range(M_LEN):
            if len(word1) > i:
                answer += word1[i]
            if len(word2) > i:
                answer += word2[i]
        return answer
