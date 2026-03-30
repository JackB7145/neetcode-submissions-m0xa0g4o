# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        while head:
            prev = head
            head = head.next
            prev.next = "Passed"
            if head and head.next == "Passed":
                return True
        return False