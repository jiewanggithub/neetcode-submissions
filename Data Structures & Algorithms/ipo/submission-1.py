class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        capHeap, proHeap = [], []
        cnt = 0
        for cap, profit in zip(capital, profits):    
            heapq.heappush(capHeap, [cap, profit])
        
        while cnt < k:
            while capHeap and capHeap[0][0] <= w:
                cap, pro = heapq.heappop(capHeap)
                heapq.heappush(proHeap, -pro)
            
            if not proHeap:
                break
                
            profit = heapq.heappop(proHeap)
            cnt += 1
            w += (-profit)
        return w
