# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        prev = None
        temp = curr
        while curr != None:
            temp = curr
            curr = curr.next
            temp.next = prev
            prev = temp


        return temp