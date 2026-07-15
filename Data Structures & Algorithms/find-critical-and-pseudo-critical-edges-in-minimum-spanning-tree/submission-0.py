class UnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n)]
        self.rank = [1] * n

    def find(self,n):
        while n != self.par[n]:
            self.par[n] = self.par[self.par[n]]
            n = self.par[n]
        return n
    
    def union(self, n1, n2):
        p1, p2 = self.find(n1), self.find(n2)
        if p1 == p2:
            return False
        
        if self.rank[p1] > self.rank[p2]:
            self.rank[p1] += self.rank[p2]
            self.par[p2] = p1
        else:
            self.rank[p2] += self.rank[p1]
            self.par[p1] = p2 
        return True 

class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        for i, edge in enumerate(edges):
            edge.append(i)
        
        edges.sort(key=lambda x: x[2])

        mst_weights = 0
        uf = UnionFind(n)

        for v1, v2, weight, i in edges:
            if uf.union(v1, v2):
                mst_weights += weight 
        
        critical, pseudo_critical = [], []

       
        for n1, n2, weight, i in edges:
            weights = 0
            uf = UnionFind(n)
            # try without the edge 
            for v1, v2, w, j in edges:
                if i != j and uf.union(v1, v2): 
                    weights += w
            if max(uf.rank) < n or weights > mst_weights:
                critical.append(i)
                continue

            # try with the edge
            weights = weight 
            uf = UnionFind(n)
            uf.union(n1, n2)
            for v1, v2, w, j in edges:
                if uf.union(v1, v2):
                    weights += w
            if weights == mst_weights:
                pseudo_critical.append(i)

        return [critical, pseudo_critical]









