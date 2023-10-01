class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l = 0
        r = len(nums)-1
        mid = (l+r)//2
        out = [-1,-1]
        while l<=r:
            if nums[mid] > target:
                r = mid -1
            elif nums[mid] < target:
                l = mid +1
            else:
                out[0] = mid
                r = mid-1
            mid = (l+r)//2

        l = 0
        r = len(nums)-1
        mid = (l+r)//2
        rgt_most = -1
        while l<=r:
            if nums[mid] > target:
                r = mid -1
            elif nums[mid] < target:
                l = mid +1
            else:
                out[1] = mid
                l = mid+1
            mid = (l+r)//2
        return out
			
