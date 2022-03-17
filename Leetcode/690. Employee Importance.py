# https://leetcode.com/problems/employee-importance/discuss/209120/Python-solution
class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        def DFS(idx):
            return d[idx][0] + sum(DFS(j) for j in d[idx][1])
        
        d = {}
        for node in employees:
            d[node.id] = [node.importance, node.subordinates]
        return DFS(id)
