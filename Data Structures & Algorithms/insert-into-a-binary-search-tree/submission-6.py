# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def traverse(curr):
            if not curr:
                return
            
            if val <= curr.val:
                if not curr.left:
                    curr.left = TreeNode(val)
                    return
                traverse(curr.left)
            
            else:
                if not curr.right:
                    curr.right = TreeNode(val)
                    return
                traverse(curr.right)
            
        traverse(root)
        if not root:
            return TreeNode(val)
        return root