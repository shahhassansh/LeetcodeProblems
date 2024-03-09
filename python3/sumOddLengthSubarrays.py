class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        s = sum(arr)
        sz = 3
        while sz <= len(arr):
            for i in range(0,len(arr)-sz+1):
                s += sum(arr[i:i+sz])
            sz+=2
        return s
