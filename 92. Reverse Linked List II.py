# https://leetcode.com/problems/reverse-linked-list-ii/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        prev = None
        current = head
        i = 1
        while current:
            if i < m:
                prev = current
                current = current.next
            if i == m:
                before_reverse = prev
                reversed_tall = ListNode(current.val)
                reversed_head = reversed_tall
                while current:
                    if i < n:
                        prev = current
                        current = current.next
                        new_node = ListNode(current.val)
                        new_node.next = reversed_head
                        reversed_head = new_node
                    if i == n:
                        if before_reverse:
                            before_reverse.next = reversed_head
                        else:
                            head = reversed_head
                        reversed_tall.next = current.next
                        return head
                    i += 1
            i += 1
        return head
                        
                    
                
                
                
                
                
            
        
