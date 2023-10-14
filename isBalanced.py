# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root):
        if root is None:
            return 0
        left_height = self.maxDepth(root.left)
        right_height = self.maxDepth(root.right)
        if abs(left_height-right_height) >1:
            return -1
        if left_height == -1:
            return -1
        if right_height == -1:
            return -1
        return 1 + max(self.maxDepth(root.left),self.maxDepth(root.right))
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if self.maxDepth(root) == -1:
            return False
        else:
            return True
