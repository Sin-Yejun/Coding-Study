# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return root
        def find(node):
            if not node:
                return
            arr.append(node.val)
            find(node.left)
            find(node.right)
        arr = []
        find(root)
        return arr
