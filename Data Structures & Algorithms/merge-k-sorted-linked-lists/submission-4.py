# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = node = ListNode()

        minHeap = [(lists[i].val, i, lists[i]) for i in range(len(lists))]

        heapq.heapify(minHeap)

        while minHeap:
            smallest = heapq.heappop(minHeap)
            smallestNode = smallest[2]
            node.next = smallestNode
            newNode = smallestNode.next

            if newNode:
                heapq.heappush(minHeap, (newNode.val, smallest[1], newNode))

            node = node.next

        return dummy.next