# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        def find_all(node):
            if node is None:
                return
            element.append(node.val)
            find_all(node.left)
            find_all(node.right)
        element = []
        
        find_all(root)
        print(element)
        answer = False
        copy = element
        idx = 0
        for i in range(len(element)):
            if (k-element[i]) in element[i+1:]:
                answer = True
        return answer
