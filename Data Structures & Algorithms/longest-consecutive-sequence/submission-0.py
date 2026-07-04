class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        def dfs(i):
            count = 1
            if i+1 in nums:
                count += dfs(i+1)
            return count

        ans = 0

        for i in nums:
            ans = max(ans, dfs(i))
            
        return ans