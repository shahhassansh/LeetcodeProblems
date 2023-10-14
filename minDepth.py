# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self,root):
        if root is None:
            return float('inf')
        if root.left is None and root.right is None:
            return 1
        return min(self.helper(root.left),self.helper(root.right))+1
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        return self.helper(root)
        
