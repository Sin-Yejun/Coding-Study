from itertools import combinations
class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        output = 0
        for i in range(1, len(nums)+1):
            temp = list(combinations(nums, i))
            for j in temp:
                xor = 0
                for k in j:
                    xor ^= k
                output += xor
        return output
