class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height)-1
        out = 0
        while left < right:
            x = min(height[left],height[right])*(right-left)
            out = max(out,x)
            if height[left]<height[right]:
                left+=1
            else:
                right-=1
        return out
