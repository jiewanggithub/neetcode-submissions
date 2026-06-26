class FreqStack:

    def __init__(self):
        self.stacks = {}
        self.maxCnt = 0
        self.cnt = defaultdict(int)

    def push(self, val: int) -> None:
        self.cnt[val] += 1
        if self.cnt[val] > self.maxCnt:
            self.maxCnt += 1
            self.stacks[self.maxCnt] = []
        self.stacks[self.cnt[val]].append(val)

    def pop(self) -> int:
        res = self.stacks[self.maxCnt].pop()
        self.cnt[res] -= 1
        if not self.stacks[self.maxCnt]:
            self.maxCnt -= 1
        return res


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()