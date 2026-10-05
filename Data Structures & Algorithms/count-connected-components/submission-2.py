class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)

        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        visited = set()
        count = 0

        for i in range(n):
            if i not in visited:
                count += 1

                queue = deque([i])
                visited.add(i)
                
                while queue:
                    node = queue.popleft()
                    for nei in adj[node]:
                        if nei not in visited:
                            queue.append(nei)
                            visited.add(nei)
        return count
        """
        def dfs(node):
            if node in visited:
                return 

            visited.add(node)

            for nei in adj[node]:
                dfs(nei)
        """