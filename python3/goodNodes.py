# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self, node, mx):
        if not node:
            return 0
        if node.val >= mx:
            count = 1
        else:
            count = 0
        mx = max(mx, node.val)
        count+= self.helper(node.left, mx)
        count+= self.helper(node.right, mx)
        return count


    def goodNodes(self, root: TreeNode) -> int:
        return self.helper(root, float('-inf'))
        
