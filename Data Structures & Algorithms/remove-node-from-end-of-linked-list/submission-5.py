# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        ''' 
        If we are removing the nth node from the end we need a spacer of size n I believe

        A spacer pointer
        '''
        dummy = ListNode()
        dummy.next = head
        slow, spacer = head, head
        for _ in range(n):
            spacer = spacer.next
        
        prev = dummy
        while spacer:
            prev = slow
            slow = slow.next
            spacer = spacer.next
        
        prev.next = slow.next if slow else None

        return dummy.next