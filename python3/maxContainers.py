class Solution:
    def maxContainers(self, n: int, w: int, maxWeight: int) -> int:
        c = n*n
        if w*c < maxWeight:
            return c
        else:
            return maxWeight//w
        
