class Solution:
    def partition(self, word: str) -> List[List[str]]:
        
        res = []
        def dfs(i,path,s):
            if i >= len(word):
                if s == "":
                    res.append(list(path))
                return
            
            s = s + word[i]
            if self.palin(s):
                path.append(s)
                dfs(i+1,path,"")
                path.pop()         

            dfs(i+1,path,s)

        dfs(0,[],"")
        return res

    def palin(self, s):
        return s == s[::-1]