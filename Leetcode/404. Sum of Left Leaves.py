# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def find(node):
            if node is None:
                return
            if node.left:
                if node.left.left == None and node.left.right == None:
                    output[0] += node.left.val
            find(node.left)
            find(node.right)
                
        output = [0]
        find(root)
        return output[0]
