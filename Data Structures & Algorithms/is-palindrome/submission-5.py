class Solution:
    def isPalindrome(self, s: str) -> bool:
        x = 0
        print([z for z in "".join(s.split())])
        s = "".join([z for z in "".join(s.split(" ")) if z.isalnum()])
        y = len(s) - 1
        print(s)
        flag = False
        if len(s) == 0 or len(s) == 1:
            return True 
        while x <= y:
            if not s[x].isalnum():
                x += 1
                continue
            if not s[y].isalnum():
                y -= 1
                continue
            if s[x].lower() != s[y].lower():
                return False

            x += 1
            y -= 1
    
            flag = True

        return flag
   