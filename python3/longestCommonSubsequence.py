class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        row = len(text2)+1
        col = len(text1)+1
        m = [[0 for j in range(col)] for i in range(row)]
        for i in range(1,row):
            for j in range(1,col):
                if text1[j-1]==text2[i-1]:
                    m[i][j] =m[i-1][j-1]+1
                else:
                    m[i][j] = max(m[i-1][j],m[i][j-1])
        print(m)
        return m[-1][-1]
                    
