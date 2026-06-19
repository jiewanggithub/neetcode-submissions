class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        prefixSum = {0 : 1}
        curSum = 0

        for n in nums:
            curSum += n
            diff = curSum - k
            res += prefixSum.get(diff, 0)
            prefixSum[curSum] = prefixSum.get(curSum, 0) + 1
        return res 

        