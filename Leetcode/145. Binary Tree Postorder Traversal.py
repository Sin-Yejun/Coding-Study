# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def find(node):
            if not node:
                return
            
            find(node.left)
            find(node.right)
            arr.append(node.val)
            
        arr = []
        find(root)
        return arr
