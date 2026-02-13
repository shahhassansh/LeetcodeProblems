class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 1 or (nums[0] > nums[1]):
            return 0
        l = 0
        r = len(nums)-1
        
        while l < r:
            i = (l+r)//2
            if (i == 0 and nums[i] > nums[i+1]) or (i == len(nums)-1 and nums[i] > nums[i-1]):
                return i
            elif i == 0:
                l = i+1
            elif i == len(nums)-1:
                r = i-1
            if nums[i-1] < nums[i] and nums[i] > nums[i+1]:
                return i
            if nums[i-1] > nums[i]:
                r = i-1
            else:
                l = i+1
        return l

        
