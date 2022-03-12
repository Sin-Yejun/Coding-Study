class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        arr_s = list(s)
        arr_t = list(t)
        for i in range(len(arr_s)):
            try:
                arr_t.remove(arr_s[i])
            except:
                continue
        return ''.join(arr_t)
