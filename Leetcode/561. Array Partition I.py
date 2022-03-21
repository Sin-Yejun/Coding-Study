class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort(reverse = True)
        print(nums)
        answer = 0
        for i in range(1,len(nums),2):
            answer += nums[i]
        return answer
