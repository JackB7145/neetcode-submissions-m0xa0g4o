# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
    #           1
    #       N       2
    #           3      4
    #        N     5      N
    #           6
    #The diameter is the pathlength it takes to get from the deepest 1 on the left to the deepest 1 on the right

        def findMaxDepth(curr): #Recursive function takes in the current node as a parameter
            if curr: #Ensuring that the current node has both a left and right child to prevent errors

                val = 1 + max(findMaxDepth(curr.left), findMaxDepth(curr.right))
                print(val, curr.val)
                return val #If curr is a tree node we find the maximum depth of both the left and right, and take the higher one, incrementing the depth (1 + ...) for every recursive level
            return 0 #If the current node is none we return 0 for this node
        
        return findMaxDepth(root)