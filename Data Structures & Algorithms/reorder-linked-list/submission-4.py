class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        # 1. Find the middle
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # 2. Split and reverse the second half
        second = slow.next
        slow.next = None
        prev = None
        while second:
            nxt = second.next
            second.next = prev
            prev = second
            second = nxt

        # 3. Merge using a dummy node
        dummy = node = ListNode()
        curr1 = head
        curr2 = prev

        while curr1 and curr2:
            next1, next2 = curr1.next, curr2.next   # save before relinking

            node.next = curr1
            node = node.next
            node.next = curr2
            node = node.next

            curr1, curr2 = next1, next2

        if curr1:
            node.next = curr1
        elif curr2:
            node.next = curr2