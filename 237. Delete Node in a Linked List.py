#https://leetcode.com/problems/delete-node-in-a-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        pre_previous = None
        previous = node
        current = node.next
        while current:
            previous.val = current.val
            pre_previous = previous
            previous = current
            current = current.next
        pre_previous.next = None
        
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        
