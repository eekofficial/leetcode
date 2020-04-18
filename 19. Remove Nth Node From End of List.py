# https://leetcode.com/problems/remove-nth-node-from-end-of-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        length = 0
        current = head
        while current:
            current = current.next
            length += 1
        
        remove_ind = length - n
        prev = None
        current = head
        i = 0
        if remove_ind == i:
            return head.next
        while current:
            prev = current
            current = current.next
            i += 1
            if i == remove_ind:
                if current:
                    prev.next = current.next
                    if current.next:
                        current = current.next.next
        return head
                    
                
            
