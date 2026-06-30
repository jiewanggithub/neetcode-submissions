class ListNode:
    
    def __init__(self, key, val=0, pre=None, next=None):
        self.key = key
        self.val = val
        self.pre = pre
        self.next = next 

class LRUCache:

    def __init__(self, capacity: int):
        self.hashmap = {} # key, node placeholder pointer
        self.capacity = capacity
        self.cnt = 0
        self.left = ListNode(0)
        self.right = ListNode(0)
        self.left.next = self.right
        self.right.pre = self.left

    def get(self, key: int) -> int:
        if self.hashmap and key in self.hashmap:
            node = self.hashmap[key]

            node.pre.next = node.next
            node.next.pre = node.pre
            
            pre = self.right.pre
            self.right.pre = node
            node.next = self.right
            node.pre = pre
            pre.next = node
            return node.val
        
        return -1
        

    def put(self, key: int, value: int) -> None:
        # key does exist in the hashmap
        if self.hashmap and key in self.hashmap:
            self.hashmap[key].val = value
            self.get(key)
        else:
            # key doesn't exist in the hashmap 
            newNode = ListNode(key, value)
            if self.cnt == self.capacity:
                delete = self.left.next
                nxt = self.left.next.next 
                self.left.next = nxt
                nxt.pre = self.left
                del self.hashmap[delete.key]
                self.cnt -= 1
            self.hashmap[key] = newNode
            pre = self.right.pre 
            pre.next = newNode
            newNode.pre = pre 
            newNode.next = self.right
            self.right.pre = newNode
            self.cnt += 1






