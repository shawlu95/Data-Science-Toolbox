class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.s1 = []
        self.s2 = []

    def push(self, x: 'int') -> 'None':
        """
        Push element x to the back of queue.
        """
        self.s1.append(x)

    def pop(self) -> 'int':
        """
        Removes the element from in front of queue and returns that element.
        """
        self.peek()
        if self.s2:
            return self.s2.pop()
        return None

    def peek(self) -> 'int':
        """
        Get the front element.
        """
        # s2 is always dequeued in queue order
        # refill s2 only after it has been emptied
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
        if self.s2:
            return self.s2[-1]
        return None

    def empty(self) -> 'bool':
        """
        Returns whether the queue is empty.
        """
        self.peek()
        return not self.s2

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()