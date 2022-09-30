class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        type_ = len(set(candyType))
        half = len(candyType)//2
        if type_ < half:
            return type_
        else:
            return half
