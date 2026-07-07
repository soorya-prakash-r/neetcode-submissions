class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        l = 0
        for r in range(1,len(nums)):
            if nums[r] in nums[l:r]:
                return nums[r]

            r += 1
