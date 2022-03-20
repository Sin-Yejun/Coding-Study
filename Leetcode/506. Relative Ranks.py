class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        def rank(k):
            cnt = 1
            for i in score:
                if i != k and i > k:
                    cnt += 1
            return cnt
        ans = []
        for i in score:
            x = rank(i)
            if x == 1:
                ans.append("Gold Medal")
            elif x == 2:
                ans.append("Silver Medal")
            elif x == 3:
                ans.append("Bronze Medal")
            else:
                ans.append(str(x))
        return ans
