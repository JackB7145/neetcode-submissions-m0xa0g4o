# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        queue = deque()
        queue.append(p)
        queue.append(q)
        while queue:
            print(queue)
            if queue[0] and queue[1] and queue[0].val == queue[1].val:
                queue.append(queue[0].left)
                queue.append(queue[1].left)
                queue.append(queue[0].right)
                queue.append(queue[1].right)
            elif not queue[0] and not queue[1]:
                pass
            else:
                return False
            queue.popleft()
            queue.popleft()
        return True