# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        d = {}
        q = []
        q.append((root, 0))

        while q:
            node, x = q.pop(0)
            if node:
                if x not in d:
                    d[x] = [node.val]
                elif x in d:
                    d[x].append(node.val)
                if node.left:
                    q.append((node.left, x-1))
                if node.right:
                    q.append((node.right, x+1))
        d = dict(sorted(d.items(), key=lambda item:item[0]))
        return list(d.values())
        




        
