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

        def dfs(i, node):
            if i == len(word):
                return node.end
            
            if word[i] == '.':
                for n in node.children.values():
                    if dfs(i + 1, n):
                        return True 
                return False 
            if word[i] not in node.children:
                return False
            
            return dfs(i + 1, node.children[word[i]])
        return dfs(0, cur)











