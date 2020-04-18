#https://leetcode.com/problems/remove-linked-list-elements/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        previous = None
        current = head
        
        while current:
            if current.val == val and previous == None:
                head = current.next
            elif current.val == val:
                previous.next = current.next
            else:
                previous = current
            current = current.next
        return head
