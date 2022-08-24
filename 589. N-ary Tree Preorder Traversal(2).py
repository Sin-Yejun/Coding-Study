"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        arr = []
        def prefind(node):
            if not node:
                return
            arr.append(node.val)
            for n in node.children:
                prefind(n)
        prefind(root)
        return arr
