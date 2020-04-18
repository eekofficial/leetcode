#https://leetcode.com/problems/swap-nodes-in-pairs/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head:
            return None
        if not head.next:
            return head
        pre_prev = None
        prev = head
        current = head.next
        prev.next = current.next
        current.next = prev
        head = current
        if not head.next.next:
            return head
    
        pre_prev = head.next
        prev = head.next.next
        current = head.next.next.next
        while current:
            prev.next = current.next
            current.next = prev
            pre_prev.next = current
            pre_prev = prev.next
            current = prev
            prev = current
            
            pre_prev = current
            prev = current.next
            if current.next:
                current = current.next.next
            else:
                current = current.next
            
            
            
            
        return head
