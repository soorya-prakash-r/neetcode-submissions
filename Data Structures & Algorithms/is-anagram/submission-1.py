from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        x = s + t
        d1 = defaultdict(int)
        d2 = defaultdict(int)
        flag = False
        for i in s:
            d1[i] += 1 
        for j in t:
            d2[j] += 1

        return d1 == d2
