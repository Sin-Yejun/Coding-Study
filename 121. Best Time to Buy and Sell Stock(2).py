class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        M = 0
        m = float('inf')
        for price in prices:
            m = min(price, m)
            profit = price - m
            M = max(M, profit)
        return M
