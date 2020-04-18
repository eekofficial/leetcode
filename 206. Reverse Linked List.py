#https://leetcode.com/problems/reverse-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head == None:
            return None
        reversed_head_old = ListNode(head.val)
        current = head.next
        while current:
            reversed_head = ListNode(current.val)
            reversed_head.next = reversed_head_old
            reversed_head_old = reversed_head
            current = current.next
        return reversed_head_old
            
            
                
        
