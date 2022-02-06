class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        def check(root, val):
            if root is None:
                return
            if root.val != val:
                ch.append(1)
            check(root.left, val)
            check(root.right, val)
        ch = []       
        val = root.val
        check(root,val)
        if len(ch) == 0:
            return True
        else:
            return False
