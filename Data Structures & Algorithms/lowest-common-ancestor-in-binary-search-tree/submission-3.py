# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def findLowest(curr, p, q):
            if not curr:
                return False
            
            left = findLowest(curr.left, p, q)
            right = findLowest(curr.right, p, q)

            if left and right:
                return curr
            
            if left and curr.val not in [p.val, q.val]:
                return left
            
            if right and curr.val not in [p.val, q.val]:
                return right
            
            return curr if curr.val == p.val or curr.val == q.val else False
            
        return findLowest(root, p, q)
        


        

        
