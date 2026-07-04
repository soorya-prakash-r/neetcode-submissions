class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)        
        x = strs[0]

        for i in strs:
            l = []
            for x in i:
                l.append(x)
            l.sort()
            y = "".join(l)
            d[y].append(i)

        return list(d.values())
