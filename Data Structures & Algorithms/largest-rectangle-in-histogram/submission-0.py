class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxi = 0
        index = 0
        for i in range(0, len(heights)):
            index = i
            while stack and stack[-1][1] >= heights[i]:
                x = stack.pop()
                maxi = max(maxi, x[1] * (i - x[0]))
                index = x[0]
            stack.append([index, heights[i]])
        i += 1
        for x in stack:
            maxi = max(maxi, x[1] * (i - x[0]))
            
        return maxi