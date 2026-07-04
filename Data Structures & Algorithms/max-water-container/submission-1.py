class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        cap = 0
        h = height[0]

        while l < r:
            if height[l] < height[r]:
                cap = max(cap, height[l]*(r-l))
                l += 1
            else:
                cap = max(cap, height[r]*(r-l))
                r -= 1

        return cap

        