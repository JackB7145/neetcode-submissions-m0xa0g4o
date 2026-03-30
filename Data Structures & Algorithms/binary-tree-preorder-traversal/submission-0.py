# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def traverse(curr):
            if not curr:
                return
            
            res.append(curr.val)
            traverse(curr.left)
            traverse(curr.right)
        
        traverse(root)
        return res