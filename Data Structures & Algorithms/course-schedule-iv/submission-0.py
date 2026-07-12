class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        course = {i:[] for i in range(numCourses)}
        for a, b in prerequisites:
            course[a].append(b)
        
        reachable = {i:set() for i in range(numCourses)}

        def dfs(start, cur):
            for nei in course[cur]:
                if nei not in reachable[start]:
                    reachable[start].add(nei)
                    dfs(start, nei)
        
        for start in range(numCourses):
            dfs(start, start)
        
        return [b in reachable[a] for a, b in queries] 