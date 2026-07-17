class UnionFind:
    def __init__(self, n):
        self.count = n
        self.size = [1] * n
        self.par = {i: i for i in range(n)}

    def find(self, src):
        while src != self.par[src]:
            self.par[src] = self.par[self.par[src]]
            src = self.par[src]  
        return src
    
    def union(self, n1, n2):
        p1, p2 = self.find(n1), self.find(n2)
        if p1 == p2:
            return   
        
        if self.size[p1] > self.size[p2]:
            self.size[p1] += self.size[p2]
            self.par[p2] = p1
        else:
            self.size[p2] += self.size[p1]
            self.par[p1] = p2
        self.count -= 1

class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        uf = UnionFind(len(nums))
        factor = {}
        if len(nums) == 1:
            return True

        if 1 in nums:
            return False

        for i, num in enumerate(nums):
            f = 2
            while f * f <= num:
                if num % f == 0:
                    if f in factor:
                        uf.union(i, factor[f])
                    else:
                        factor[f] = i
                while num % f == 0:
                    num //= f 
                f += 1
        
            if num > 1:
                if num in factor:
                    uf.union(i, factor[num])
                else:
                    factor[num] = i
        return uf.count == 1 













