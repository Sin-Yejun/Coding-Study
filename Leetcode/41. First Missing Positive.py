class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums = list(set(nums))
        nums.sort()
        r = 1
        for i in nums:
            if i > 0:
                if i != r:
                    return r
                r += 1
        return r
