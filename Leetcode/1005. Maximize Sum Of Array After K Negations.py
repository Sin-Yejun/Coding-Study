# https://leetcode.com/problems/maximize-sum-of-array-after-k-negations/discuss/252254/JavaC%2B%2BPython-Sort
class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        nums.sort()
        i = 0
        while i < len(nums) and k > 0 and nums[i] < 0:
            k -= 1
            nums[i] *= -1
            i += 1
        if k %2 == 0:
            return sum(nums)
        else:
            return sum(nums) - 2*min(nums)
