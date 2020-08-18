class Solution:
    def reverse(self, x: int) -> int:

        if x < 0:
            neg = -1
            x = -1 * x
        else:
            neg = 1
        mul = 1
        ans = 0
        while x >0:
            r = x%10
            ans = (ans*10) + r
            x = x//10
        if ans > (2**31) -1:
            return 0
        ans = ans * neg
        return ans
