class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        lon = 1
        max_lon = 1
        for i in range(1,len(nums)):
            if nums[i] > nums[i-1]:
                lon = lon+1
                max_lon = max(max_lon,lon)
            else:
                lon = 1  
        ln = 1
        max_ln = 1
        for i in range(1,len(nums)):
            if nums[i] < nums[i-1]:
                ln =  ln+1
                max_ln = max(max_ln,ln)
            else:
                ln = 1
        return max(max_lon, max_ln) 
        
