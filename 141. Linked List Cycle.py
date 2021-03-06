# https://leetcode.com/problems/linked-list-cycle/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head:
            return False
        slow_pointer = head
        fast_pointer = head
        
        while fast_pointer and slow_pointer:
            if fast_pointer.next:
                    fast_pointer = fast_pointer.next.next
            else:
                return False
            slow_pointer = slow_pointer.next
            if fast_pointer == slow_pointer:
                return True
        return False
        
