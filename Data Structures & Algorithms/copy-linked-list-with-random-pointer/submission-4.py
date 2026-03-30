"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        '''
        We need to store all the nodes in a hash map by their value
        As we pass, each node has a random and a next, if the node for random or next is in the 
        the mp already we assign it, if it's not we create a new one and add it to the mp
        '''
        mp = {None:None}
        curr = head
        dummy = node = Node(-101)

        while curr:
            newNode = Node(curr.val)
            mp[curr] = newNode
            curr = curr.next
        
        curr = head
        while curr:
            copyNode = mp[curr]
            copyNode.next = mp[curr.next]
            copyNode.random = mp[curr.random]

            node.next = copyNode
            node = node.next

            curr = curr.next
        
        return dummy.next


        