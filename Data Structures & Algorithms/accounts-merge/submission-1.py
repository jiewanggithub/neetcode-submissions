class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [1] * n   # size heuristic
    
    def find(self, x):
        while x != self.parent[x]:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, n1, n2):
        p1, p2 = self.find(n1), self.find(n2)
        if p1 == p2:
            return False
        
        if self.rank[p1] > self.rank[p2]:
            self.parent[p2] = p1
            self.rank[p1] += self.rank[p2]
        else:
            self.parent[p1] = p2
            self.rank[p2] += self.rank[p1]
    
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = UnionFind(len(accounts))
        emailToAcc = {}

        for i, info in enumerate(accounts):
            for e in info[1:]:
                if e in emailToAcc:
                    uf.union(i, emailToAcc[e]) 
                else:
                    emailToAcc[e] = i
        
        emailGroup = defaultdict(list)
        for e, i in emailToAcc.items():
            root = uf.find(i)
            emailGroup[root].append(e)

        res = []
        for i, emails in emailGroup.items():
            res.append([accounts[i][0]] + sorted(emails))
        return res

        