class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        maxHeap = []
        for count, char in [(a, 'a'), (b,'b'), (c, 'c')]:
            if count > 0:
                heapq.heappush(maxHeap, [-count, char])
        
        res = []

        while maxHeap:
            count1, char1 = heapq.heappop(maxHeap)
            
            if len(res) >= 2 and char1 == res[-1] and char1 == res[-2]:
                if not maxHeap:
                    break
                
                count2, char2 = heapq.heappop(maxHeap)
                res.append(char2)

                if count2 + 1 < 0:
                    heapq.heappush(maxHeap, [count2 + 1, char2])

                heapq.heappush(maxHeap, [count1, char1])
            else:
                res.append(char1)
                count1 += 1

                if count1 < 0:
                    heapq.heappush(maxHeap, [count1, char1]) 
        return "".join(res)   

        

        
