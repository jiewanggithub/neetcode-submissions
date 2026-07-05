class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # maxHeap
        for i in range(len(nums)):
            nums[i] *= -1
        heapq.heapify(nums)
        
        for _ in range(k):
            ans = heapq.heappop(nums)
        return -ans