class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        def search(root):
            if root is None:
                return
            arr.append(root.val)
            search(root.left)
            search(root.right)
            
        arr = []
        Min = int(1e5)
        search(root)
        if len(arr) == 1:
            return arr[0]
        arr.sort()
        for i in range(1, len(arr)):
            if Min > arr[i] - arr[i-1]:
                Min = arr[i] - arr[i-1]
        return Min
