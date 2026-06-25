class Solution:
    def reverseBetween(self, head, left, right):
        dummy = ListNode(0, head)
        prev = dummy

        # 1. Move to node before left
        for _ in range(left - 1):
            prev = prev.next

        prevL = prev
        leftNode = prev.next

        # 2. Find rightNode
        curr = leftNode
        for _ in range(right - left):
            curr = curr.next

        rightNode = curr
        postR = rightNode.next

        # 3. Cut
        rightNode.next = None

        # 4. Reverse normally
        prev = None
        curr = leftNode
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        # 5. Reconnect
        prevL.next = prev
        leftNode.next = postR

        return dummy.next