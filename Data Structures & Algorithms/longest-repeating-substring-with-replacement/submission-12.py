class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        d = {}
        l = 0
        maxi = 0
        res = 0
        for r in range(0, len(s)):
            d[s[r]] = d.get(s[r],0) + 1
            size = r - l + 1
            maxi = max(maxi, d.get(s[r],0))
            
            while size - maxi > k:
                d[s[l]] = d.get(s[l],0) - 1
                if d.get(s[l],0) == 0:
                    del d[s[l]] 
                l += 1
                size = r - l + 1
            res = max(res, r-l+1)
        return res