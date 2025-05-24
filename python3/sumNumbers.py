# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        q = []
        q.append(root)
        s = 0
        while q:
            n = q.pop(0)
            if n.left == None and n.right == None:
                s+=n.val
            if n.left:
                n.left.val = (n.val*10) + n.left.val
                q.append(n.left)
            if n.right:
                n.right.val = (n.val*10) + n.right.val
                q.append(n.right)
        return s                
        
