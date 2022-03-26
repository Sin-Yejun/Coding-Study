# https://leetcode.com/problems/cousins-in-binary-tree/discuss/299889/Python-BFS-solution
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        
        nodes = collections.defaultdict(list)
        queue = [(root,0,0)]
        while queue:
            node,level,parent = queue.pop(0)
            nodes[node.val] = [level,parent]

            if node.left:
                queue.append((node.left,level+1,node.val))
            if node.right:
                queue.append((node.right,level+1,node.val))

        if nodes[x][0]==nodes[y][0] and nodes[x][1] != nodes[y][1]:
            return True
        return False
    
    
