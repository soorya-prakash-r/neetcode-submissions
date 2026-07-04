from collections import defaultdict
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        d = defaultdict(int)
        for i in nums:
            d[i] += 1
            if d[i] == 2:
                return True
        return False