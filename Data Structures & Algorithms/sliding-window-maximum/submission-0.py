class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        l = 0
        maxi = 0
        i = 0
        temp = []
        for r in range(0, len(nums)):
            temp.append(nums[r])
            if len(temp) == k:
                res.append(max(temp))
                temp.pop(0)

        return res