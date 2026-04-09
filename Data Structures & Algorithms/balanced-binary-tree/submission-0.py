# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        #Look at the root node
        #Determine the height of its left and right nodes
        #If the height of the left is >= height of right +/-1 we are good. Else return false
        #If we are false return false
        #If we are true, then look at the depth of the right and

        #We know its false when either the left node has children with children and the right node has nothing: not curr.right and curr.left and curr.left.left or curr.right.right 
        def findChildren(curr):
            if curr:
                if curr.left and not curr.right:
                    if curr.left.left or curr.left.right:
                        return False
                elif curr.right and not curr.left:
                    if curr.right.left or curr.right.right:
                        return False
                else:
                    return findChildren(curr.left) and findChildren(curr.right)
            return True

        return findChildren(root)