class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = nums1 + nums2
        nums.sort()
        if len(nums) %2 == 1:
            median = nums[len(nums)//2]
            return float(median)
        else:
            median = nums[len(nums)//2] + nums[len(nums)//2-1]
            return float(median)/2
