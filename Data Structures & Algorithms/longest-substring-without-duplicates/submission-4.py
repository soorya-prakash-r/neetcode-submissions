class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        temp = []
        l = 0
        y = 0 
        count = 0
        for i in s:
            if i not in temp:
                temp.append(i)
            else:
                if temp[0] == i:
                    temp.pop(0)
                    temp.append(i)
                else:
                    temp = []
                    temp.append(i)
            count = max(count, len(temp))
        
        return count