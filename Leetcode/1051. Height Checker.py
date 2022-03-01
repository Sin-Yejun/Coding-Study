class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        arr = sorted(heights)
        output = 0
        if arr == heights:
            return 0
        for i in range(len(heights)):
            if arr[i] != heights[i]:
                output += 1
        
        return output
