class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        d1 = {}
        d2 = {}
        l = 0
        r = 0
        for i in s1:
            d1[i] = d1.get(i,0) + 1
        
        t = 0      
        flag = False
        length = len(s1)  
        while r < len(s2):
            d2[s2[r]] = d2.get(s2[r],0) + 1
            t += 1

            if t == length:
                for i in s1:
                    print(i)
                    if d1.get(i) != d2.get(i,0):
                        flag = False
                        break
                    flag = True
                if flag: return flag
                
                d2[s2[l]] = d2.get(s2[l],0) - 1
                if d2[s2[l]] == 0:
                    del d2[s2[l]]
                l += 1
                t -= 1
            r += 1
        return False