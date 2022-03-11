class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        point1 = 0
        point2 = 1
        while point1 != len(nums):
            try:
                if nums[point1] == 0 and nums[point2] != 0:
                    nums[point1], nums[point2] = nums[point2], nums[point1]
                elif nums[point1] != 0:
                    point1 += 1; point2 += 1
                elif nums[point2] == 0:
                    point2 += 1
            except:
                break
            
            
            
