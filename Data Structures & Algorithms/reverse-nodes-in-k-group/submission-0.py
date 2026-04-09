# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        curr = rP = head
        count = k
        while count < 0:
            count -= 1
            rP = rP.next

        while rP: #Repeats as long as rP is not 0 or it hasnt reached the end of the list
            for i in range(k): #Iterates k# of times
                temp = curr.next #Saves the next chain of nodes

                if not i: #If its the first iteration
                    curr.next = rP #The first node has to be the pointing to the right node

                else: #Otherwise
                    curr.next = prev #It should point towards the previous -> the reversal component

                prev = curr #Saves the current as the previous as it prepares to move to the next node
                curr = temp #Moves pointers to the next node to delegate everything
                
                rP = rP.next #Move the right pointer over 1 
                print(curr, rP, end=" -> ")

        return head 