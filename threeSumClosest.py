class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        cl = 100000
        for i in range(len(nums)-2):
            j = i+1
            k = len(nums)-1
            while j <k:
                s = nums[i] + nums[j] + nums[k]
                if abs(target-s) < cl:
                    cl = abs(target-s)
                    f_s = s
                elif s < target:
                    j+=1
                else:
                    k-=1
                
        return f_s
