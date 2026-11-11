from functools import cache 
class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj = defaultdict(list)
        for pre, take in prerequisites:
            adj[take].append(pre)

        @cache
        def dfs(course):
            res = set()

            for pre in adj[course]:
                res.add(pre)
                res.update(dfs(pre))
            return frozenset(res)
        ans = []

        for pre, take in queries:
            ans.append(pre in dfs(take))
        return ans