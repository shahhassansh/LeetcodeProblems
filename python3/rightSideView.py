# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        out = []
        q = []
        q.append((root, 0))
        while q:
            n,v = q.pop(0)
            if len(out) -1 >= v:
                out[v] = n.val
            else:
                out.append(n.val)
            if n.left:
                q.append((n.left,v+1))
            if n.right:
                q.append((n.right,v+1))
        return out
            

        
