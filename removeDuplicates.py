class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0 or len(nums) == 1:
            return len(nums)
        out = 1
        i=1
        for st in range(len(nums)):
            if i < len(nums):
                while nums[i] == nums[st]:
                    i+=1
                    if i>=len(nums):
                        return out
                nums[st+1],nums[i] = nums[i], nums[st+1]
                i+=1
                out+=1
            else:
                break
            
                
        return out
