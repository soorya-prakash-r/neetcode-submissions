class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        d = {}
        heap = []
        for i in tasks:
            d[i] = d.get(i,0) + 1
        for i in d:
            heapq.heappush(heap, -d[i])
        
        t = 0
        temp = deque()
        while heap or temp:
            
            if heap:
                x = heapq.heappop(heap)
                x += 1
                if x:
                    temp.append([x, t+n])
            if temp:
                if temp[0][1] == t:
                    heapq.heappush(heap, temp.popleft()[0])
            t += 1
        return t