class Solution:
    def bestClosingTime(self, customers: str) -> int:
        penalty = customers.count("Y")
        best = 0
        min_penalty = penalty

        for i, c in enumerate(customers):
            if c == "Y":
                penalty -= 1
            else:
                penalty += 1
            
            if penalty < min_penalty:
                min_penalty = penalty
                best = i + 1
            
        return best