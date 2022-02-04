class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def check(root, arr):
            if root is None:
                arr.append(None)
                return
            arr.append(root.val)
            check(root.left,arr)
            check(root.right,arr)
             
        
        arr1 = []
        arr2 = []
        check(p, arr1)
        check(q, arr2)
        
        if arr1 == arr2:
            return True
        else:
            return False
