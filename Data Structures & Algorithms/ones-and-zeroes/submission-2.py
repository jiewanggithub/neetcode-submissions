from functools import cache 
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        cnts = [Counter(s) for s in strs]
        @cache 
        def dfs(i, ones, zeros):
            if i >= len(strs):
                return 0
            
            if ones + cnts[i]["1"] > n or zeros + cnts[i]["0"] > m:
                return dfs(i + 1, ones, zeros)

            return max(1 + dfs(i + 1, ones + cnts[i]["1"], zeros + cnts[i]["0"]),
            dfs(i + 1, ones, zeros))

        return dfs(0, 0, 0)

