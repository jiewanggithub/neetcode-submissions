# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        leftPre, cur = dummy, head

        for _ in range(left - 1):
            leftPre = leftPre.next
            cur = cur.next
        # leftPre: the one before reverse
        # cur: node at position left

        pre = None
        tail = cur
        # right - left + 1: including all end nodes
        for _ in range(right - left + 1):
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt
        
        # original node on left point to None
        # original node on right point to previous one (reverse)

        # the node on right should be the nxt of leftPre
        # the node on left should point to cur (the one out of the reverse range)

        leftPre.next = pre
        tail.next = cur
        return dummy.next
        




          
