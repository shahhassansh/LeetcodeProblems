class SparseVector:
    def __init__(self, nums: List[int]):
        self.v = nums
        

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        res = 0
        for i in range(len(self.v)):
            print(i)
            print(self.v[i])
            print(vec.v[i])
            res += (self.v[i] * vec.v[i])
        return res

        

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)
