# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = temp = ListNode()

        while True:
            exchange = False
            sIndex = -1

            for i in range(len(lists)):
                if lists[i]:
                    if sIndex == -1 or lists[i].val < lists[sIndex].val:
                        sIndex = i
                        exchange = True
            
            if not exchange:
                break

            temp.next = lists[sIndex]
            lists[sIndex] = lists[sIndex].next
            temp = temp.next

        return dummy.next



#My solution:
#We repeat until there is no longer an exchange between linked lists and comparisons are completed. As long as there is one node left in the linked
#we will go over it again and again until each node is currectly organized and added. I itereate over the lists 1 by 1