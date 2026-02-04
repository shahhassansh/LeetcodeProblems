class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        rightSum = sum(nums[1:])
        leftSum = 0
        for i in range(1,len(nums)):
            if rightSum == leftSum:
                return i-1
            rightSum -= nums[i]
            leftSum += nums[i-1]
        if leftSum == rightSum:
            return len(nums)-1

        return -1

        
