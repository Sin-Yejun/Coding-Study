# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def find(root):
            if not root:
                return
            if low <= root.val <= high:
                s[0] += root.val
            find(root.left)
            find(root.right)
        
        s = [0]
        find(root)
        return s[0]
