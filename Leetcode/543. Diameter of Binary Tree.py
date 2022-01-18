# https://leetcode.com/problems/diameter-of-binary-tree/discuss/329022/Python-bottom-up-DFS-solution

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        def depth(root):
            if root is None:
                return 0
            l_depth = depth(root.left)
            r_depth = depth(root.right)
            res[0] = max(res[0], l_depth + r_depth)
            return 1 + max(l_depth, r_depth)
        
        res = [0]
        depth(root)
        return res[0]
