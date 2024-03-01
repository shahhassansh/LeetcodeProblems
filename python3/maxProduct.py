class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        global_max = nums[0]
        prev_max = nums[0]
        prev_min = nums[0]
        for x in nums[1:]:
            curr_min = min(prev_min*x,prev_max*x,x)
            curr_max = max(prev_min*x,prev_max*x,x)
            global_max = max(global_max, curr_max)
            prev_max = curr_max
            prev_min = curr_min
        return global_max
