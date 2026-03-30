# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def traverse(curr, left, right):
            if not curr:
                return True
            
            leftSub = traverse(curr.left, left, curr.val)
            rightSub = traverse(curr.right, curr.val, right)

            return left < curr.val < right and leftSub and rightSub

        return traverse(root, float('-inf'), float('inf'))