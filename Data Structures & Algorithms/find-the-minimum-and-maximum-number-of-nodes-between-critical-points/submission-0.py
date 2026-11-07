class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        c_points = []

        prev = head
        left = head.next
        cnt = 1

        while left and left.next:
            if (prev.val < left.val > left.next.val or
                prev.val > left.val < left.next.val):
                c_points.append(cnt)

            prev = left
            left = left.next
            cnt += 1

        if len(c_points) < 2:
            return [-1, -1]

        min_dist = float('inf')

        for i in range(1, len(c_points)):
            min_dist = min(
                min_dist,
                c_points[i] - c_points[i - 1]
            )

        max_dist = c_points[-1] - c_points[0]

        return [min_dist, max_dist]
        
