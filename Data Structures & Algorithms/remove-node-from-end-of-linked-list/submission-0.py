class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        tracker = dummy
        count = 0
        curr = head
        while curr:
            if count >= n:
                tracker = tracker.next
            
            curr = curr.next
            count += 1
        
        temp = tracker.next.next
        tracker.next = temp
        
        return dummy.next