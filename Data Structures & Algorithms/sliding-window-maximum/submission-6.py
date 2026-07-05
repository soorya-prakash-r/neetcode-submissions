class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        if k == 1:
            return nums
        l = 0
        maxi = 0
        i = 0
        temp = deque()
        for r in range(0, len(nums)):
            maxi = max(maxi, nums[r])
            if r-i+1 == k:
                res.append(maxi)
                i += 1
                maxi = max(nums[i:r+1:1])
                print(maxi)

        return res