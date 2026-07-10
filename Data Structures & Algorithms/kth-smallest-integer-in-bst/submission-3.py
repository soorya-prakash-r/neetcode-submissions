# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        q = []

        def dfs(node):
            nonlocal q, k
            if not node:
                return
            
            left = dfs(node.left) 
            if left is not None:
                return left
            q.append(node.val)
            if k == len(q):
                return q[k-1]
            return dfs(node.right)
            
        return dfs(root)