class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        first = ['q','w','e','r','t','y','u','i','o','p']
        second = ['a','s','d','f','g','h','j','k','l']
        third = ['z','x','c','v','b','n','m']
        ans = []
        for i in words:
            x,y,z = 0,0,0
            for j in i:
                j = j.lower()
                if j in first:
                    x = 1
                elif j in second:
                    y = 1
                elif j in third:
                    z = 1
            if x==1 and y == 0 and z == 0:
                ans.append(i)
            if x==0 and y == 1 and z == 0:
                ans.append(i)
            if x==0 and y == 0 and z == 1:
                ans.append(i)
                
        return ans
                
            
