class Solution:
    def trap(self, height: List[int]) -> int:

        minLeftRight = [0] * len(height)
        maxi = height[0]
        for i in range(1, len(height)):
            minLeftRight[i] = maxi
            maxi = max(maxi, height[i])
        maxi = 0
        minLeftRight[-1] = 0
        for i in range(len(height)-1, -1, -1):
            minLeftRight[i] = min(maxi, minLeftRight[i])
            maxi = max(maxi, height[i])

        result = []
        for i in range(0, len(height)):
            x = minLeftRight[i] - height[i]
            if x > 0:
                result.append(x)
        print(minLeftRight)
        return sum(result)

