class Solution:
    def countBits(self, n: int) -> List[int]:
        l = []
        def binary(x):
            count = 0
            while x > 0:
                t = x%2
                x = x//2

                if t == 1:
                    count += 1
            return count

        for i in range(0, n+1):
            l.append(binary(i))
        return l
        