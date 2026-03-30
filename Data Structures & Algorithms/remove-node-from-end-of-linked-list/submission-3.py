# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp = head
        count = 0 
        while temp:
            temp = temp.next
            count += 1
        
        depth = 0
        curr = head
        prev = None
        while depth < count - n:
            prev = curr
            curr = curr.next
            depth +=1

        if curr and prev:
            prev.next = curr.next
        elif prev:
            prev.next = None
        else:
            if head.next:
                head = head.next
            else:
                head = None


        return head