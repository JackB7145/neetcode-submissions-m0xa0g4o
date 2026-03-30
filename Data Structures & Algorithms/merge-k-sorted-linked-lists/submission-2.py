# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = node = ListNode()
        temp =  [None for _ in range(len(lists))]
        while lists != temp:
            highest = (float('inf'), len(lists))

            for i in range(len(lists)):
                if not lists[i]:
                    continue
                
                if highest[0] > lists[i].val:
                    highest = (lists[i].val, i)

            node.next = lists[highest[1]]
            node = node.next
            lists[highest[1]] = lists[highest[1]].next

        return dummy.next