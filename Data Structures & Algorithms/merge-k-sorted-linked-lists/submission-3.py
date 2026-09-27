# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution: 
    def mergeTwoSortedLists(self, list1, list2):
        head1, head2 = list1, list2
        head = ListNode()
        head_res = head
        while head1 and head2:
            if head1.val < head2.val:
                head_res.next = head1
                head1 = head1.next
            else:
                head_res.next = head2
                head2 = head2.next
            head_res = head_res.next
        
        if head1:
            head_res.next = head1
        
        if head2:
            head_res.next = head2
        
        return head.next

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        while len(lists) > 1:
            merged = []
            for i in range(0, len(lists), 2):
                list1 = lists[i]
                if i + 1 < len(lists):
                    list2 = lists[i + 1]
                else:
                    list2 = None
                
                merged.append(self.mergeTwoSortedLists(list1, list2))
                 
            lists = merged
        return lists[0]


