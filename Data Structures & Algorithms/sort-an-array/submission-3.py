class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) == 1:
            return nums

        def mergeSort(arr, l, r):
            if l == r:
                return 
            
            m = (l + r) // 2
            mergeSort(arr, l, m)
            mergeSort(arr, m + 1, r)
            merge(arr, l, m, r)
            return arr

        def merge(arr, l, m, r):
            arr1, arr2 = arr[l:m+1], arr[m+1:r+1]
            i, j, k = l, 0, 0

            while j < len(arr1) and k < len(arr2):
                if arr1[j] < arr2[k]:
                    arr[i] = arr1[j]
                    i += 1
                    j += 1
                else:
                    arr[i] = arr2[k]
                    i += 1
                    k += 1
            while j < len(arr1):
                arr[i] = arr1[j]
                i += 1
                j += 1
            
            while k < len(arr2):
                arr[i] = arr2[k]
                i += 1
                k += 1
        return mergeSort(nums, 0, len(nums) - 1)
        

        
            
        
        