# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        q = deque()
        q.append(root)
        if not root:
            return "-1"

        res = [str(root.val)]
        while q:
            x = q.popleft()
            if x.left:
                q.append(x.left)
                res.append(str(x.left.val))
            else:
                res.append("-1")
            if x.right:
                q.append(x.right)
                res.append(str(x.right.val))
            else:
                res.append("-1")
        
        return ",".join(res)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        res = data.split(",")
        q = deque()
        if int(res[0]) == -1:
            return None
        root = TreeNode(int(res[0]))
        q.append(root)
        index = 0
        print(res)
        while q:
            x = q.popleft()
            if x is None:
                continue

            if index+1 < len(res) and int(res[index+1]) != -1:
                x.left = TreeNode(int(res[index+1]))
            else:
                x.left = None
            
            if index+2 < len(res) and int(res[index+2]) != -1:
                x.right = TreeNode(int(res[index+2]))
            else:
                x.right = None

            q.append(x.left)
            q.append(x.right)
            index += 2

        return root