class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 0 or len(s) == 1:
            return s
        longest = 0
        for i in range(1,len(s)):
            start = i-1
            end = i
            while start >=0 and end <len(s) and s[start] == s[end]:
                if end-start+1 > longest:
                    longest = end-start+1
                    ans = s[start:end+1]
                start -=1
                end+=1
            
            start = i-1
            end = i+1
            while start >=0 and end < len(s) and s[start] == s[end]:
                if end-start+1 > longest:
                    longest = end- start+1
                    ans = s[start:end+1]
                start -=1
                end+=1
        if longest == 0:
            return s[0]
        
        return ans
