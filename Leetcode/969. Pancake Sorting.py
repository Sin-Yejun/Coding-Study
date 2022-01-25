# https://leetcode.com/problems/pancake-sorting/discuss/214213/JavaC%2B%2BPython-Straight-Forward

class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        res = []
        for x in range(len(arr), 1, -1):
            i = arr.index(x)
            res.extend([i + 1, x])
            arr = arr[:i:-1] + arr[:i]
        return res
