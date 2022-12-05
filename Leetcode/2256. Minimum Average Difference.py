class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        miniavg = float('inf')
        left = 0
        answer = 0
        s = sum(nums)
        for i, num in enumerate(nums):
            left += num
            right = s - left
            if i != len(nums)-1:
                if abs(left//(i+1) - right//(len(nums)-i-1)) < miniavg:
                    miniavg = abs(left//(i+1) - right//(len(nums)-i-1))
                    answer = i
            else:
                if abs(left//(i+1)) < miniavg:
                    miniavg = abs(left//(i+1))
                    answer = i
        return answer