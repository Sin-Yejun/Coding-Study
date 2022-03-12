class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        d = {}
        for i in nums:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1
        
        if max(d.values()) < 2:
            return max(d.values())
        hubo = []
        for key, val in d.items():
            if val == max(d.values()):
                hubo.append(key)
        Min = float("inf")
        for num in hubo:
            idx1 = nums.index(num)
            idx2 = nums[::-1].index(num)
            temp = len(nums)-idx2 - idx1
            Min = min(Min, temp)
        return Min
