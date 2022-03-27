class Solution:
    def reverseWords(self, s: str) -> str:
        arr = s.split(" ")
        ans = []
        for i in arr:
            ans.append(i[::-1])
        return " ".join(ans)
