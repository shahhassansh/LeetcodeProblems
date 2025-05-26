class Solution:
    def minDeletion(self, s: str, k: int) -> int:
        dct = {}
        for a in s:
            if a in dct:
                dct[a]+=1
            else:
                dct[a] = 1
        dct = dict(sorted(dct.items(), key= lambda item:item[1], reverse=True))
        l = list(dct.values())
        return len(s) - sum(l[:k])
        
        
