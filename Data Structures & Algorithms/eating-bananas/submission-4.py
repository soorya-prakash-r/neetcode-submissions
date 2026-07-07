class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles) - 1
        
        def is_valid(n):
            summ = 0
            summ = sum([math.ceil(x/n) for x in piles])
            if summ <= h:
                return True

        while l <= r:
            mid = math.ceil(l + (r-l)/2)
            
            if is_valid(mid):
                r = mid - 1
            else:
                l = mid + 1

        return l
