class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                nums[i] = 2 * nums[i]
                nums[i+1] = 0
        print(nums)
        for i in range(len(nums)):
            c = i
            if nums[c] == 0:
                c+=1
                while c< len(nums) and nums[c] == 0:
                    c+=1
                if c < len(nums):
                    nums[i] = nums[c]
                    nums[c] = 0
                else:
                    return nums
        return nums 


        
