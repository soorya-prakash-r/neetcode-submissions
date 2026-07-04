from collections import Counter
import heapq


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = list(Counter(nums).items())
        c.sort(key = lambda x: x[1], reverse = False)
        l = []
        for i in range(0,k):
            l.append(c[-1-i][0])
        return l