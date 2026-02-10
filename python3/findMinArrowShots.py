class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        res = 1
        points.sort()
        prevEnd = points[0][1]


        for i in range(1,len(points)):
            if points[i][0] > prevEnd:
                res +=1
                prevEnd = points[i][1]
            else:
                prevEnd = min(points[i][1], prevEnd)
        return res

        
