class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        out = ""
        mn = min(len(word1),len(word2))
        for i in range(mn):
            out = out + word1[i] + word2[i]
        if len(word1) > mn:
            return out+word1[mn:]
        else:
            return out+word2[mn:]
        
