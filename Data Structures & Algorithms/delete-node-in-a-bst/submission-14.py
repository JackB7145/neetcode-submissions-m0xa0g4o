class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:

        def findNode(curr, parent):
            if not curr:
                return None
            
            if curr.val == key:
                return curr, parent
            
            if key < curr.val:
                return findNode(curr.left, curr)
            else:
                return findNode(curr.right, curr)

        found = findNode(root, None)
        if not found:
            return root
        
        removeNode, parent = found

        leftTree = removeNode.left
        rightTree = removeNode.right

        # CASE 1: no right subtree → just return left
        if not rightTree:
            if not parent:
                return leftTree
            if parent.left == removeNode:
                parent.left = leftTree
            else:
                parent.right = leftTree
            return root

        # CASE 2: attach left subtree to leftmost node of right subtree
        curr = rightTree
        while curr.left:
            curr = curr.left
        
        curr.left = leftTree

        # connect parent to rightTree
        if not parent:
            return rightTree

        if parent.left == removeNode:
            parent.left = rightTree
        else:
            parent.right = rightTree

        return root