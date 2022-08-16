class Solution:
    def countOdds(self, low: int, high: int) -> int:
        
        if low % 2 == 1 and high % 2 == 1:
            answer = (high - low) // 2 +1
        else:
            answer = (high - low) // 2
            if low % 2 == 1 or high % 2 == 1:
                answer += 1
        return answer
