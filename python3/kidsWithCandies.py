class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        out = [""] * len(candies)
        mx = max(candies)
        for i in range(len(candies)):
            if candies[i] + extraCandies >= mx:
                out[i] = True
            else:
                out[i] = False
        return out
        
