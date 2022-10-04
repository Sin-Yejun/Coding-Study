# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        s = []
        def find(node):
            if not node:
                return
            s.append(str(node.val))
            if not node.left and not node.right:
                return
            
            s.append('(')
            find(node.left)
            s.append(')')
            if node.right:
                s.append('(')
                find(node.right)
                s.append(')')
        
        find(root)
        return ''.join(s)            
