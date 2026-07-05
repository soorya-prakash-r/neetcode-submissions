class MinStack:

    def __init__(self):
        self.arr = []
        self.sort = []

    def push(self, val: int) -> None:
        self.arr.append(val)  
        mini = val
        if self.sort:
            mini = min(self.sort[-1], mini)
        self.sort.append(mini)

    def pop(self) -> None:
        x = self.arr.pop()
        self.sort.pop()

    def top(self) -> int:
        return self.arr[-1]

    def getMin(self) -> int:
        return self.sort[-1]
        
