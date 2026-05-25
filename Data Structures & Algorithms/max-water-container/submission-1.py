class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        max_c = 0
        while l<r:
            height = min(heights[l], heights[r])
            width = r-l
            area = height*width
            max_c = max(max_c, area)
            if heights[l]>heights[r]:
                r-=1
            else:
                l+=1
        return max_c