from collections import defaultdict

class Solution:
    def frequencySort(self, s: str) -> str:
        d = defaultdict(int)
        for i in s:
            d[i] += 1
        sorted_d = sorted(d.items(), key= operator.itemgetter(1), reverse = True)
        answer = ''
        for i, j in sorted_d:
            answer += i*j
        return answer