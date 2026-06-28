class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        n = mountainArr.length()
        l, r = 0, n - 1

        while l <= r:
            m = (l + r) // 2
            if mountainArr.get(m - 1) < mountainArr.get(m) < mountainArr.get(m + 1):
                l = m + 1
            elif mountainArr.get(m - 1) > mountainArr.get(m) > mountainArr.get(m + 1):
                r = m - 1
            else:
                break
            
        peak = m 
        
        l, r = 0, peak
        while l <= r:
            m = (l + r) // 2
            if mountainArr.get(m) == target:
                return m
            elif mountainArr.get(m) > target:
                r = m - 1
            else:
                l = m + 1
        
        l, r = peak + 1, n - 1
        while l <= r:
            m = (l + r) // 2
            if mountainArr.get(m) == target:
                return m
            elif mountainArr.get(m) > target:
                l = m + 1
            else:
                r = m - 1
        return -1 