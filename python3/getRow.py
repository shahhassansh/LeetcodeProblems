class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        prev = [1]
        for i in range(1,rowIndex+1):
            loc = [1]
            for j in range(1,i):
                loc.append(prev[j-1]+prev[j])
            loc.append(1)
            prev = loc
        return loc
