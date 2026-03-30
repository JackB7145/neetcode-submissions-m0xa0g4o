# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSameTree(t1, t2):
            if not t1 and not t2:
                return True
            elif not t1 or not t2:
                return False

            return t1.val == t2.val and isSameTree(t1.left, t2.left) and isSameTree(t1.right, t2.right)

        def findRoot(curr):
            if not curr:
                return False
            
            left = findRoot(curr.left) 
            right = findRoot(curr.right)

            if left or right:
                return True
            
            if curr.val == subRoot.val and isSameTree(curr, subRoot):
                return True
            return False

        
        return findRoot(root)
