class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        ans = []
        for num in range(left, right+1):
            flag = True
            arr = list(map(int,str(num)))
            for i in arr:
                if i == 0:
                    flag = False
                elif num % i != 0:
                    flag = False
            
            if flag:
                ans.append(num)
        
        return ans
