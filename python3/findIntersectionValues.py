class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        output = []
        nums1_s = set(nums1)
        nums2_s = set(nums2)
        a = 0
        for x in nums1:
            if x in nums2_s:
                a+=1
        b = 0
        for x in nums2:
            if x in nums1:
                b+=1

        return [a,b]

        
