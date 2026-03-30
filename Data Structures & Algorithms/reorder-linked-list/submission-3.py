# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        slow = head
        fast = head
        if not fast.next:
            return 
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        
        prev.next = None
        prev = None
        while slow:
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp
        
        curr1 = head
        curr2 = prev

        while curr2:
            temp = curr1.next if curr1 else None
            if curr1:
                curr1.next = curr2 
                 
            curr1 = temp
            temp = curr2.next
            curr2.next = curr1 if curr1 else curr2.next
            curr2 = temp
        
        


        