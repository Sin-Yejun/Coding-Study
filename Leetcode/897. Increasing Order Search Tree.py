class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        vals = []
        def inorder(node):
            if node is None:
                return
            inorder(node.left)
            vals.append(node.val)
            inorder(node.right)
        inorder(root)
        tree = TreeNode(val = vals[0])
        tmp = tree
        for i in vals[1:]:
            tmp.right = TreeNode(val=i)
            tmp = tmp.right
        
        return tree
