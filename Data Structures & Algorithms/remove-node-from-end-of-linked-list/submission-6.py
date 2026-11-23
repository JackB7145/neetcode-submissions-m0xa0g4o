# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        prev = dummy    
        curr = dummy.next

        for i in range(n):
            curr = curr.next

        slow, end = head, curr

        while end != None:
            prev = slow
            slow = slow.next
            end = end.next

        prev.next = slow.next

        return dummy.next

        