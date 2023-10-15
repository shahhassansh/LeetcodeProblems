class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        out = ""
        a = columnNumber
        while a:
            a = a-1
            r = a%26
            c = chr(65+r)
            out = c + out
            a = a //26
        return out
