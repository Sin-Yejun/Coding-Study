# https://leetcode.com/problems/container-with-most-water/discuss/6131/O(N)-7-line-Python-solution-72ms

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        width = len(height) - 1
        res = 0
        
        for i in range(width, 0 ,-1):
            if height[left] < height[right]:
                res = max(res, height[left]*i)
                left += 1
            else:
                res = max(res, height[right]*i)
                right -= 1
        return res
