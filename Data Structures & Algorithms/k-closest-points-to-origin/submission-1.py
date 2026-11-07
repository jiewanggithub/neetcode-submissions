class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        if k >= len(points):
            return points

        heap = []
        def distanceCalc(a, b):
            return math.sqrt((a[0] - b[0]) ** 2 + ((a[1] - b[1]) ** 2))
        
        for point in points:
            heapq.heappush(heap, (-distanceCalc([0, 0], point), point[0], point[1]))
        
        while len(heap) > k:
            heapq.heappop(heap)
        
        res = []
        for dis, a, b in heap:
            res.append([a, b])     
        return res 
        
