class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def canSplit(largest):
            curSum = 0
            subarr = 0

            for n in nums:
                curSum += n
                if curSum > largest:
                    subarr += 1
                    curSum = n
            return subarr + 1 <= k

        l, r = max(nums), sum(nums)
        res = r

        while l <= r:
            mid = (r + l) // 2
            if canSplit(mid):
                res = mid
                r = mid - 1
            else:
                l = mid + 1

        return res 

