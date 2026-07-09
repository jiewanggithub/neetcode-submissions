class Node:
    def __init__(self):
        self.children = {}
        self.end = False

class Trie:
    def __init__(self, words):
        self.root = Node()
        for word in words:
            cur = self.root
            for c in word:
                if c not in cur.children:
                    cur.children[c] = Node()
                cur = cur.children[c]
            cur.end = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = Trie(words).root    

        res = set()
        ROWS, COLS = len(board), len(board[0])
        def dfs(r, c, node, s):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS:
                return 
            
            char = board[r][c]

            if char == "#":
                return 
            if char not in node.children:
                return
            s += char
            node = node.children[char]
            if node.end:
                res.add(s)
            
            board[r][c] = "#"
            dfs(r + 1, c, node, s)
            dfs(r, c + 1, node, s )
            dfs(r - 1, c, node, s )
            dfs(r, c - 1, node, s )
            board[r][c] = char

        for i in range(ROWS):
            for j in range(COLS):
                cur = root
                dfs(i, j, cur, "")
        return list(res)     




