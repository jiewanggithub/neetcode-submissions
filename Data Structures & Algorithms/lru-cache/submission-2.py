class ListNode():
    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.pre = None
        self.next = None

class LRUCache():
    def __init__(self, capacity):
        self.cap = capacity
        self.cache = {}

        self.left = ListNode()
        self.right = ListNode()
        self.left.next = self.right
        self.right.pre = self.left
    
    def remove(self, node):
        pre, nxt = node.pre, node.next
        pre.next, nxt.pre = nxt, pre
    
    def insert_to_right(self, node):
        pre, nxt = self.right.pre, self.right
        pre.next = node
        nxt.pre = node
        node.next = self.right
        node.pre = pre 
    
    def get(self, key):
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert_to_right(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key, val):
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = ListNode(key, val)
        self.insert_to_right(self.cache[key])

        if len(self.cache) > self.cap:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
        
    







