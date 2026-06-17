class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) == 1:
            return nums

        def mergeSort(arr, l, r):
            if l == r:
                return 
            
            m = (l + r) // 2
            mergeSort(arr, l, m)
            mergeSort(arr, m+1, r)
            merge(arr, l, m, r)
            return arr
        
        def merge(arr, l , m, r):
            firstArr, secondArr = arr[l:m+1], arr[m+1:r+1]
            i, j, k = l, 0, 0
            
            while j < len(firstArr) and k < len(secondArr):
                if firstArr[j] < secondArr[k]:
                    arr[i] = firstArr[j]
                    i += 1
                    j += 1
                else:
                    arr[i] = secondArr[k]
                    i += 1
                    k += 1
                
            while j < len(firstArr):
                arr[i] = firstArr[j]
                i += 1
                j += 1
            
            while k < len(secondArr):
                arr[i] = secondArr[k]
                i += 1
                k += 1
        return mergeSort(nums, 0, len(nums) - 1)
        
        