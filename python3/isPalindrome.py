class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        x2 = x
        outp = 0
        while x2 >0:
            outp = outp*10 + x2%10
            x2 = x2//10
        if outp == x:
            return True
        else:
            return False
