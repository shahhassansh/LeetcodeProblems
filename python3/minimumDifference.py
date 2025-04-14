class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        if k == 1:
            return 0
        m = float('inf')
        nums.sort()
        for i in range(len(nums)-k+1):
            m = min(m, max(nums[i:i+k]) - min(nums[i:i+k]))
        return m



        
