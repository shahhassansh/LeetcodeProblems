class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dct = {}
        for x in strs:
            a = sorted(x)
            a = ''.join(a)
            if a not in dct:
                dct[a] = [x]
            else:
                dct[a].append(x)
        res = []
        for y in dct.values():
            res.append(y)
        return res
