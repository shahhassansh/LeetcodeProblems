# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        def traverse(self, root, path):
            if not root:
                return 
            path.append(str(root.val))
            if not root.left and not root.right:
                paths.append('->'.join(path))
            else:
                traverse(self, root.left, path[:])
                traverse(self, root.right, path)
        paths = []
        traverse(self, root, [])
        return paths
        
        
