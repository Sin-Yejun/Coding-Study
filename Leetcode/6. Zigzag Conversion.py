class Solution:
    def convert(self, s: str, numRows: int) -> str:
        switch = 1
        index = 0
        t = []
        ans = ''
        if numRows == 1:
            return s
        for i in s:
            t.append([i,index])
            if index == 0:
                switch = 1
            elif index == numRows-1:
                switch = -1
            if switch == 1:
                index += 1
            else:
                index -= 1
        for i in range(numRows):
            for j in range(len(t)):
                if t[j][1] == i:
                    ans += t[j][0]
        return ans
            
