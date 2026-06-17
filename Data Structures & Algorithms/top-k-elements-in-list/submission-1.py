class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        freq = [[] for _ in range(len(nums) + 1)]
        
        for n in nums:
                count[n] += 1
        for n, c in count.items():
            freq[c].append(n)
        
        last = len(freq) - 1
        res = []
        for i in range(last, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
                
                
        