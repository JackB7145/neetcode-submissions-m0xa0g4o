# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(curr):
            if curr:
                right = curr.right.val if curr.right else None
                left = curr.left.val if curr.left else None
                us = curr.val

                if curr.right and curr.left:
                    return right >= left and right >= us and left <= us and dfs(curr.right) and dfs(curr.left)
                elif curr.right:
                    return right >= us and dfs(curr.right)
                elif curr.left:
                    return left <= us and dfs(curr.left)
                else:
                    return True
            return True

        return dfs(root)
                    



                