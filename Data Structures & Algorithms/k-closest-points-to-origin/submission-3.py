class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        d = {0.0: []}
        heap = []
        for x in points:
            dis = math.sqrt(x[0]*x[0] + x[1]*x[1])
            heapq.heappush(heap, [-dis, x])
            if len(heap) > k:
                heapq.heappop(heap)
            
        res = []
        while len(res) < k:
            x = heapq.heappop(heap)
            res.append(x[1])
        return res