class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        if len(strs) == 1:
            return strs[0]
        j = 0
        while 1:
            if len(strs[0]) == 0:
                return ""
            th = strs[0][j]
            for i in range(1,len(strs)):
                if j >= len(strs[i]):
                    return strs[i][0:j]
                if strs[i][j] != th:
                    return strs[i][0:j]
            j+=1
            if j >= len(strs[0]):
                return strs[i][0:j]
