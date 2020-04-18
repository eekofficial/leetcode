#https://leetcode.com/problems/implement-stack-using-queues/

class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue = collections.deque()
        self.queue_tmp = collections.deque()
        
    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.queue.append(x)

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        size = len(self.queue)
        for i in range(size - 1):
            self.queue_tmp.append(self.queue.popleft())
        elem = self.queue.popleft()
        self.queue = self.queue_tmp
        self.queue_tmp = collections.deque()
        return elem
        

    def top(self) -> int:
        """
        Get the top element.
        """
        size = len(self.queue)
        for i in range(size - 1):
            self.queue_tmp.append(self.queue.popleft())
        elem = self.queue.popleft()
        self.queue_tmp.append(elem)
        self.queue = self.queue_tmp
        self.queue_tmp = collections.deque()
        return elem
        
        

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return len(self.queue) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
