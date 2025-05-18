class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        hp = []
        for a in nums:
            heapq.heappush(hp,a)
            if len(hp) > k:
                heapq.heappop(hp)
        return hp[0]
