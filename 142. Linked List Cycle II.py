# https://leetcode.com/problems/linked-list-cycle-ii/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if not head:
            return None
        fast_pointer = head
        slow_pointer = head
        ind = 0
        while fast_pointer and fast_pointer.next:
            fast_pointer = fast_pointer.next.next
            slow_pointer = slow_pointer.next
            if slow_pointer == fast_pointer:
                while head:
                    if head == slow_pointer:
                        return head
                    else:
                        head = head.next
                        slow_pointer = slow_pointer.next
        return None
