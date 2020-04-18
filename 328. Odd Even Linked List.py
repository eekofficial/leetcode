# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if head and head.next and head.next.next:
            last_odd = head
            prev = head.next
            current = head.next.next
            while current:
                new_node = ListNode(current.val)
                new_node.next = last_odd.next
                last_odd.next = new_node
                last_odd = new_node
                if current.next:
                    prev.next = current.next
                    prev = current.next
                    if current.next:
                        current = current.next.next
                else:
                    prev.next = None
                    current = current.next


            
        return head
            
        
