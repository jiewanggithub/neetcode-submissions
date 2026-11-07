class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        n = len(senate)
        R = deque()
        D = deque()

        for i, s in enumerate(senate):
            if s == "D":
                D.append(i)
            else:
                R.append(i)
        
        while D and R:
            d = D.popleft()
            r = R.popleft()

            if d < r:
                D.append(d + n)
            else:
                R.append(r + n)
        return "Radiant" if R else "Dire"
