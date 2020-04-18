# https://leetcode.com/problems/min-stack/

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        

    def push(self, x: int) -> None:
        if len(self.stack) == 0:
            self.stack.append((x, x))
        else:
            prev_min = self.getMin()
            if x < prev_min:
                self.stack.append((x, x))
            else:
                self.stack.append((x, prev_min))

    def pop(self) -> None:
        return self.stack.pop()[0]

    def top(self) -> int:
        return self.stack[len(self.stack) - 1][0]

    def getMin(self) -> int:
        return self.stack[len(self.stack) - 1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

##[[],[-2],[0],[-1],[],[],[],[]]
