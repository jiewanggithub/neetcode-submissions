class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        res = []
        loop = 0
        for num, val in counter.most_common():
            if loop == k:
                break
            loop += 1
            res.append(num)
        return res
