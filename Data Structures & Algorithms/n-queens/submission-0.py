class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols = set()
        pdiag = set()
        ndiag = set()
        res = []
        path = [["."] * n for i in range(0,n)]

        def dfs(r):
            if r >= n:
                print(path)
                res.append(["".join(i) for i in path])
                return
            
            for c in range(0,n):

                if c in cols or (r+c) in pdiag or (r-c) in ndiag:
                    continue

                cols.add(c)
                pdiag.add(r+c)
                ndiag.add(r-c)
                path[r][c] = "Q"

                dfs(r+1)

                cols.remove(c)
                pdiag.remove(r+c)
                ndiag.remove(r-c)
                path[r][c] = "."
        dfs(0)
        return res