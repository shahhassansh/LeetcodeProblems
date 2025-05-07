class Solution:
    def reverseDegree(self, s: str) -> int:
        sm = 0
        for i in range (len(s)):
            rev = 26-(ord(s[i])-97)
            sm+= (rev*(i+1))
        return sm

        
