class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        dct = {}
        for a in s:
            if a in dct:
                dct[a] +=1
            else:
                dct[a] = 1
        for b in t:
            if b not in dct:
                return False
            if dct[b] == 0:
                return False
            dct[b] -=1
            if dct[b] == 0:
                del dct[b] 
        return True
