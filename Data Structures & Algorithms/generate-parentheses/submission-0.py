class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        res = []
        
        def dfs(openc, closec, path):
            if openc == closec == n:
                res.append("".join(list(path)))
                return
            
            if openc < n:
                path.append("(")
                dfs(openc+1, closec, path)
                path.pop()
            if closec < openc:
                path.append(")")
                dfs(openc, closec+1, path)
                path.pop()

        dfs(0, 0, [])
        return res