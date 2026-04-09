# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        temp = deque([root])
        res = []
        level = [0, -1]
        while temp:
            curr = temp.popleft() #Gets the current node
            if curr:
                if level[0] <= 0: #If the momentum is 0 we created a new list
                    res.append([]) #We create the new list in the array
                    level[1] += 1 #We increment the level we are on
                    level[0] = 2 ** level[1] #We calculate our new momentum
                res[level[1]].append(curr.val) #We add the node to the level
                temp.append(curr.left) #We add the left node
                temp.append(curr.right) #We add the right node
            level[0] -= 1 #We decrement the momentum
            
        return res
                

            

            

