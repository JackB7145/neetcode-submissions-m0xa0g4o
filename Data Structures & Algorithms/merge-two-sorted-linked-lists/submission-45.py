# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = node = ListNode()

        l1, l2 = list1, list2

        while l1 or l2:
            val1 = l1.val if l1 else float('inf')
            val2 = l2.val if l2 else float('inf')

            if val1 < val2:
                node.next = l1
                l1 = l1.next
            else:
                node.next = l2
                l2 = l2.next
            
            node = node.next
        return dummy.next