class ListNode():
    def __init__(self, key=0, val=0):
        self.key, self.val = key, val
        self.pre = self.next = None

class LRUCache:

    # most least recently used is on the right side 
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        self.left, self.right = ListNode(), ListNode()
        self.left.next, self.right.pre = self.right, self.left

    def insert(self, node):
        # insert to the left 
        after_left = self.left.next
        self.left.next, after_left.pre = node, node
        node.pre = self.left
        node.next = after_left

    def remove(self, node):
        nxt, pre = node.next, node.pre
        pre.next, nxt.pre = nxt, pre

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1 

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = ListNode(key, value)
        self.insert(self.cache[key])
        
        if len(self.cache) > self.cap:
            lru = self.right.pre
            self.remove(lru)
            del self.cache[lru.key]

        


        
