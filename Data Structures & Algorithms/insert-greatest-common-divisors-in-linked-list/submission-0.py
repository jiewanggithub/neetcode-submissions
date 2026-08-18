# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
    
        def gcd(a, b):
            while b:
                a, b = b, a % b 
            return a 
        
        cur = head
        while cur.next:
            next_node = cur.next 
            new_node = ListNode(gcd(cur.val, next_node.val))
            
            cur.next = new_node
            new_node.next = next_node
            cur = next_node 
        return head
