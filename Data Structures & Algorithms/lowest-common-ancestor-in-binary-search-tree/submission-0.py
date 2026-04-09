# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        #The LCA between two nodes Is the node that connects both of them
        #From my understanding, in the example, 3 is the common ancestor since, it is both one of the values we are looking for and, connects with the other node
        #So for each step, we need to determine whether or not the substeps have 4 or 3 in it 
        #First use dfs to search the left and right subtrees of the node for the two nodes p and q
        #If true : set the nonlocal feild to that it reflects the current node valie
        #elif false : 
            #Check the current value to see if its either p or q:
            #If this is true and at least 1 of the numbers of p or q were found in the left or right subtree, set the nonLocal to our curr.val
            #else:
                #dfs(curr.left) and dfs(curr.right)
        ancestor = root
        def dfs(curr):
            if curr:
                nonlocal ancestor
                isLeft = dfs(curr.left) #Look Left
                isRight = dfs(curr.right) #Look Right
                if isLeft and isRight: #If both the left and right then set ancestor
                    ancestor = curr #Setting ancestor
                    return False 
                elif curr.val == p.val or curr.val == q.val and isLeft or isRight: #If the current value is either p or q and left or right has p or q in it 
                    ancestor = curr #Setting the ancestor
                    return False
                elif curr.val == p.val or curr.val == q.val: #The baseline, if the current value is p or q, then we return True
                    return True
                elif isLeft and not isRight or isRight and not isLeft: #We get the recursion first before the control statements, therefore we need to send the recursive chain up if we found something below in one of the right or left
                    return True
                else:
                    return False #Pointless node
            return False #None node

        dfs(root)
        return ancestor
