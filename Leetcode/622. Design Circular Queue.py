from collections import deque
class MyCircularQueue:
    def __init__(self, k: int):
        self.arr = deque()
        self.K = k
    def enQueue(self, value: int) -> bool:
        if len(self.arr) == self.K:
            return False
        self.arr.append(value)
        return True

    def deQueue(self) -> bool:
        if len(self.arr) == 0:
            return False
        self.arr.popleft()
        return True

    def Front(self) -> int:
        if len(self.arr) == 0:
            return -1
        return self.arr[0]

    def Rear(self) -> int:
        if len(self.arr) == 0:
            return -1
        return self.arr[-1]

    def isEmpty(self) -> bool:
        if len(self.arr) == 0:
            return True
        else:
            return False

    def isFull(self) -> bool:
        if len(self.arr) == self.K:
            return True
        else:
            return False


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
