class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        out = 0
        for x in columnTitle:
            out = out*26+ (ord(x)-64)
        return out
