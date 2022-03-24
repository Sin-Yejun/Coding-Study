class Solution:
    def balancedStringSplit(self, s: str) -> int:
        arr = []
        cnt = 0
        for i in s:
            arr.append(i)
            if arr and arr.count('R') == arr.count('L'):
                arr.clear()
                cnt += 1  
            
            #print(arr)
        return cnt
