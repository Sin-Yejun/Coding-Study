class Solution:
    def maxDepth(self, root: 'Node') -> int:
        def check(root, m):
            if root is None:
                return
            if len(root.children) > 0:
                m += 1
            else:
                if m > M[0]:
                    M[0] = m
            for i in range(len(root.children)):
                check(root.children[i], m)
        
        M = [0]
        check(root, 0)
        if root is None:
            return 0
        return M[0]+1
