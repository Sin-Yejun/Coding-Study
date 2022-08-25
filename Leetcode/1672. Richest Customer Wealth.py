class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        Max = 0
        for arr in accounts:
            Max = max(Max, sum(arr))
        
        return Max
