class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        s = {}
        cnt = 0
        for a in nums:
            if k - a in s:
                if s[k-a] > 0:
                    cnt +=1
                    s[k - a] -=1
                else:
                    s[a] = s.get(a,0) + 1
            else:
                s[a] = s.get(a,0) + 1
        return cnt


            
        
