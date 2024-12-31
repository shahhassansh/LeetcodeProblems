# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        q= []
        curr = root
        q.append(curr)
        res = []
        nq = []
        while len(q) > 0:
            tmp = []
            for i in range(len(q)):
                curr = q[0]
                tmp.append(curr.val)
                q.pop(0)
                if curr.left:
                    nq.append(curr.left)
                if curr.right:
                    nq.append(curr.right)
            res.append(tmp)
            q = nq
        return res


        
