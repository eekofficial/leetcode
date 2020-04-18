#https://leetcode.com/problems/palindrome-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        s = ''
        reversed_s = ''
        while head:
            s += str(head.val)
            reversed_s = str(head.val) + reversed_s 
            head = head.next
        return s == reversed_s
