class Solution:
    def jump(self, nums: List[int]) -> int:
        steps = 0
        l, r = 0, 0
        while r < len(nums) - 1:
            max_jump = 0
            for i in range(l, r + 1):
                max_jump = max(max_jump, nums[i])
            l = r + 1
            r += max_jump
            steps += 1  
        
        return steps