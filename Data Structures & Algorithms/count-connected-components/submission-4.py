class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = [i for i in range(n)]
        rank = [1] * n

        def find(x):
            while x != parent[x]:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(x, y):
            parentA = find(x)
            parentB = find(y)

            if parentA == parentB:
                return 0
            if rank[parentA] > rank[parentB]:
                parentA, parentB = parentB, parentA
            
            rank[parentB] += rank[parentA]
            parent[parentA] = parentB
            return 1
        
        components = n
        for u, v in edges:
            components -= union(u, v)
        return components 
            

        
