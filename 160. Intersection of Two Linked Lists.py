# 160. Intersection of Two Linked Lists

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        a_dict = dict()
        b_dict = dict()
        current_a = headA
        current_b = headB
        while current_a:
            a_dict[current_a] = True
            current_a = current_a.next
        while current_b:
            b_dict[current_b] = True
            current_b = current_b.next
        for node in a_dict.keys():
            if b_dict.get(node) != None:
                return node
        return None
