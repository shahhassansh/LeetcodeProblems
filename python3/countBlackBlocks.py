class Solution:
    def countBlackBlocks(self, m: int, n: int, coordinates: List[List[int]]) -> List[int]:
        arr = [0,0,0,0,0]
        dct = {}
        for x,y in coordinates:
            for dx,dy in [(-1,-1), (-1,0),(0,-1), (0,0)]:
                nx = x + dx
                ny = y + dy 
                if 0 <= nx < m-1 and 0 <= ny < n-1:
                    if (nx, ny) in dct:
                        dct[(nx, ny)] +=1
                    else:
                        dct[(nx, ny)] = 1
        for a in dct.values():
            arr[a]+=1
        t = (m-1) * (n-1) 
        arr[0] = t - sum(arr[1:])
        return arr


        
