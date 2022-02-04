# https://leetcode.com/problems/cousins-in-binary-tree/discuss/246883/Python-straightforward-and-clean-DFS
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        def dfs(node, parent, depth, mod):
            if node:
                if node.val == mod:
                    return depth, parent
                return dfs(node.left, node, depth + 1, mod) or dfs(node.right, node, depth + 1, mod)
        dx, px, dy, py = dfs(root, None, 0, x) + dfs(root, None, 0, y)
        return dx == dy and px != py
