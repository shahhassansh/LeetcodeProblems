class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1 or grid[len(grid)-1][len(grid)-1] ==1:
            return -1
        
        q = []
        q.append((0,0,1))
        visited = set()
        visited.add((0,0))

        neighbors = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1),(1,0),(1,1)]
        while q:
            x,y,length = q.pop(0)
            if x == len(grid) -1 and y == len(grid) -1:
                return length 
            for dx,dy in neighbors:
                if x+dx >= 0 and y+dy >= 0 and x+dx < len(grid) and y+dy < len(grid) and grid[x+dx][y+dy] == 0 and (x+dx,y+dy) not in visited:
                    q.append((x+dx, y+dy, length+1))
                    visited.add((x+dx,y+dy)) 
        return -1


        
