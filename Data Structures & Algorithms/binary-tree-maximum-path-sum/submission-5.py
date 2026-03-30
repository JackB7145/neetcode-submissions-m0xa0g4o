# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        '''
        Note that the number of nodes in the tree is 1 <= 1000


        I think at any given node we have an opportunity to go right, or go back to the previous parent

        meaning find the sum of the left subtree, and either include it in the above path, or choose to go right
        
        Wait I like postorder traversal, considering joining the two at the parent node, and then returning the larger one

        cuz you are either joining at the parent or going back up
        '''
        res = float('-inf')
        def traverse(curr):
            nonlocal res
            if not curr:
                return 0

            left = traverse(curr.left)
            right = traverse(curr.right)
            res = max(res, left + right + curr.val)
            return max(curr.val + max(left, right, 0), 0)
        
        fromRoot = traverse(root)
        return res
