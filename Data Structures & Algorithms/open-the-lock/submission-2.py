class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        visited = set(deadends)
        q = deque([("0000", 0)])

        if "0000" in visited:
            return -1
            
        def children(lock):
            res = []
            for i in range(4):
                digit = str((int(lock[i]) + 1) % 10)
                res.append(lock[:i] + digit + lock[i+1:])
                digit = str((int(lock[i]) + 9) % 10)
                res.append(lock[:i] + digit + lock[i+1:])
            return res 

        while q:
            lock, turns = q.popleft()

            if lock == target:
                return turns
            
            for child in children(lock):
                if child not in visited:
                    visited.add(child)
                    q.append((child, turns + 1))
        
        return -1
