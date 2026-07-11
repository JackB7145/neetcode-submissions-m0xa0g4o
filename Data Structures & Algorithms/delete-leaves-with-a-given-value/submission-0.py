# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        dummy = TreeNode()
        dummy.right = root
        def traverse(curr):
            if not curr:
                return False

            left = traverse(curr.left)
            right = traverse(curr.right)

            if left:
                curr.left = None
            
            if right:
                curr.right = None

            if curr.val == target and not curr.left and not curr.right:
                return True

            return False

        traverse(dummy)
        return dummy.right
