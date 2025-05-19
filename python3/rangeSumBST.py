# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        s = 0
        def helper(root, low, high):
            nonlocal s
            if not root:
                return
            if root.val >= low and root.val <= high:
                s+=root.val
                helper(root.left, low, high)
                helper(root.right, low, high)
            elif root.val < low:
                helper(root.right, low, high)
            else:
                helper(root.left, low, high)
        helper(root,low, high)
        return s
        
        
