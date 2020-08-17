class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_dict = dict()
        arr = []
        for i in range(0,len(nums)):
            k = target - nums[i]
            if k in my_dict:
                arr.append(my_dict[k])
                arr.append(i)
                return arr
            else:
                my_dict[nums[i]] = i
