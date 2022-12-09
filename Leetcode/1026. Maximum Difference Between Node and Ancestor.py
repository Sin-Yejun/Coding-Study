# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        paths = [0]
        def find(node, path):
            if not node:
                return
            path.append(node.val)
            if node.left is None and node.right is None:
                print(path)
                paths[0] = max(max(path) - min(path),paths[0])
            find(node.left, path)
            find(node.right, path)
            path.pop()
        find(root,[])
        
        return paths[0]