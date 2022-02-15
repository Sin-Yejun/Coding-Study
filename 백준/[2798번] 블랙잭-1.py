n, m = map(int,input().split())

nums = list(map(int,input().split()))
mmax = 0
for i in range(len(nums)-2):
    for j in range(i+1, len(nums)-1):
        for k in range(j+1, len(nums)):
            if nums[i]+nums[j]+nums[k] <= m:
                if mmax < nums[i]+nums[j]+nums[k]:
                    mmax = nums[i]+nums[j]+nums[k]
                
print(mmax)
    
            
