class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        res = 0
        x = len(pref)
        for a in words:
            if a[:x] == pref:
                res+=1
        return res

        
