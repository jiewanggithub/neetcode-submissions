class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
    
        def merge(list1, list2):
            res = []
            i = j = 0

            while i < len(list1) and j < len(list2):
                if list1[i] < list2[j]:
                    res.append(list1[i])
                    i += 1
                else:
                    res.append(list2[j])
                    j += 1
            
            res.extend(list1[i:])
            res.extend(list2[j:])
            return res
        
        if len(nums) <= 1:
            return nums
        
        mid = len(nums) // 2
        list1 = self.sortArray(nums[:mid])
        list2 = self.sortArray(nums[mid:])
        return merge(list1, list2)