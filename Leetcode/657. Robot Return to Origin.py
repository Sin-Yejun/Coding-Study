class Solution:
    def judgeCircle(self, moves: str) -> bool:
        a,b= 0, 0
        for i in moves:
            if i == 'U':
                a += 1
            if i == 'D':
                a -= 1
            if i == 'L':
                b += 1
            if i == 'R':
                b -= 1
        if a == 0 and b == 0:
            return True
        return False
