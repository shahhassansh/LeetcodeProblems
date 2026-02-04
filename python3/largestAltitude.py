class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        al = 0
        mx = 0
        for a in gain:
            al += a
            mx = max(mx,al)
        return mx

        
