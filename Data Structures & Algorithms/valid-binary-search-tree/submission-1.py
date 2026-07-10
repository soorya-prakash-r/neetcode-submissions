# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return False
        flag = True
        def dfs(node, mini, maxi):
            nonlocal flag
            if not node:
                return

            if not mini < node.val < maxi:
                flag = False
            
            dfs(node.left, mini, node.val)
            dfs(node.right, node.val, maxi)
            return flag

        return dfs(root, float("-inf"), float("inf"))