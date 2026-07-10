# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        q1 = deque()
        q2 = deque()
        
        if p is None and q is None:
            return True
        if not p or not q:
            return False
            
        q1.append(p)
        q2.append(q)
        
        while q1 and q2:
            x = q1.popleft()
            y = q2.popleft()
            
            if (x.val != y.val) or (x.left is None) ^ (y.left is None) or (x.right is None) ^ (y.right is None):
                return False
            
            if x.left and y.left:
                q1.append(x.left)
                q2.append(y.left)

            if x.right and y.right:
                q1.append(x.right)
                q2.append(y.right)

        if q1 or q2:
            return False
        
        return True