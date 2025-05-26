class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        st = strs[0]
        for i in range(1,len(strs)):
            x = min(len(st),len(strs[i]))
            st = st[:x]
            for j in range(x): 
                if strs[i][j] != st[j]:
                    st = strs[i][:j]
                    break
                
        return st

        
