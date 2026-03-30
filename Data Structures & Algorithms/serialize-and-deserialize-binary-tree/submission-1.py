# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        res = []
        def traverse(curr):
            if not curr:
                res.append("None")
                return
            res.append(str(curr.val))
            traverse(curr.left)
            traverse(curr.right)
        traverse(root)
        return '_'.join(res)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        vals = data.split('_')
        idx = 0

        def traverse():
            nonlocal idx
            if vals[idx] == "None":
                idx += 1
                return None
            
            node = TreeNode(int(vals[idx]))
            idx += 1
            node.left = traverse()
            node.right = traverse()
            return node

        return traverse()
