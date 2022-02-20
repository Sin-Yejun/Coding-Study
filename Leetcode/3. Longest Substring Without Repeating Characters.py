class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        arr = []
        cnt = 0
        Max = 0
        for i in s:
            if i in arr:
                index = arr.index(i)
                arr = arr[index+1:]
                arr.append(i)
            else:
                arr.append(i)
                if Max <= len(arr):
                    Max = len(arr)
        
        return Max
            
