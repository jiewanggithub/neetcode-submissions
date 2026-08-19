class CountSquares:

    def __init__(self):
        self.points = []
        self.counter = Counter()

    def add(self, point: List[int]) -> None:
        if point[0] >= 0 and point[1] >= 0 and point[0] <= 1000 and point[1] <= 1000:
            self.points.append(point)
            self.counter[(point[0], point[1])] += 1

    def count(self, point: List[int]) -> int:
        x, y = point[0], point[1]
        cnt = 0
        
        for (px, py), freq in self.counter.items():
            # if p is a digonal point 
            if abs(x - px) == abs(y - py) and x != px:    
                cnt += self.counter[(px, py)] * self.counter[(x, py)] * self.counter[(px, y)] 
        return cnt 