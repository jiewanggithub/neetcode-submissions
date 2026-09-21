class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        freq = [[] for _ in range(len(nums) + 1)]

        res = []
        for num in nums:
            counter[num] = counter.get(num, 0) + 1

        for num, c in counter.items():
            freq[c].append(num) 

        res = []

        for i in range(len(freq) - 1, -1, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res 

