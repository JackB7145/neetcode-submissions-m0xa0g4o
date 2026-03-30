# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        '''
        Tasks:
        Move a pointer k down. 
        if completed, 
        node the beginning and the end,
        reverse until k, 
        setting the previous to the end, and the beginning 
        to the next
        '''

        def getEndK(currentStart):
            count = 1
            curr = currentStart
            while count < k:
                if not curr:
                    return None
                curr = curr.next
                count += 1
            return curr

        dummy = node = ListNode()
        node.next = head

        end = getEndK(head)

        print('Value of first end: ', end.val if end else None)

        start = head
        before = node

        while end:
            before.next = end

            prev = end.next
            curr = start

            for _ in range(k):
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
        
            
            start = curr
            end = getEndK(start)

            for _ in range(k):
                node = node.next
            
            before = node

            


        return dummy.next

