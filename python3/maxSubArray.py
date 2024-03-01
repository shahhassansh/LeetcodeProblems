class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        summ = 0
        ans = nums[0]
        for i in range(0,len(nums)):
            if summ+nums[i] <0:
                summ = 0
                ans = max(ans,nums[i])
            else:
                summ+=nums[i]
                ans = max(ans,summ)
        return ans
