class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []
        temp = 0
        l, r = 0, 1
        for x,y in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < y:
                t = stack.pop()
                result[t] = x - t
            stack.append(x)
        return result
                
            