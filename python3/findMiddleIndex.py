class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if i == 0:
                left = 0
            if i == len(nums)-1:
                right = 0 
            left = sum(nums[:i])
            right = sum(nums[(i+1):])
            if left == right:
                return i 
        return -1
        
