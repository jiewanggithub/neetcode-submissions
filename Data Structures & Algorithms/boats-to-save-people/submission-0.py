class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        l, r = 0, len(people) - 1
        res = 0

        while l < r:
            sumWeight = people[l] + people[r]
            if sumWeight <= limit:
                res += 1
                l += 1
                r -= 1
            elif sumWeight > limit:
                res += 1 
                r -= 1
        if l == r:
            res += 1
        return res 
                