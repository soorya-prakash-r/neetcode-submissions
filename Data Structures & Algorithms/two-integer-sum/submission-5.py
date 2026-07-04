from collections import defaultdict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = defaultdict(int)

        for i in range(0, len(nums)):
            x = d.get(target - nums[i], -1)
            if i != x and x != -1:
                return [x, i]
            d[nums[i]] = i

        