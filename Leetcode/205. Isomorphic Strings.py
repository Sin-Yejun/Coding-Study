class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        arr_s = []
        idx_s = []
        idx = 0
        for i in s:
            for j in range(len(arr_s)):
                if i == arr_s[j]:
                    idx_s.append(j)
            if i not in arr_s:
                arr_s.append(i)
                idx_s.append(idx)
                idx += 1
        
        arr_t = []
        idx_t = []
        idx = 0
        for i in t:
            for j in range(len(arr_t)):
                if i == arr_t[j]:
                    idx_t.append(j)
            if i not in arr_t:
                arr_t.append(i)
                idx_t.append(idx)
                idx += 1
        if idx_s == idx_t:
            return True
        else:
            return False
                
            
                
            
