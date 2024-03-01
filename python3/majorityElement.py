class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        
        for a in nums:
            if count == 0:
                candidate = a
                count+=1
            elif a == candidate:
                count+=1
            else:
                count-=1
        return candidate
