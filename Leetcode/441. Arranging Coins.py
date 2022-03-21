# https://leetcode.com/problems/arranging-coins/discuss/1560442/C%2B%2BPython-4-Simple-Solutions-w-Explanation-or-Brute-Force-%2B-Binary-Search-%2B-Math-or-Beats-100
class Solution:
    def arrangeCoins(self, n: int) -> int:
        rows = 1
        while n > 0:
            rows += 1
            n -= rows
        return rows - 1
            
                
