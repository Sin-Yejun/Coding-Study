# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        M = [0]
        def add(node, d):
            if not node:
                return
            if d == depth-1:
                temp = node.left
                node.left = TreeNode(val)
                node.left.left = temp
                temp = node.right
                node.right = TreeNode(val)
                node.right.right = temp
            if node.left:
                add(node.left, d+1)
            if node.right:
                add(node.right, d+1)
        if depth == 1:
            temp = root
            root = TreeNode(val)
            root.left = temp
        else:
            add(root, 1)
        return root
