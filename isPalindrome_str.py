class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) <=1:
            return True
        l = 0
        r = len(s)-1
        while l < r:
            if s[l].isalnum() == False:
                l+=1
            elif s[r].isalnum() == False:
                r-=1
            elif s[l].lower() != s[r].lower():
                return False
            else:
                l+=1
                r-=1
        return True
