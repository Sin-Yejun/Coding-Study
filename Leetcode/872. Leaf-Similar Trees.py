# 872. Leaf-Similar Trees
class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        def check(node, arr):
            if node is None:
                return
            if node.left is None and node.right is None:
                arr.append(node.val)
            check(node.left,arr)
            check(node.right,arr)
        
        arr1 = []
        arr2 = []
        check(root1, arr1)
        check(root2, arr2)
        if arr1 == arr2:
            return True
        else:
            return False
