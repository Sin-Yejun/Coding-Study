# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        
        cur = head
        arr = []
        while cur:
            arr.append(cur.val)
            cur = cur.next
        paths = []
        def find(node, path):
            if not node:
                return
            path.append(node.val)
            if not node.left and not node.right:
                paths.append(list(path))
            find(node.left,path)
            find(node.right,path)
            path.pop()
            
        path = deque()
        find(root,path)
        arrs = ''.join(map(str,arr))
        for p in paths:
            ps = ''.join(map(str,p))
            if arrs in ps:
                return True
        return False
