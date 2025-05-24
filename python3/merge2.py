class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = [intervals[0]]
        for a in intervals[1:]:
            if a[0] <= res[-1][1]:
                res[-1][0] = min(res[-1][0], a[0])
                res[-1][1] = max(res[-1][1], a[1])
            else:
                res.append(a)
        return res
        
