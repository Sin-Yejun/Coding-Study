class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        even_sum = 0
        for i in nums:
            if i % 2 == 0:
                even_sum += i
        arr = []
        for x,y in queries:
            prev, next = nums[y], nums[y]+x
            if prev % 2 == 0:       # nums[y]가 짝수일 때
                if next % 2 == 0:
                    even_sum += x
                else:
                    even_sum -= prev
            else:                   # nums[x]가 홀수일 때
                if next % 2 == 0:
                    even_sum += next
                else:
                    pass
            nums[y] += x
            arr.append(even_sum)
        return arr
            
                
                    
