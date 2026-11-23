# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = node = ListNode()
        curr1, curr2 = list1, list2
        while curr1 and curr2:
            val1 = curr1.val
            val2 = curr2.val

            if val1 > val2:
                node.next = curr2
                curr2 = curr2.next
            else:
                node.next = curr1
                curr1 = curr1.next
        
            node = node.next

        if curr2:
            node.next = curr2
        
        elif curr1:
            node.next = curr1
        
        return dummy.next


