# https://leetcode.com/problems/add-two-numbers-ii/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        num1 = 0
        num2 = 0
        current_l1 = l1
        
        while current_l1:
            num1 = 10 * num1 + current_l1.val
            current_l1 = current_l1.next
        
        current_l2 = l2
        
        while current_l2:
            num2 = 10 * num2 + current_l2.val
            current_l2 = current_l2.next
        
        res = str(num1 + num2)
        head = ListNode(int(res[0]))
        for i in range(1, len(res)):
            current = head
            while current.next:
                current = current.next
            current.next = ListNode(int(res[i]))
        return head
        
            
