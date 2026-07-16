class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        if not len(nums):
            return [[]]
        self.permu = self.permute(nums[1:])
        for x in self.permu:
            for i in range(0,len(x)+1):
                permu_copy = list(x)
                permu_copy.insert(i, nums[0])
                res.append(permu_copy)

        return res