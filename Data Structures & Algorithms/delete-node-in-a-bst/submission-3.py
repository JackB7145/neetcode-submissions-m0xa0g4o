# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        '''
        3 cases:

        1. We search the tree and don't find the node
        2. We search the tree and find the node
            2a. The node is a leaf node
            2b. The node is a parent node

        design a search algorithm o(n) time complexity -> Check if parent is val, then search children in preorder dfs traversal

        when we find the node ...?

        We check to see if its a leaf node with not left and not right == Leaf node. So we just delete it

        If its not a leaf node ... 

        1. set right node to current and left node to left child
        2. Just set left node 


        Possible Solution:

        1. Linearly scan the tree, find the node, do the above checks

        but keep a counter of the parent node reference

        Issue, its a bst, and the only reason 4 is placed there is because its less than 5??

        and 1 makes sense
    

        I can reinsert them but is that the process?

        I reinsert 1 and 4, and do I reinsert all of the child nodes?


        '''
        if root.val == key:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            root.right.left = root.left
            return root.right

        def traverse(curr, parent):
            if not curr:
                return
            
            if curr.val == key:
                print(curr.val, curr.left.val, curr.right.val)
                if curr == parent.left:
                    if curr.right:
                        parent.left = curr.right
                        parent.left.left = curr.left
                    else:
                        parent.left = curr.left
                else:
                    if curr.left:
                        parent.right = curr.left
                        curr.right.right = curr.right
                    else:
                        parent.right = curr.right

                return
            
            traverse(curr.left, curr)
            traverse(curr.right, curr)
        
        traverse(root, None)
        return root


            