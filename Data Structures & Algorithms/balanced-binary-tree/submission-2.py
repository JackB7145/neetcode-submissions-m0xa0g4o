# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        '''
        What do we want to return.

        I'm thinking we check the depth of the left and right subtrees, 

        but if one of them comes up false, it means we just fuck off and return false perhaps?

        otherwise if the return is not false then we return true
        '''

        def checkBalanced(curr):
            if not curr:
                return [0, True]

            left = checkBalanced(curr.left)
            right = checkBalanced(curr.right)

            if not left[1] or not right[1]:
                return [0, False]
            
            return [1 + max(left[0], right[0]), abs(left[0]-right[0])<2]
        
        return checkBalanced(root)[1]