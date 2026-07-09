class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = None
        count = 0

        def traverse(curr):
            nonlocal res, count
            if not curr or res is not None:
                return
            
            # left
            traverse(curr.left)

            # node
            count += 1
            if count == k:
                res = curr.val
                return

            # right
            traverse(curr.right)

        traverse(root)
        return res