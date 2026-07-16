class MedianFinder:

    def __init__(self):
        self.small = []
        self.large = []        

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, -num)
        while len(self.small) - len(self.large) > 1 or self.large and -self.small[0] > self.large[0]:
            x = heapq.heappop(self.small)
            heapq.heappush(self.large, -x)
        while len(self.large) - len(self.small) > 1:
            x = heapq.heappop(self.large)
            heapq.heappush(self.small, -x)

    def findMedian(self) -> float:
        print(self.small, self.large)
        if len(self.small) > len(self.large):
            return -self.small[0]
        elif len(self.large) > len(self.small):
            return self.large[0]
        else:
            print(-self.small[0], self.large[0])
            return (-self.small[0] + self.large[0]) / 2
        
        