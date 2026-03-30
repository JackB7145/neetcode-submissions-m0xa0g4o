# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def traverse(curr):
            if curr.val < val:
                if not curr.right:
                    curr.right = TreeNode(val)
                else:
                    traverse(curr.right)
            elif curr.val > val:
                if not curr.left:
                    curr.left = TreeNode(val)
                else:
                    traverse(curr.left)
                
        if not root:
            return TreeNode(val)
        traverse(root)
        return root
                

        
