class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1 or n == 2:
            return n
        else:
            pp = 1
            p = 2
            for i in range (3,n+1):
                res = p+pp
                pp = p
                p = res
        return res

        
