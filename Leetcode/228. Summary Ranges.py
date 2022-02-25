class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        cnt = 0
        arr = []
        for i in range(len(nums)):
            try:
                if nums[i+1]== nums[i]+1:
                    cnt += 1
                else:
                    if cnt == 0:
                        arr.append(str(nums[i]))
                    else:
                        arr.append(str(nums[i-cnt])+"->"+str(nums[i-cnt]+cnt))
                        cnt = 0
            except:
                if cnt == 0:
                    arr.append(str(nums[i]))
                else:
                    arr.append(str(nums[i-cnt])+"->"+str(nums[i-cnt]+cnt))
                    cnt = 0
        return arr
            
                
