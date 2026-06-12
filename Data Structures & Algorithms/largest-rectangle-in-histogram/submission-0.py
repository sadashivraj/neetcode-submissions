class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        area = 0

        for idx,height in enumerate(heights):
            start = idx
            while stack and stack[-1][1] > height:
                curr_idx, curr_height = stack.pop()
                area = max(area, curr_height*(idx-curr_idx))
                start = curr_idx
            stack.append((start, height))
        
        for i,h in stack:
            area = max(area, h*(len(heights)-i))

        return area
