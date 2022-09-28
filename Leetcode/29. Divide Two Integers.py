class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        ans = dividend / divisor
        ans = int(ans)
        ans = max(ans, -2147483648)
        ans = min(ans, 2147483647)
        return ans
