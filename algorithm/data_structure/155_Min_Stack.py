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
        if len(self.stack) == 0:
            self.idx.append(0)
        else:
            if self.stack[self.idx[-1]] >= x:
                # x is the new min
                self.idx.append(len(self.stack))
            else:
                # duplicate old idx
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
        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.stack[self.idx[-1]]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()