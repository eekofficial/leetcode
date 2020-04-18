#https://leetcode.com/problems/rotate-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return None
        length = 0
        current = head
        while current:
            length += 1
            current = current.next
        k = k % length
        
        for _ in range(k):
            current = head
            while current.next.next:
                current = current.next
            new_node = ListNode(current.next.val)
            current.next = None
            new_node.next = head
            head = new_node
        return head
            
        
