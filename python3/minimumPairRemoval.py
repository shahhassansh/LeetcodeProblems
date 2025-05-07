

class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        mn = float('inf')
        r = 0
        pop = 0
        while nums != sorted(nums):
            for i in range(len(nums)-1):
                if nums[i]+nums[i+1] < mn:
                    pop = i 
                    mn = nums[i]+nums[i+1]
            r +=1
            nums.pop(pop)
            nums[pop] = mn
            mn = float('inf')
            pop = 0
        return r

                


                


        
