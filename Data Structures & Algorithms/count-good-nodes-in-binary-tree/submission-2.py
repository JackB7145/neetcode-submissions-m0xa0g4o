# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0
        def traverse(curr, largest):
            nonlocal res
            if curr:
                if curr.val >= largest:
                    res += 1
                    largest = curr.val
                traverse(curr.left, largest)
                traverse(curr.right, largest)
            
        traverse(root, float('-inf'))
        return res


'''
    3
   3 null
 4  2


'''