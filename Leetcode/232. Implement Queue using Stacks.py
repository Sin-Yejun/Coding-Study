class MyQueue(object):

    def __init__(self):
        self.arr = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.arr.append(x)

    def pop(self):
        """
        :rtype: int
        """
        self.arr = self.arr[::-1]
        x = self.arr.pop()
        self.arr = self.arr[::-1]
        return x

    def peek(self):
        """
        :rtype: int
        """
        return self.arr[0]

    def empty(self):
        """
        :rtype: bool
        """
        if len(self.arr) == 0:
            return True
        else:
            return False
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()