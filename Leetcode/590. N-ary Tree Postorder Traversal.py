"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        def find(node):
            if not node:
                return
            for i in node.children:
                find(i)
            arr.append(node.val)
        
        arr = []
        find(root)
        return arr
