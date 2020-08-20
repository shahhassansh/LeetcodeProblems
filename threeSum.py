class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        out = []
        vis = set()
        nums.sort()
        for i in range(0,len(nums)-2):
            if i != 0 and nums[i-1] == nums[i]:
                continue
            j = i+1
            k = len(nums)-1
            while j <k:
                s = nums[i] + nums[j] + nums[k]
                if s == 0:
                    out.append([nums[i], nums[j], nums[k]])
                    a = nums[k]
                    j+=1
                    k-=1
                    while nums[k] == a and k>=0:
                        k-=1
                elif s < 0:
                    j+=1
                elif s >0:
                    k-=1
        return out
            
