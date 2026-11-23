class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        lb = dummy
        for _ in range(left - 1):
            lb = lb.next

        start = lb.next
        prev, curr = None, start
        for _ in range(right - left + 1):
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        lb.next = prev      # node before the section → new front (old right)
        start.next = curr   # old front (now the tail) → node after the section
        return dummy.next