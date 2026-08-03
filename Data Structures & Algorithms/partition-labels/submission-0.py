class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        cnt = defaultdict(int)
        for char in s:
            cnt[char] += 1

        res = []
        visited = set()
        l, r = 0, 0
        for char in s:
            visited.add(char)
            cnt[char] -= 1
            flag = 0
            for v in visited:
                if cnt[v] != 0:
                    flag = 1
            for char in s:
                if cnt[char] == 0 and char in visited:
                    visited.remove(char)
    
            if flag:
                r += 1
            else:
                res.append(r - l + 1)
                r += 1
                l = r
        return res 
