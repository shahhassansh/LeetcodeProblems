import collections
class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        if not rooms:
            return rooms
        q = collections.deque()
        r = len(rooms)
        c = len(rooms[0])
        for i in range(r):
            for j in range(c):
                if rooms[i][j] == 0:
                    q.append((i,j))
        d = [(-1,0),(1,0),(0,1),(0,-1)]
        while q:
            x,y = q.popleft()
            print(str(x)+' '+str(y))
            distance = rooms[x][y] + 1
            for dx,dy in d:
                new_x = x+dx
                new_y = y+dy
                print(str(new_x)+' '+str(new_y))
                if 0<=new_x<r and 0<=new_y<c:
                    if rooms[new_x][new_y] == 2147483647:
                        rooms[new_x][new_y] = distance
                        q.append((new_x,new_y))
        return rooms


        
        
