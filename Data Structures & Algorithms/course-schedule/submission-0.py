class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        course = {i:[] for i in range(numCourses)}

        for a, b in prerequisites:
            course[a].append(b)

        visiting = set()
        finished = set()

        def dfs(cur):
            if cur in visiting:
                return False
            
            if cur in finished:
                return True 
            
            visiting.add(cur)

            for pre in course[cur]:
                if not dfs(pre):
                    return False
            
            visiting.remove(cur)
            finished.add(cur)
            return True 
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True 
