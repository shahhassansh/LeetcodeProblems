class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        res = 0 
        i = 0
        while tickets[k] >= 1:
            if tickets[i] >0:
                tickets[i] -= 1
                res+=1
            i+=1
            if i >= len(tickets):
                i = 0
        return res
