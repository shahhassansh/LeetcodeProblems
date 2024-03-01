class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:
            return 0
        if nums[0] >= target:
            return 0
        if nums[len(nums)-1] < target:
            return len(nums)
        l = 0
        r = len(nums)-1
        m = (l+r)//2
        while l <= r:
            if nums[m] >= target and nums[m-1] < target:
                return m
            elif nums[m] < target:
                l=m+1
            else:
                r =m
            m = (l+r)//2 
