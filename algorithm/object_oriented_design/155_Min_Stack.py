class MinStack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.idx = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        # stack is just a regular stack
        # idx keep track of minimum element's index
        if len(self.stack) == 0:
            self.idx.append(0)
        else:
            if self.stack[self.idx[-1]] >= x:
                self.idx.append(len(self.stack))
            else:
                self.idx.append(self.idx[-1])
        self.stack.append(x)

    def pop(self):
        """
        :rtype: void
        """
        self.idx.pop()
        self.stack.pop()

    def top(self):
        """
        :rtype: int
        """
        # just like regular stack
        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        # does not pop idx or stack
        return self.stack[self.idx[-1]]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()