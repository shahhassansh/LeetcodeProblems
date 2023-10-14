class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]

        out = [[1]]
        for i in range(1,numRows): 
            loc = [1]
            for j in range(1,i):
                loc.append(out[i-1][j-1]+out[i-1][j])
            loc.append(1)
            out.append(loc)
        return out
