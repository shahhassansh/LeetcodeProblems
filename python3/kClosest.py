class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        for a in points:
            dist = a[0]**2 + a[1]**2
            a.append(dist)
        a_sorted = sorted(points, key=lambda x: x[2])
        res = []
        i = 0
        for x in range(k):
            res.append([a_sorted[i][0],a_sorted[i][1]])
            i+=1
        return res


        
