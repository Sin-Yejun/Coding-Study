class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True
        if len(s1) != len(s2):
            return False
        cnt = 0
        temp = []
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                temp.append(s1[i])
                temp.append(s2[i])
                cnt += 1
        if cnt == 2:
            if temp[0] == temp[3] and temp[1] == temp[2]:
                return True
        return False
