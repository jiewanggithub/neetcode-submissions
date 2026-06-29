# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        head1 = head
        head2 = head
        while head1 and head1.next:
            head1 = head1.next.next
            head2 = head2.next
            if head1 == head2 and head1.val == head2.val:
                return True 
        return False
        