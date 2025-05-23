class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        res = []
        for i in range(len(heights)-1, -1,-1):
            if i == len(heights)-1:
                res.append(i)
                prev_max = heights[i]
            elif heights[i] > prev_max:
                res.append(i)
                prev_max = heights[i]
        return res[::-1]


        
