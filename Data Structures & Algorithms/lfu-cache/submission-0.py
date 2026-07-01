class ListNode:

    def __init__(self, key=0, prev=None, next=None):
        self.key = key
        self.prev = prev
        self.next = next

class LinkList:

    def __init__(self):
        self.left = ListNode(0)
        self.right = ListNode(0, self.left)
        self.left.next = self.right
        self.map = {} # val to location
    
    def length(self):
        return len(self.map)
    
    def pushRight(self, val):
        node = ListNode(val)
        prev = self.right.prev
        node.next = self.right 
        self.right.prev = node
        node.prev = prev
        prev.next = node
        self.map[node.key] = node

    def pop(self, val):
        if val in self.map:
            node = self.map[val]
            nxt, prev = node.next, node.prev
            prev.next = nxt
            nxt.prev = prev
            self.map.pop(val, None)
    
    def popLeft(self):
        val = self.left.next.key
        self.pop(val)
        return val

    def update(self, val):
        self.pop(val)
        self.pushRight(val)

class LFUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.valMap = {}
        self.cntMap = defaultdict(int)
        self.listMap = defaultdict(LinkList)
        self.lfuCnt = 0

    def counter(self, key):
        cnt = self.cntMap[key]
        self.cntMap[key] += 1
        self.listMap[cnt].pop(key)
        self.listMap[cnt + 1].pushRight(key)

        if cnt == self.lfuCnt and self.listMap[cnt].length() == 0:
            self.lfuCnt += 1

    def get(self, key: int) -> int:
        if key not in self.valMap:
            return -1
        self.counter(key)
        return self.valMap[key]

    def put(self, key: int, value: int) -> None:
        if self.cap == 0:
            return 
        
        if key not in self.valMap and len(self.valMap) == self.cap:
            val = self.listMap[self.lfuCnt].popLeft()
            self.cntMap.pop(val)
            self.valMap.pop(val)

        self.valMap[key] = value 
        self.counter(key)
        self.lfuCnt = min(self.lfuCnt, self.cntMap[key])


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)