# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        left_root = root.left
        right_root = root.right
        left_arr = []
        right_arr = []
        def left(node):
            if node is None:
                left_arr.append(None)
                return
            left_arr.append(node.val)
            left(node.right)
            left(node.left)
        def right(node):
            if node is None:
                right_arr.append(None)
                return
            right_arr.append(node.val)
            right(node.left)
            right(node.right)
        left(left_root)
        right(right_root)
        if left_arr == right_arr:
            return True
        else:
            return False
