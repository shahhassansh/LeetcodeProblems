class Solution:
    def canFinish(self, piles, k, h):
        hours = 0
        for p in piles:
            hours += p//k
            if p%k != 0:
                hours +=1
            if hours > h:
                return False
        return True

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1 
        r = max(piles)
        while l<=r:
            m = (l+r)//2
            if self.canFinish(piles, m, h):
                ans = m
                r = m-1
            else:
                l = m +1
        return ans

        
