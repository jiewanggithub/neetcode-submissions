class MedianFinder:

    def __init__(self):
        self.smallHeap = []
        self.largeHeap = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.smallHeap, -num)
        if self.largeHeap and -self.smallHeap[0] > self.largeHeap[0]:
            number = heapq.heappop(self.smallHeap)
            heapq.heappush(self.largeHeap, -number)

        if len(self.smallHeap) > len(self.largeHeap) + 1:
            val = -heapq.heappop(self.smallHeap)
            heapq.heappush(self.largeHeap, val)

        if len(self.largeHeap) > len(self.smallHeap):
            val = heapq.heappop(self.largeHeap)
            heapq.heappush(self.smallHeap, -val)
    def findMedian(self) -> float:
        n = len(self.smallHeap) + len(self.largeHeap)
        if n % 2:
            # odd 
            return -self.smallHeap[0]
        else:
            sum_ = self.largeHeap[0] + (-self.smallHeap[0])
            return float(sum_ / 2)
        