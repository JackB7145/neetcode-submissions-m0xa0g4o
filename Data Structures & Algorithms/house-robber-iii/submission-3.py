# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from functools import lru_cache
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        @lru_cache
        def traverse(curr, canRob):
            if not curr:
                return 0

            total = 0

            if canRob:
                total = curr.val + traverse(curr.left, False) + traverse(curr.right, False)

            total = max(total, traverse(curr.left, True) + traverse(curr.right, True))

            return total
        
        return traverse(root, True)
            

