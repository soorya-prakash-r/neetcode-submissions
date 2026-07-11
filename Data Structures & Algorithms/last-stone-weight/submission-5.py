class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        new_stones = [-s for s in stones]
        heapq.heapify(new_stones)
        while len(new_stones) > 1:
            x = -heapq.heappop(new_stones)
            y = -heapq.heappop(new_stones)
            heapq.heappush(new_stones, -(abs(x-y)))

        return abs(new_stones[0])
        