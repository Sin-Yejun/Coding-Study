# https://leetcode.com/problems/brick-wall/discuss/382414/easy-peasy-python-solution
class Solution(object):
    def leastBricks(self, wall):
        """
        :type wall: List[List[int]]
        :rtype: int
        """
        if len(wall) == 0:
            return 0
        
        mp = {}
        
        for w in wall:
            sm = 0
            for i in range(len(w)-1):
                brick = w[i]
                sm += brick
                mp[sm] = mp.get(sm,0) + 1
        rs = 0
        for key, val in mp.items():
            rs = max(rs,val)
        
        return len(wall) - rs
