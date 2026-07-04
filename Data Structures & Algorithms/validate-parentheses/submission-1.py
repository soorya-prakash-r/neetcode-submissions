class Solution:
    def isValid(self, s: str) -> bool:
        l = []
        for i in range(0, len(s)): 
            if len(l) == 0:
                l.append(s[i])
            elif l[-1] == '{' and s[i] == '}':
                l.pop()                
            elif l[-1] == '[' and s[i] == ']':
                l.pop()
            elif l[-1] == '(' and s[i] == ')':
                l.pop()
            else:
                l.append(s[i])
            print(l)

        return len(l) == 0