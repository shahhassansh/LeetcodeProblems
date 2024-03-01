class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        m = prices[0]
        out = 0
        for i in range(1,len(prices)):
            if prices[i] <= m:
                m = prices[i]
            else:
                out = max(out, prices[i]-m)
        return out  
