# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        stack = []
        while curr:
            while stack and stack[-1] < curr.val:
                stack.pop()
            stack.append(curr.val)
            curr = curr.next
        
        dummy = ListNode()
        curr = dummy
        for val in stack:
            curr.next = ListNode(val=val)
            curr = curr.next
        return dummy.next
