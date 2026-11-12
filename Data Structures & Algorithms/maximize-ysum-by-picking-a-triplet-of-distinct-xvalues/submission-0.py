class Solution:
    def maxSumDistinctTriplet(self, x: List[int], y: List[int]) -> int:
        hashmap = {}
        for i, val in enumerate(x):
            if val in hashmap:
                if hashmap[val] < y[i]:
                    hashmap[val] = y[i]
            else:
                hashmap[val] = y[i]

        if len(hashmap) < 3:
            return -1
        
        return sum(sorted(hashmap.values(), reverse=True)[:3])
        
        
