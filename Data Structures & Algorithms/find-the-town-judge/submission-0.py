class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        inDegree = [0] * (n + 1)
        outDegree = [0] * (n + 1)

        for from_, to_ in trust:
            inDegree[to_] += 1
            outDegree[from_] += 1

        for i in range(1, n + 1):
            if inDegree[i] == (n - 1) and \
            outDegree[i] == 0:
                return i
        return -1