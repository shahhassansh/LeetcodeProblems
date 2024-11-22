"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        q = deque()
        q.append(node)
        nodes = {}
        visited = set()
        while q:
            tmp = q.popleft()
            if tmp in visited:
                continue
            visited.add(tmp)
            nodes[tmp.val] = []
            for x in tmp.neighbors:
                nodes[tmp.val].append(x.val)
                q.append(x)
        print(nodes)

        copied_nodes = {}
        for nd in nodes:
            copied_nodes[nd] = Node(nd)

        for nd in nodes:
            ac = copied_nodes[nd]
            ac.neighbors = []
            for y in nodes[nd]:
                ac.neighbors.append(copied_nodes[y])

        return copied_nodes[node.val]

        
