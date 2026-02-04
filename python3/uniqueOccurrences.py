class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        dct = {}
        for a in arr:
            dct[a] = dct.get(a,0)+1
        s = set()
        for x in dct.keys():
            if dct[x] in s:
                return False
            s.add(dct[x])
        return True

        
