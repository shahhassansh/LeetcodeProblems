class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        s = sum(nums[:k])
        mx = s/k
        for i in range(k, len(nums)):
            s= s-nums[i-k]+nums[i]
            mx = max(mx, s/k)
        return mx
        
