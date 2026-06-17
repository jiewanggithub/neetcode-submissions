class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        

        def merge(arr, l, m, r):
            left, right = arr[l:m+1], arr[m+1:r+1]
            i, j, k = l, 0, 0

            while j < len(left) and k < len(right):
                if left[j] > right[k]:
                    arr[i] = right[k]
                    k += 1
                    i += 1
                else:
                    arr[i] = left[j]
                    j += 1
                    i += 1
            
            while j < len(left):
                arr[i] = left[j]
                j += 1
                i += 1

            while k < len(right):
                arr[i] = right[k]
                k += 1
                i += 1


        def mergeSort(arr, l, r):
            if l == r:
                return 
            
            mid = (l + r) // 2
            mergeSort(arr, l, mid)
            mergeSort(arr, mid + 1, r)
            merge(arr, l, mid, r)
            return arr
        
        if len(nums) == 1:
            return nums 
        return mergeSort(nums, 0, len(nums) - 1)
        
        