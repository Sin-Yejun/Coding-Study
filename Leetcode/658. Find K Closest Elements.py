class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        new_arr = sorted(arr, key = lambda a:abs(a-x))
        answer = new_arr[:k]
        answer.sort()
        return answer
