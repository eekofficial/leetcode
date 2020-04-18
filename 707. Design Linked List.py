#https://leetcode.com/problems/design-linked-list/

class ListNode:
    
    def __init__(self, x):
        self.prev = None
        self.val = x
        self.next = None

class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None
        

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        if not self.head:
            return -1
        current = self.head
        i = 0
        while current:
            if index == i:
                return current.val
            i += 1
            current = current.next
        return -1
        

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        if not self.head:
            self.head = ListNode(val)
        new_head = ListNode(val)
        self.head.prev = new_head
        new_head.next = self.head
        self.head = new_head
        
        

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        current = self.head
        while current.next:
            current = current.next
        new_tail = ListNode(val)
        new_tail.prev = current
        current.next = new_tail
        
        

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        if index == 0:
            return self.AddAtHead(val)
        current = self.head
        i = 0
        while current:
            if index == i:
                new_node = ListNode(val)
                current.prev.next = new_node
                new_node.prev = current.prev
                new_node.next = current
            i += 1
            current = current.next
        
        

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if index == 0:
            return self.head.next
        current = self.head
        i = 0
        while current:
            if index == i:
                if current.next:
                    current.prev.next = current.next
                    current.next.prev = current.prev
                else:
                    current.prev.next = None
            i += 1
            current = current.next

        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
