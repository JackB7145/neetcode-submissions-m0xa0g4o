# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head

        curr = head
        prev = dummy

        if not curr.next:
            return None
        for _ in range(n):
            prev = curr
            curr = curr.next
        
        prev.next = curr.next if curr else None
        return dummy.next