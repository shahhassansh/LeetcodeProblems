class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        result = []
        for x in nums:
            result = result + list(map(int, str(x)))
        return result
