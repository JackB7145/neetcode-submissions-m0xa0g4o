# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        '''
        We want the maximum path of the left, the right, and the current added together

        '''

        res = float('-inf')
        def traverse(curr):
            nonlocal res
            if not curr:
                return 0
            
            left = traverse(curr.left)
            right = traverse(curr.right)

            res = max(res, curr.val + left + right)

            largest = max(left + curr.val, right + curr.val, 0)
            return largest

        traverse(root)
        return res

