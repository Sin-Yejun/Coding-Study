# https://leetcode.com/problems/balanced-binary-tree/discuss/436499/Python-beats-99-(40ms)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def depth(self, root: TreeNode) -> int:
        if not root:
            return 0
        hl = self.depth(root.left) + 1
        hr = self.depth(root.right) + 1
        if abs(hl - hr) > 1:
            raise Exception("Sorry, the tree is unbalanced")
        else:
            return max(hl, hr)
        
    def isBalanced(self, root: TreeNode) -> bool:
        try:
            self.depth(root)
        except:
            return False
        return True
