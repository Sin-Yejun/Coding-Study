class Solution:
    def average(self, salary: List[int]) -> float:
        M = max(salary)
        m = min(salary)
        salary.remove(M)
        salary.remove(m)
        return round(sum(salary)/len(salary),5)
