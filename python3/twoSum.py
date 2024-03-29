class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i in range(0,len(nums)):
            if target - nums[i] not in d:
                d[nums[i]] = i
            else:
                return [d[target - nums[i]],i]
