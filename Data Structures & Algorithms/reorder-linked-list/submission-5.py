# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def findMid(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = head
        slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        return slow 
    
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pre = None
        curr = head
        while curr:
            nxt = curr.next
            curr.next = pre
            pre = curr
            curr = nxt
        return pre

    def reorderList(self, head: Optional[ListNode]) -> None:
        mid = self.findMid(head)
        endHead = self.reverseList(mid)
      
        while endHead.next:
            nxt = head.next
            nxt2 = endHead.next
            head.next = endHead
            endHead.next = nxt
            endHead = nxt2 
            head = nxt 
        
        
        
        

        

    