#https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/discuss/39743/Python-DP-solution-120ms
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        one_buy = two_buy =   sys.maxsize
        one_profit = two_profit = 0
        for p in prices:
            one_buy = min(one_buy,p)
            one_profit = max(one_profit,p - one_buy)
            two_buy = min(two_buy,p - one_profit)
            two_profit = max(two_profit,p - two_buy)
            print(p,':',one_buy,one_profit,two_buy,two_profit)
        return two_profit
