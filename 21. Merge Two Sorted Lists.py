#https://leetcode.com/problems/merge-two-sorted-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 == None and l2 == None:
            return None
        
        if l1 == None:
            head = ListNode(l2.val)
            current = head
            current_l2 = l2.next
            current_l1 = None
        elif l2 == None:
            head = ListNode(l1.val)
            current = head
            current_l1 = l1.next
            current_l2 = None
        elif l1.val < l2.val:
            head = ListNode(l1.val)
            current_l1 = l1.next
            current_l2 = l2
            current = head
        else:
            head = ListNode(l2.val)
            current_l2 = l2.next
            current_l1 = l1
            current = head
        while current_l1 and current_l2:
            if current_l1.val <= current_l2.val:
                current.next = ListNode(current_l1.val)
                current_l1 = current_l1.next
            else:
                current.next = ListNode(current_l2.val)
                current_l2 = current_l2.next
            current = current.next
        
        while current_l1:
            current.next = ListNode(current_l1.val)
            current = current.next
            current_l1 = current_l1.next
        
        while current_l2:
            current.next = ListNode(current_l2.val)
            current = current.next
            current_l2 = current_l2.next
        return head
        
