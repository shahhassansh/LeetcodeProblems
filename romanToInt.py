class Solution:
    def romanToInt(self, s: str) -> int:
        dic = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        ans = 0
        prev = 0
        for i in range(len(s)-1,-1,-1):
            if dic[s[i]] >= prev:
                ans+=dic[s[i]]
            else:
                ans-=dic[s[i]]
            prev = dic[s[i]]
        return ans
