# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        res=[]
        def dfs(curr):
            nonlocal res
            if curr:
                res.append(str(curr.val))
                dfs(curr.left)
                dfs(curr.right)
            else:
                res.append("None")
        dfs(root)
        return ",".join(char for char in res)

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        data = data.split(',')
        index = 0
        def dfs(curr):
            nonlocal index
            if curr == 'None':
                return None
            else:
                node = TreeNode(int(curr))
                index += 1
                node.left = dfs(data[index])
                index += 1
                node.right = dfs(data[index])
                return node
        if data:
            return dfs(data[0])
            

