# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # if not lists:
        #     return []
        minHeap = [(node.val, i, node) for i, node in enumerate(lists) if node]
        heapq.heapify(minHeap)

        dummy = node = ListNode()
        while minHeap:
            _, idx, curr = heapq.heappop(minHeap)
            if curr.next:
                heapq.heappush(minHeap, (curr.next.val, idx, curr.next))
            
            node.next = curr
            node = node.next

        return dummy.next
