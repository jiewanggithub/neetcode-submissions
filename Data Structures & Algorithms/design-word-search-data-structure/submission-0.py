class Node:
    def __init__(self):
        self.children = {}
        self.end = False 
class WordDictionary:

    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = Node()
            node = node.children[char]
        node.end = True

    def search(self, word: str) -> bool:

        def dfs(i, root):
            for j in range(i, len(word)):
                c = word[j]
                if c == '.':
                    for child in root.children.values():
                        if dfs(j + 1, child):
                            return True 
                    return False 
                else:
                    if c not in root.children:
                        return False
                    root = root.children[c]
            return root.end
        return dfs(0, self.root)
                

            
