# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        '''
        At every single node the left becomes the right

        I'm thinking preorder traversal, swap left and right pointers then move left and right
        '''
        def recurse(curr):
            if not curr:
                return
            
            temp = curr.right
            curr.right = curr.left
            curr.left = temp

            recurse(curr.left)
            recurse(curr.right)
        
        recurse(root)
        return root
            