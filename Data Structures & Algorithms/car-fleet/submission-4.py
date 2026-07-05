class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [[p,s] for p,s in zip(position, speed)]
        res = []
        pair.sort()
        for p,s in pair[::-1]:
            res.append((target-p)/s) #time

            while len(res) >= 2 and res[-1] <= res[-2]:
                res.pop()

        return len(res)

