class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        R = deque()
        D = deque()

        for i, s in enumerate(senate):
            if s == "D":
                D.append(i)
            else:
                R.append(i)
        
        n = len(senate)
        while R and D:
            r = R.popleft()
            d = D.popleft()

            if r < d:
                R.append(r + n)
            else:
                D.append(d + n)
        
        return "Radiant" if R else "Dire"
