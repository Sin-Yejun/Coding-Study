class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        def search(root, pv):
            if root is None:
                return
            pv += str(root.val)
            if root.left is None and root.right is None:
                pv = '0b' + pv
                arr.append(pv)
            search(root.left, pv)
            search(root.right, pv)
            
        pv = ''
        arr = []
        search(root, pv)
        ans = 0
        for i in arr:
            ans += int(i,2)
        return ans
