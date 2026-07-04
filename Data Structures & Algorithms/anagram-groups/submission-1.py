class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)        
        x = strs[0]

        for i in strs:
            l = [0] * 26
            for x in i:
                l[ord(x) - ord("a")] += 1
            
            d[tuple(l)].append(i)

        return list(d.values())
