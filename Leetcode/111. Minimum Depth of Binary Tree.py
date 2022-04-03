# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        arr = []
        def find(node, depth):
            if not node:
                return
            if not node.left and not node.right:
                arr.append(depth)
            find(node.left, depth+1)
            find(node.right, depth+1)
        find(root, 1)
        return min(arr)
