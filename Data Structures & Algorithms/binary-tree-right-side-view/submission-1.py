# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        #On each depth, the very right side node should be added to a list
        #The deepest one, on the right side, is what we have to add
        #Look left and right for the deeper trees, if the deeper one is on the right, just do that one
        #Otherwise go until it finishes, and then go to the deeper one after 

        #Solution Idea1:

        #After reviewing a previous solution I have a intuitive fool proof one. In, level order traversal, we use a technique that ensures that we only operate on a per level basis. I'm just going to take the right one and add the node to a list and first try it

        q = deque([root])
        res = []
        while q:
            length = len(q)
            temp = None
            for _ in range(length):
                node = q.popleft()
                if node:
                    temp = node
                    q.append(node.left)
                    q.append(node.right)
            if node:
                res.append(node.val)
            elif temp:
                res.append(temp.val)

        return res