# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        queue = deque([root])
        res = []
        
        while queue:
            last = None
            for _ in range(len(queue)):
                node = queue.popleft()
                if node:
                    last = node.val
                    queue.append(node.left)
                    queue.append(node.right)
                
            if last:
                res.append(last)
        
        return res