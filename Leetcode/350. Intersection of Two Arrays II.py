class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        d1 = {}
        d2 = {}
        ans = []
        for i in nums1:
            if i not in d1:
                d1[i] = 1
            else:
                d1[i] += 1
        for i in nums2:
            if i not in d2:
                d2[i] = 1
            else:
                d2[i] += 1
    
        for key, val in d1.items():
            if key in d2.keys():
                m = min(val, d2[key])
                for _ in range(m):
                    ans.append(key)
        
        return ans
