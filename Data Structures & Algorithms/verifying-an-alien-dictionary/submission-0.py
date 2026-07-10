class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        mapping = {c:i for i, c in enumerate(order)}

        for i in range(len(words) - 1):
            word1 = words[i]
            word2 = words[i + 1]

            
            shorter = min(len(word1), len(word2))
            for j in range(shorter):
                if word1[j] != word2[j]:
                    if mapping[word1[j]] > mapping[word2[j]]:
                        return False
                    break
            else:
                if len(word1) > len(word2):
                    return False
        return True

            