class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def find(root, depth):
            if root is None:
                return
            dp.append(depth)
            find(root.left, depth+1)
            find(root.right, depth+1)
        
        dp = []
        find(root,1)
        
        if len(dp) == 0:
            return 0
        return max(dp)
