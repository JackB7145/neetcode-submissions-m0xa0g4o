# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        def display_linked_list(head):
            current = head
            values = []
            while current:
                values.append(str(current.val))
                current = current.next
            print(" -> ".join(values))

        if not list1:
            return list2
        if not list2:
            return list1

        if list1.val > list2.val:
            curr1, curr2 = list2, list1
        else:
            curr1, curr2 = list1, list2
        
        head = curr1
        prevNode = None
        while curr1:
            temp = curr1 #Saving the current chain
            display_linked_list(curr1)
            print("Entering Loop: ", curr1 and curr2 and curr2.val < curr1.val, "\n")
            while curr1 and curr2 and curr2.val < curr1.val: # While the second list has a value that is less than the value in the right list


                prevNode.next = curr2 # Make the previous node point to the list2 node instead
                temp1 = curr2.next #Saving the pointer the next node of current
                curr2.next = temp # Add the current from list1 onto the end
                prevNode = curr1 #Catching the previous node before we move down one 
                curr2 = temp1 #Moving down 1 on the chain of list 2
                temp = curr1 # Resetting temp to be the list1 chain again but moved 

                display_linked_list(curr2)
                break
                    
            if not curr1:
                prevNode.next = curr2
                break

            prevNode = curr1
            curr1 = curr1.next

            if not curr1:
                prevNode.next = curr2
                break

    
        return head