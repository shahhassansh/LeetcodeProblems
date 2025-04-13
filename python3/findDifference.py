class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        set1 = set(nums1)
        set2 = set(nums2)
        f = set()
        s = set()
        for a in nums1:
            if a not in set2:
                f.add(a)
        for a in nums2:
            if a not in set1:
                s.add(a)
        return [list(f),list(s)]
        
