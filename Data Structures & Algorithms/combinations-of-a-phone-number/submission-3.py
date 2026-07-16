class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        letterMap = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        res = []
        if len(digits) == 0:
            return res
        def dfs(s,digit):
            if len(s) == len(digits):
                res.append(s[::1])
                return
            if digit >= len(digits):
                return
            for x in letterMap[digits[digit]]:
                dfs(s+x, digit+1)

        dfs("", 0) 
        return res