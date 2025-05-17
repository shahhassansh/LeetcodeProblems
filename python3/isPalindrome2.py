class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0 
        r = len(s)-1
        while l < r:
            if not s[l].isalnum():
                l+=1
            elif not s[r].isalnum():
                r-=1
            elif s[l].lower() != s[r].lower():
                return False
            else:
                r-=1
                l+=1
        return True



    
        
