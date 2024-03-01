# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        in_or = []
        curr = root
        def inorder(curr):
            if curr is None:
                return
            inorder(curr.left)
            in_or.append(curr.val)
            inorder(curr.right)
        inorder(curr)
        return in_or
