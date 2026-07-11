class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            heapq.heapify_max(stones)
            x = stones.pop(0)
            heapq.heapify_max(stones)
            y = stones.pop(0)
            stones.append(abs(x-y))
            heapq.heapify_max(stones) 

        return stones[0]
        