# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def traverse(curr):
            if not curr:
                return [0, True]

            left = traverse(curr.left)
            right = traverse(curr.right)

            if not left[1] or not right[1] or abs(left[0] - right[0]) > 1:
                return [0, False]

            return [1 + max(left[0], right[0]), True]

        return traverse(root)[1]
        
