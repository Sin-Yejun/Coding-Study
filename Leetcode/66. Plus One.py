class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s = ''.join(map(str,digits))
        
        return list(map(int,str(int(s)+1)))
