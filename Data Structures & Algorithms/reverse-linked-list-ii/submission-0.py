class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        
        before_left = dummy
        for _ in range(left - 1):
            before_left = before_left.next

        prev = None
        curr = before_left.next
        for _ in range(right - left + 1):
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        before_left.next.next = curr
        before_left.next = prev
        
        return dummy.next