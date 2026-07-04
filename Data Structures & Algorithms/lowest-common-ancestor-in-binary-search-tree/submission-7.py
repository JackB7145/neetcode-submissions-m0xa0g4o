# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        res = TreeNode(-1)
        def traverse(curr):
            nonlocal res
            if not curr:
                return False
            
            currentIsOne = curr.val == p.val or curr.val == q.val

            left = traverse(curr.left)
            right = traverse(curr.right)

            if left and right or left and currentIsOne or right and currentIsOne:
                res = curr
                return False

            if curr.val == p.val or curr.val == q.val:
                return True
            
            return left or right
        
        traverse(root)
        return res
            

