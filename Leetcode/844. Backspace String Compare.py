class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        a = ''
        b = ''
        for i in s:
            if i == '#':
                a= a[0:len(a)-1]
            else:
                a += i
        for j in t:
            if j == '#':
                b = b[0:len(b)-1]
            else:
                b += j
        if a==b:
            return True
        else:
            return False
