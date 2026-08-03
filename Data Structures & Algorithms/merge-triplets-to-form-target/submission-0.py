class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        arr = []
        for a, b, c in triplets:
            if not (a > target[0] or b > target[1] or c > target[2]):
                arr.append([a, b, c])
        triplet = [-1, -1, -1]
        for a, b, c in arr:
            triplet = [max(a, triplet[0]), max(b, triplet[1]), max(c, triplet[2])]
        if triplet == target:
            return True

        return False
