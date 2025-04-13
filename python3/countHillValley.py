class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        nums2 = []
        nums2.append(nums[0])
        for i in range(1,len(nums)):
            if nums[i] != nums2[-1]:
                nums2.append(nums[i])
        print(nums2)
        res = 0
        for i in range(1, len(nums2)-1):
            if nums2[i] > nums2[i-1] and nums2[i] > nums2[i+1]:
                res+=1
            elif nums2[i] < nums2[i-1] and nums2[i] < nums2[i+1]:
                res+=1
        return res
        
