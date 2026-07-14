class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(i, curr):
            if curr not in res:
                res.append(list(curr))            
            if i >= len(nums):
                return
            
            curr.append(nums[i])
            dfs(i+1, curr)

            curr.pop()
            dfs(i+1, curr)

        dfs(0, [])
        return res

        