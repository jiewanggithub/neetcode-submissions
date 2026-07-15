class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = defaultdict(list)
        for from_i, to_i, price_i in flights:
            adj[from_i].append((price_i, to_i))
        
        min_heap = [(0, src, 0)]
        visited = {}
        max_flight = k + 1
        while min_heap:
            total_price, city, flight_used = heapq.heappop(min_heap)
            
            if city == dst:
                return total_price
            
            if flight_used == max_flight:
                continue

            for price, nei in adj[city]:
                heapq.heappush(min_heap, (total_price + price, nei, flight_used + 1))
        
        return -1