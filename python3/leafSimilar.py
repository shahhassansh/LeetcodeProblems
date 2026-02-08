# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self, node, arr):
        if not node:
            return arr
        l = node.left
        r = node.right
        if not l and not r:
            arr.append(node.val)
        self.helper(node.left, arr)
        self.helper(node.right, arr)
        return arr
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        return self.helper(root1, []) == self.helper(root2, [])
        

        
