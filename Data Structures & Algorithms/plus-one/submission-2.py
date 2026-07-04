class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        l = []
        temp = 0
        end = 1
        for i in range(len(digits)-1, -1, -1):
            t = digits[i]+end
            l.append(t%10)
            end = t//10
            
        if end != 0:
            l.append(end)
        
        return l[::-1]