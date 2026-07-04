class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        count = 0
        for i in nums:
            if i-1 not in set(nums):
                length = 1
                while i+length in set(nums):
                    length += 1
                count = max(count, length)
        return count