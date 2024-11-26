class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        ans = 0
        for i in range(1,len(nums)+1):
            ans = ans ^ i
        for n in nums:
            ans = ans^n
        return ans
        
