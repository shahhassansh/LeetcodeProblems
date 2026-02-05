class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        dctr = {}
        dctc = {}

        for i in range(len(grid)):
            row = ""
            col = ""
            for j in range(len(grid[0])):
                row = row + '_' + str(grid[i][j])
                col = col + '_' + str(grid[j][i])
            dctr[row] = dctr.get(row,0)+1
            dctc[col] = dctc.get(col,0)+1
        pair = 0
        for x in dctr.keys():
            if x in dctc:
                pair = pair + dctr[x]*dctc[x]
        return pair 
         
        
