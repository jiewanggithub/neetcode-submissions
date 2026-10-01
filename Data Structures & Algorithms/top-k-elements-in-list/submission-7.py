class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        for n in nums:
            freq[n] += 1
        
        sorted_num = sorted(freq.keys(), key=lambda x: freq[x], reverse=True)

        return list(sorted_num[:k])
    