class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        prev = head
        left = head.next
        idx = 1

        first = -1 
        last = -1
        min_dist = float('inf')

        while left and left.next:
            if (prev.val < left.val > left.next.val or
                prev.val > left.val < left.next.val):

                if first == -1:
                    first = idx
                else:
                    min_dist = min(min_dist, idx - last)
                last = idx
            prev = left
            left = left.next
            idx += 1

        if min_dist == float('inf'):
            return [-1, -1]

        return [min_dist, last - first]
        
