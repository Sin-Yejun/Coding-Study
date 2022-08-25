class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        cnt = 0
        temp = []
        for i in range(len(nums)):
            if nums[i] != 0:
                temp.append(nums[i])
                cnt += 1
        for i in range(cnt):
            nums[i] = temp[i]
        for i in range(cnt, len(nums)):
            nums[i] = 0
