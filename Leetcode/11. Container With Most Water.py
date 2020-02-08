class Solution:
    def maxArea(self, height: List[int]) -> int:
        beg = 0
        end = len(height) - 1
        maxArea = 0
        while beg < end:
            if min(height[beg],height[end]) * (end - beg) > maxArea:
                maxArea = min(height[beg],height[end]) * (end - beg)
            if height[beg] >= height[end]:
                end -= 1
            else:
                beg += 1
                
        return maxArea