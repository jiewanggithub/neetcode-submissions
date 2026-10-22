class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        Dir = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def dfs(i, j, l, s):
            if l == len(word):
                return True
            if (i, j) in s:
                return 
            if i < 0 or j >= COLS:
                return 
            if i < 0 or i >= ROWS or j < 0 or j >= COLS:
                return False 
            if board[i][j] != word[l]:
                return False
            s.add((i, j))
            
            res = False
            for dx, dy in Dir:
                nx, ny = dx + i, dy + j
                res = res or dfs(nx, ny, l + 1, s)
            s.remove((i, j))
            return res

        for i in range(ROWS):
            for j in range(COLS):
                if dfs(i, j, 0, set()):
                    return True
        return False         
                