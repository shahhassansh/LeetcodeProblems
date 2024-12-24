class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        dct = {}
        l = 0
        r = 0
        maxl = 0
        ans = 0
        for r in range(len(s)):
            dct[s[r]] = 1+dct.get(s[r],0)
            maxl = max(maxl, dct[s[r]])

            if (r-l+1) - maxl > k:
                dct[s[l]]-=1
                l+=1
            ans = max(ans, r-l+1)
        return ans 
        
