class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        if len(A) > len(B):
            A ,B = B, A
        
        total = len(A) + len(B)
        half = total // 2
        l, r = 0 , len(A) - 1
        while True:
            m = (l + r) // 2
            j = half - m - 2 # m 是长度不是0based，j本身就得-1 所以-2
            
            leftEndA = A[m] if m >= 0 else float('-inf')
            rightStartA = A[m+1] if m + 1 < len(A) else float('inf')
            leftEndB = B[j] if j >= 0 else float('-inf')
            rightStartB = B[j+1] if j + 1 < len(B) else float('inf')

            if leftEndA <= rightStartB and leftEndB <= rightStartA:
                # odd
                if total % 2:
                    return min(rightStartA, rightStartB)
                else:
                    return (max(leftEndA, leftEndB) + min(rightStartA,rightStartB)) / 2
            else:
                if leftEndA > rightStartB:
                    r = m - 1
                else:
                    l = m + 1