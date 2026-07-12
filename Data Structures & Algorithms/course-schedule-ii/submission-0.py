class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        course = {i:[] for i in range(numCourses)}
        for c, pre in prerequisites:
            course[c].append(pre)
        
        visiting = set()
        finished = set()
        res = []
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

            res.append(cur)
            return True
        for cur in range(numCourses):
            if not dfs(cur):
                return []
        return res