# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0
        def dfs(node, maxi):
            if not node:
                return
            nonlocal count
            if node.val >= maxi:
                maxi = max(maxi, node.val)           
                count += 1
            dfs(node.left, maxi)
            dfs(node.right, maxi)
            return
        
        x = dfs(root, root.val)
        return count