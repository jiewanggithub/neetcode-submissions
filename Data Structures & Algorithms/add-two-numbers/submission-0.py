# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        pos = 0
        res = 0
        while l1 and l2:
            val = l1.val + l2.val
            val = val * 10**pos
            res += val
            pos += 1
            l1 = l1.next
            l2 = l2.next
        
        while l1:
            res += l1.val * 10**pos
            pos += 1
            l1 = l1.next

        while l2:
            res += l2.val * 10**pos
            pos += 1
            l2 = l2.next

        head = ListNode()
        cur = head
        for ch in str(res)[::-1]:
            cur.next = ListNode(int(ch))
            cur = cur.next
        return head.next
