# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0

        def dfs(curr, highest):
            nonlocal res
            if curr:
                if curr.val >= highest:
                    res += 1
                    highest = curr.val
                dfs(curr.left, highest)
                dfs(curr.right, highest)

        dfs(root, root.val)
        return res
