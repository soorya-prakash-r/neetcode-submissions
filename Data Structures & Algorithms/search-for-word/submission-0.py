class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        def dfs(r, c, i, path):
            if len(path) == len(word):
                return True
                
            if i < 0 or i >= len(word) or r < 0 or c < 0 or r >= len(board) or c >= len(board[0]) or word[i] != board[r][c] or (r,c) in path:
                return False
            
            path.append((r,c))
            res = dfs(r+1,c,i+1,path) or dfs(r-1,c,i+1,path) or dfs(r,c+1,i+1,path) or dfs(r,c-1,i+1,path)
            path.pop()

            return res

        for r in range(0, len(board)):
            for c in range(0, len(board[0])):
                if dfs(r,c, 0, []):
                    return True

        return False