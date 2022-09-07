class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        arr2num = int(''.join(map(str,num)))
        s = arr2num + k
        arr = list(map(int,str(s)))
        return arr
