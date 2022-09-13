"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        arr = [(root.val,0)]
        M = [0]
        def find(node, depth):
            if not node:
                return
            M[0] = max(depth, M[0])
            for child in node.children:
                arr.append((child.val, depth))
                find(child, depth+1)
        find(root, 1)
        ans = [[] for _ in range(M[0])]
        for v, i in arr:
            ans[i].append(v)
        return ans
