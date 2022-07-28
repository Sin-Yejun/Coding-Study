# https://leetcode.com/problems/3sum/discuss/1544657/Easy-python-solution
from itertools import combinations
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        s=set()
        nums.sort()
        n=len(nums)
        for i in range(n):
            j=i+1
            k=n-1
            while(j<k):
                sum=nums[i]+nums[j]+nums[k]
                if sum==0:
                    s.add((nums[i],nums[j],nums[k]))
                    k=k-1
                    j=j+1
                        
                elif sum>0:
                    k=k-1
                    
                else:
                    j=j+1
                    
        return [list(i) for i in s]
