class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        flat = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                flat.append(grid[i][j])
        flat.sort()
        print(flat)
        missing = -1
        for k in range(len(flat)):
            if k == 0:
                if flat[k] != 1:
                    missing = 1
                continue 
            if flat[k] > flat[k-1]+1:
                missing = flat[k-1]+1
            if flat[k-1] == flat[k]:
                repeated = flat[k]
        if missing == -1:
            missing = flat[-1]+1
        return [repeated, missing]
