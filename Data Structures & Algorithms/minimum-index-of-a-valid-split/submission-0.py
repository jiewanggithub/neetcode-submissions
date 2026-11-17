class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        counter = Counter(nums)
        dominant, d_cnt = max(counter.items(), key=lambda x: x[1])
        
        n = len(nums)
        left_cnt = 0

        for i in range(n):
            if nums[i] == dominant:
                left_cnt += 1
            
            left_len = i + 1
            right_len = n - i - 1
            right_cnt = counter[dominant] - left_cnt

            if left_cnt * 2 > left_len and right_cnt * 2 > right_len:
                return i
        return -1

        

