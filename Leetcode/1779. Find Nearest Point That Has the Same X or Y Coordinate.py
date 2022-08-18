class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        M = float('inf')
        answer = -1
        for a, b in points:
            if a == x or b == y:
                r = abs(x-a) + abs(y-b)
                if M > r:
                    answer = points.index([a,b])
                    M = min(M,r)
        return answer
