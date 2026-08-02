class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False 
        
        count = defaultdict(int)
        for h in hand:
            count[h] += 1
        hand.sort()

        for h in hand:
            if count[h] == 0:
                continue 
            start = h
            for i in range(start, start + groupSize):
                if count[i] == 0:
                    return False 
                count[i] -= 1

        return True 
