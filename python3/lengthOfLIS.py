class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        helper = [1]*len(nums)
        for i in range(0,len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    helper[i] = max(helper[i],helper[j]+1)
        return max(helper)
