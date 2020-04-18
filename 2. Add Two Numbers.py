#https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def add_tail(self, x):
        if not self.head:
            self.head = ListNode(x)
            return
        current = self.head
        while current.next:
            current = current.next
        new_node = ListNode(x)
        current.next = new_node
            

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        number = ''
        current_1 = l1
        current_2 = l2
        result = LinkedList()
        while current_1 and current_2:
            result.add_tail((current_1.val + current_2.val + carry) % 10)
            carry = (current_1.val + current_2.val + carry) // 10
            current_1 = current_1.next
            current_2 = current_2.next
        
        if current_1:
            current = current_1
        elif current_2:
            current = current_2
        else:
            current = None
        
        while current:
            result.add_tail((current.val + carry) % 10)
            carry = (current.val+ carry) // 10
            current = current.next
        
        if carry:
            result.add_tail(carry)
        return result.head
            
            
