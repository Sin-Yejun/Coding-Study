class Solution:
    def check_array(self, arr):
        diff = arr[1] - arr[0]
        for i in range(1, len(arr)):
            if arr[i] - arr[i-1] != diff:
                return False
        return True
    
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        ans = []
        for i in range(len(l)):
            start = l[i]
            end = r[i]
            arr = nums[start:end+1]
            arr.sort()
            if self.check_array(arr):
                ans.append(True)
            else:
                ans.append(False)
        return ans
