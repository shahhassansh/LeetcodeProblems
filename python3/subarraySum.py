class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prev_sum = 0
        d = {0:1}
        count = 0
        for a in nums:
            prev_sum +=a
            if prev_sum-k in d:
                count += d[prev_sum-k]
            if prev_sum in d:
                d[prev_sum] +=1
            else:
                d[prev_sum] = 1
        return count
    

        
