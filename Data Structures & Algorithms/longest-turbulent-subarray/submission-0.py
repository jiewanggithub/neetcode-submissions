class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        l, r = 0, 1
        res, pre = 1, ""

        while r < len(arr):
            if arr[r - 1] < arr[r] and pre != "<":
                res = max(res, r + 1 - l)
                pre = "<"
                r += 1
            elif arr[r - 1] > arr[r] and pre != ">":
                res = max(res, r + 1 - l)
                pre = ">"
                r += 1
            else:
                r = r + 1 if arr[r - 1] == arr[r] else r
                l = r - 1
                pre = ""
        return res

