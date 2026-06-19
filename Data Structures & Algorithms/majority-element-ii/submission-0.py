class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        candidates = collections.defaultdict(int)
        res = []

        for n in nums:
            candidates[n] += 1
            if len(candidates) <= 2:
                continue 
            
            new_ = collections.defaultdict(int) 
            for n, c in candidates.items():
                if c > 1:
                    new_[n] = c - 1
            candidates = new_

        for n in candidates:
            if nums.count(n) > (len(nums) // 3):
                res.append(n)
        return res
