class Solution:
    def reorganizeString(self, s: str) -> str:
        counter = Counter(s)
        res = []
        n = len(s)
        maxHeap = []
        heapq.heapify(maxHeap)

    
        for char, cnt in counter.items():
            if cnt > 0:
                heapq.heappush(maxHeap, [-cnt, char])
                counter[char] -= 1
        
        prevCnt = 0
        prevChar = ""

        while maxHeap:
            cnt, char = heapq.heappop(maxHeap)
            res.append(char)
            cnt += 1

            if prevCnt < 0:
                heapq.heappush(maxHeap, [prevCnt, prevChar])
            prevCnt = cnt
            prevChar = char


        if len(res) != n:
            return ""
        return "".join(res)


                     