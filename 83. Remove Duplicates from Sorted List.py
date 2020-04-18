#https://leetcode.com/problems/remove-duplicates-from-sorted-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return None
        new_head = ListNode(head.val)
        new_current = new_head
        current = head.next
        while head:
            if head.val != new_current.val:
                new_current.next = ListNode(head.val)
                new_current = new_current.next
            head = head.next
        return new_head
        
