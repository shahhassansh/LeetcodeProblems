class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        pref = nums[0]
        x = 1
        for i in range(1,len(nums)):
            if nums[i] == nums[i-1]+1:
                pref+=nums[i]
            else:
                x = i
                break
        nums.sort()
        for x in nums:
            if pref == x:
                pref+=1
            elif pref < x:
                return pref
        return pref
        
