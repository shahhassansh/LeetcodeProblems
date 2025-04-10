class Solution:
    def scoreOfString(self, s: str) -> int:
        prev = ord(s[0])
        out = 0
        for x in s[1:]:
            out = out +  abs(prev - ord(x))
            prev = ord(x)
        return out
