# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        '''
        I'm going to say in order traversal of a binary tree. If it is the kth smallest
        we can traverse left parent right given that left < parent < right. What if we go
        left until we find the leftmost node, that is k = 0, then we keep a global counter adding 1 to k
        until we get our value, then set a nonlocal response node value and at the end of teh traversal we return that
        we could also prune for numbers greater than k

        the ineffienciet way would be to traverse inorder, keep an array for size n and retunr the kth element
        from that array but that is suboptimal as we are allocating n extra space
        '''
        count = -1 
        res = None
        def traverse(curr):
            nonlocal count, res
            if not curr and count < 0:
                count += 1
                return
            elif count > k or not curr:
                return 

            traverse(curr.left)
            count += 1
            if count == k:
                res = curr.val
            traverse(curr.right)
        
        traverse(root)
        return res
