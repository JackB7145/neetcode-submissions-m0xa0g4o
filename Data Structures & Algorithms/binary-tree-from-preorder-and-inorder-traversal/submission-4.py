class Solution:
    def buildTree(self, preorder, inorder):
        index_map = {val: i for i, val in enumerate(inorder)}

        def build(preIdx, leftBound, rightBound):
            if leftBound > rightBound:
                return None

            root_val = preorder[preIdx]
            root = TreeNode(root_val)

            inorder_idx = index_map[root_val]
            left_size = inorder_idx - leftBound

            root.left = build(preIdx + 1, leftBound, inorder_idx - 1)
            root.right = build(preIdx + 1 + left_size, inorder_idx + 1, rightBound)

            return root

        return build(0, 0, len(inorder) - 1)