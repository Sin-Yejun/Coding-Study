# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        n1 = ''
        n2 = ''
        while l1:
            n1 += str(l1.val)
            l1 = l1.next
        while l2:
            n2 += str(l2.val)
            l2 = l2.next
        n = int(n1[::-1])+int(n2[::-1])
        ans = list(map(int, str(n)))
        ans.reverse()
        res = dummy = ListNode()
        for i in ans:
            res.next = ListNode(i)
            res = res.next
        return dummy.next
