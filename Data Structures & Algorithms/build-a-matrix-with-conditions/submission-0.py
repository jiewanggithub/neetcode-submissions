class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        
        def dfs(src, adj, visited, visiting, order):
            if src in visiting:
                return False 

            if src in visited:
                return True
            visited.add(src)
            visiting.add(src)

            for nei in adj[src]:
                if not dfs(nei, adj, visited, visiting, order):
                    return False 
            
            visiting.remove(src)
            order.append(src)
            return True 


        def top_sort(edges):
            adj = defaultdict(list)
            for src, dest in edges:
                adj[src].append(dest)

            visited, visiting = set(), set()
            order = []

            for src in range(1, k + 1):
                if not dfs(src, adj, visited, visiting, order):
                    return []
            return order[::-1]

        row_order = top_sort(rowConditions)
        col_order = top_sort(colConditions)

        if not row_order or not col_order:
            return []

        rowMap = {edge: i for i, edge in enumerate(row_order)}
        colMap = {edge: i for i, edge in enumerate(col_order)}

        res = [[0] * k for i in range(k)]
        for i in range(1, k + 1):
            r, c = rowMap[i], colMap[i]
            res[r][c] = i
        return res

