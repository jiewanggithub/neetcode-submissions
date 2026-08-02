class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False 
        
        count = defaultdict(int)
        for h in hand:
            count[h] += 1

        for start in sorted(count):
            if count[start] == 0:
                continue 
            
            frequency = count[start]
            for i in range(start, start + groupSize):
                if count[i] < frequency:
                    return False 
                count[i] -= frequency

        return True 
