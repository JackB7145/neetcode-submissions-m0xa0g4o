# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def display(l1):
            while l1:
                if not l1.next:
                    print(l1.val)
                    break
                print(l1.val, end=" -> ")
                l1 = l1.next

        dummy = ListNode(0)
        dummy.next = head
        prev_tail = dummy
        curr = head

        while True:
            # Check if there are at least k nodes left
            rP = curr
            count = 0
            while rP and count < k:
                rP = rP.next
                count += 1
            if count < k:
                break  # Not enough nodes to reverse

            # Reverse k nodes
            prev = rP
            temp_curr = curr  # Save the start of the group (will become the tail)
            for i in range(k):
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp

            # Connect previous group to the new head
            prev_tail.next = prev
            prev_tail = temp_curr  # Move tail pointer to the end of the reversed group

        return dummy.next
