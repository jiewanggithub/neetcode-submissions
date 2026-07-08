class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        path = []
        counter = Counter(nums)

        def dfs():
            if len(path) == n:
                res.append(path.copy())
                return
            
            for x in counter:
                if counter[x] > 0:
                    path.append(x)
                    counter[x] -= 1
                    dfs()

                    counter[x] += 1
                    path.pop()
        dfs()
        return res