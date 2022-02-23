class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        def check_cycle(head):
            try:
                slow = head
                fast = head.next
                while slow is not fast:
                    slow = slow.next
                    fast = fast.next.next
                return True
            except:
                return False
            
        if check_cycle(head):
            arr = []
            while True:
                if id(head) not in arr:
                    arr.append(id(head))
                else:
                    return head
                    break
                head = head.next
        else:
            return None
