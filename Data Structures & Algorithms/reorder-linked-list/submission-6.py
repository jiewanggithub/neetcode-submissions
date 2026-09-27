# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        def reverseList(head):
            cur = head
            pre = None
            
            while cur:
                nxt = cur.next
                cur.next = pre
                pre = cur
                cur = nxt
            return pre
        def merge(node1, node2):
            cur = ListNode()
            dummy = cur
            while node1 and node2:
                dummy.next = node1
                node1 = node1.next
                dummy.next.next = node2
                node2 = node2.next
                dummy = dummy.next.next
            if node1:
                dummy.next = node1
            if node2:
                dummy.next = node2
            return dummy.next

        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        second = slow.next
        slow.next = None
        second = reverseList(second)
        merge(head, second)



        
