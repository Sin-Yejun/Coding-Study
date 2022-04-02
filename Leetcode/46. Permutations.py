import itertools

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        arr = list(itertools.permutations(nums, len(nums)))
        for i in arr:
            ans.append(list(i))
        return ans
        
