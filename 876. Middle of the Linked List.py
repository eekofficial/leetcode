#https://leetcode.com/problems/middle-of-the-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        current = head
        length = 0
        while current:
            length += 1
            current = current.next
        mid = length // 2
        current = head
        i = 0
        while i < mid:
            current = current.next
            i += 1
        return current
