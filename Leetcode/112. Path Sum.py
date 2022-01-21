# https://leetcode.com/problems/path-sum/discuss/454248/Python-DFS-Recursive
class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        def DFS(node, s, targetSum):
            if node is None:
                return
            s += node.val
            if node.left is None and node.right is None:
                if s == targetSum:
                    return True
                else:
                    False
            
            if node.left:
                if DFS(node.left, s, targetSum):
                    return True
            
            if node.right:
                if DFS(node.right, s, targetSum):
                    return True
                
        if DFS(root, 0, targetSum):
            return True
        return False
