class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        output = 0
        for i in nums:
            if i == target:
                return output
            if i > target:
                return output
            output += 1
        return output
