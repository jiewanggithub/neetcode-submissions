class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        countArr = [[] for _ in range(len(nums) + 1)]
        
        for n in nums:
                count[n] += 1
                countArr[count[n]].append(n)

        last = len(countArr) - 1
        for i in range(last, -1, -1):
            if len(countArr[i]) == k:
                return countArr[i]
        