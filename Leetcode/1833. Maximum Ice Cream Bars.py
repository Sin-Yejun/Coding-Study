class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        ans = 0
        costs.sort()
        for cost in costs:
            if coins >= cost:
                ans += 1
                coins -= cost
            else:
                break
        return ans