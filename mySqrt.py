class Solution:
    def mySqrt(self, x: int) -> int:
        if x in (0,1):
            return x
        l = 0
        r = x
        m = (l+r)//2
        while l < r:
            if m*m <= x and (m+1)*(m+1)>x:
                return m
            elif m*m < x:
                l = m
            elif m*m > x:
                r = m
            m = (l+r)//2

