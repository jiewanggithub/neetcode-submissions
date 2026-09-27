class Node():
    def __init__(self):
        self.end = False
        self.children = {}

class Trie():
    def __init__(self):
        self.root = Node()

    def addWord(self, word):
        cur = self.root 
        for char in word:
            if char not in cur.children:
                cur.children[char] = Node()
            cur = cur.children[char]
        cur.end = True

class WordDictionary:

    def __init__(self):
        self.trie = Trie()

    def addWord(self, word: str) -> None:
        self.trie.addWord(word)
        
    def search(self, word: str) -> bool:
        cur = self.trie.root

        def dfs(i, cur):
            if i == len(word):
                return cur.end
            
            char = word[i]
            if char == '.':
                for child in cur.children.values():
                    if dfs(i + 1, child):
                        return True
                return False
            
            if char not in cur.children:
                return False
            
            return dfs(i + 1, cur.children[char])
        return dfs(0, cur)

