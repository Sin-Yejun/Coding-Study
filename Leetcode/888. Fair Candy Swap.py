# https://leetcode.com/problems/fair-candy-swap/discuss/161269/C%2B%2BJavaPython-Straight-Forward
class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        diff = (sum(aliceSizes) - sum(bobSizes))/2
        aliceSizes = set(aliceSizes)
        for i in set(bobSizes):
            if diff + i in aliceSizes:
                return [diff+i, i]
