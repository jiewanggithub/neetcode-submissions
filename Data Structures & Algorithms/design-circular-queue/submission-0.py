class ListNode:

    def __init__(self, val:int =0, pre=None, next=None):
        self.val = val
        self.next = next
        self.pre = pre

class MyCircularQueue:

    def __init__(self, k: int):
        self.left = ListNode(0)
        self.right = ListNode(0)
        self.left.next = self.right
        self.right.pre = self.left
        self.cnt = 0
        self.k = k

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        newNode = ListNode(value)
        pre = self.right.pre
        self.right.pre = newNode
        newNode.next = self.right
        pre.next = newNode
        newNode.pre = pre 
        self.cnt += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        nxt = self.left.next.next
        self.left.next = nxt 
        nxt.pre = self.left
        self.cnt -= 1
        return True


    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.left.next.val

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.right.pre.val

    def isEmpty(self) -> bool:
        if self.right.pre == self.left and self.left.next == self.right:
            return True
        return False

    def isFull(self) -> bool:
        if self.cnt == self.k:
            return True
        return False
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()