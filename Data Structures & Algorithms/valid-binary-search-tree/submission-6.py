# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validate(curr, leftB, rightB):
            if not curr:
                return True
            
            elif not leftB < curr.val < rightB:
                return False
            
            return validate(curr.left, leftB, curr.val) and validate(curr.right, curr.val, rightB)
        
        return validate(root, float('-inf'), float('inf'))
        
