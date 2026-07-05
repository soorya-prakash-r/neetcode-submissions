class MinStack:

    def __init__(self):
        self.arr = []
        self.sort = []
        self.mini = math.inf

    def push(self, val: int) -> None:
        self.arr.append(val)  
        self.sort.append(val)  

    def pop(self) -> None:
        x = self.arr.pop()
        self.sort.remove(x)

    def top(self) -> int:
        return self.arr[-1]

    def getMin(self) -> int:
        heapq.heapify(self.sort)
        print(self.sort)
        return self.sort[0]
        
