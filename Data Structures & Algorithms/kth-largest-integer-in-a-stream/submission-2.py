class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.arr = []
        self.temp = []
        for i in nums:
            self.arr.append(i)
            self.temp.append(i)
        self.temp.sort(reverse=True)
        self.val = k

    def add(self, val: int) -> int:
        self.arr.append(val)
        self.temp.append(val)
        self.temp.sort(reverse=True)
        print(self.temp)
        return self.temp[self.val - 1]

