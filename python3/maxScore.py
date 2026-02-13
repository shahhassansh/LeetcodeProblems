class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        res = 0
        min_heap = []
        merged = []
        for i in range(len(nums1)):
            merged.append((nums2[i],nums1[i]))
        merged.sort(reverse=True)
        s = 0
        for a,b in merged:
            if len(min_heap) == k:
                s = s-heapq.heappop(min_heap)

            s = s + b
            heapq.heappush(min_heap,b)
            if len(min_heap) == k:
                res = max(res, a*s)
        return res

        
