# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        '''
        Find the depth of the left and right at any given node, find the sum and consider it for the maxiumum
        '''
        res = 0
        def findDepth(curr):
            nonlocal res
            if not curr:
                return 0
            
            left = findDepth(curr.left)
            right = findDepth(curr.right)

            print(curr.val, left, right)

            res = max(res, left + right)
            
            return 1 + max(left, right)
        findDepth(root)
        return res
