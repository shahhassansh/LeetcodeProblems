class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        i = 0
        j = 1
        mx = 1
        while j < len(s):
            st = set(s[i:j])
            if s[j] in st:
                j+=1
            else:
                if len(st) == 1:
                    j+=1   
                else:
                    i+=1
            mx = max(mx, j-i)
        return mx

        
