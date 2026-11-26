class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev = dummy
        while True:
            # spacer scouts ahead: lands on the k-th node of this group
            self.spacer = prev
            for _ in range(k):
                self.spacer = self.spacer.next
                if not self.spacer:
                    return dummy.next   # fewer than k left, so leave them as is
            newStart, newEnd = self.reverseK(prev.next, k)
            prev.next = newStart
            prev = newEnd

    def reverseK(self, start, k):
        prev, curr = None, start
        for _ in range(k):
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        start.next = curr
        return prev, start