# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        #Reverse the linkedlists, have a carry, fuck off and solve
        
        def display(list1):
            curr = list1
            while curr.next:
                print(curr.val, end=" -> ")
                curr = curr.next
            print(curr.val)

        def reverse(list1):
            count = 0
            prev = None
            curr = list1
            while curr:
                count += 1
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            
            return (prev, count)
        

        l1Stuff = reverse(l1)
        l2Stuff = reverse(l2)

        if l1Stuff[1] > l2Stuff[1]:
            curr = l1Stuff[0]
            curr1 = l2Stuff[0]
        else:
            curr = l2Stuff[0]
            curr1 = l1Stuff[0]
        
        head = curr

        carry = 0
        prev = None
        display(curr1)
        display(curr)
        print("Now Showing transformation")
        while curr:
            
            display(head)
            prev = curr
            total = curr.val + curr1.val + carry
            carry = total // 10 if total > 9 else 0
            total -= carry * 10
            curr.val = total
            curr = curr.next
            if curr1.next:
                curr1 = curr1.next
        if carry > 0:
            prev.next = ListNode(carry, None)
        
        return reverse(head)[0] if not(l1Stuff[1] == 1 and l2Stuff[1] == 1) else head
            

        