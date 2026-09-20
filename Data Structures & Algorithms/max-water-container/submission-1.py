class Solution:
    def maxArea(self, heights: List[int]) -> int:
        start, end = 0, len(heights)-1
        amount_water = 0
        while end > start:
            amount_water = max(amount_water, (end-start) * min(heights[start], heights[end]))
            if heights[start] < heights[end]:
                start += 1
            elif heights[end] < heights[start]:
                end -= 1
            else:
                start += 1
                end -= 1
        return amount_water
        