# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        #Right off rip, Im thinking a dfs, with each level having access to a largest value if its come accross in the path to the root
        #Note that the root will always be a 1
        res = 1

        def dfs(curr, highest):
            nonlocal res
            if curr:
                if curr.val >= highest:
                    highest = curr.val
                    res += 1
                dfs(curr.left, highest)
                dfs(curr.right, highest)
        
        dfs(root, root.val)
        return res
        