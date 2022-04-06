class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        arr = set(nums)
        if len(nums) == len(arr):
            return False
        else:
            return True
