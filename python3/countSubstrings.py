class Solution:
    def countSubstrings(self, s: str) -> int:
        cnt = 0
        for i in range(0,len(s)):
            cnt += self.helper(s,i,i)
            cnt += self.helper(s,i-1,i)
        return cnt

    def helper(self, s, l, r):
        ct = 0
        while l>= 0 and r<len(s) and s[r] == s[l]:
            ct+=1
            l-=1
            r+=1
        return ct

        
