# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        curr = head
        n = 0
        while curr:
            curr = curr.next
            n += 1

        dummy = ListNode(next=head)
        p0 = dummy
        prev = None
        curr = p0.next
        while n >= k:
            n -= k
            for _ in range(k):
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            
            nxt = p0.next
            p0.next.next = curr
            p0.next = prev
            p0 = nxt 
        return dummy.next