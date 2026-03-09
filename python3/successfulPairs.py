class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        res = [0]*len(spells)
        le = len(potions)
        for i,a in enumerate(spells):
            l = 0 
            r = le -1
            while l <= r:
                m = (l+r)//2
                if a*potions[m] < success:
                    if m == le-1:
                        res[i] = 0
                        break
                    if a*potions[m+1] >= success:
                        res[i] = le - m -1
                        break
                    l = m+1
                else:
                    if m == 0:
                        res[i] = le
                    r = m -1
        return res

        
