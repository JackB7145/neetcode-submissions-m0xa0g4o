# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def dfs(curr):
            if curr:
                if curr.val == subRoot.val:
                    if curr.left and curr.right and curr.left.val == subRoot.left.val and curr.right.val == subRoot.right.val and not curr.left.left and not curr.right.right:
                        return True
                if dfs(curr.left):
                    return True
                if dfs(curr.right):
                    return True
            else:
                return False

        if dfs(root):
            return True
        return False