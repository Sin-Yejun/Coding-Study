from collections import defaultdict
class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        answer = []
        d = defaultdict(int)
        for i in nums:
            d[i] += 1
        sort_d = sorted(d.items(), key = lambda x : (x[1],-x[0]))
        for i, j in sort_d:
            for k in range(j):
                answer.append(i)
        return answer