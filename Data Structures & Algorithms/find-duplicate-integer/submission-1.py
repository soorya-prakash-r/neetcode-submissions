class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        for i in range(0, len(nums)):
            if nums[i] in nums[i+1::1]:
                return nums[i]